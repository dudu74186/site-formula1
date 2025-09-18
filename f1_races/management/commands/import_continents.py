# f1_races/management/commands/import_races_race_results.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from f1_races.models import (
    races_race_results, races, sessions, drivers,
    constructors, enginesManufacturers, tyreManufacturers
)
from datetime import timedelta

class Command(BaseCommand):
    help = 'Importa e atualiza dados dos resultados de corridas de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='O caminho para o arquivo CSV dos resultados de corridas.')

    def handle(self, *args, **options):
        csv_path = options['csv_file']
        
        try:
            # Pré-carrega os objetos relacionados para busca rápida
            races_map = {r.racesID: r for r in races.objects.all()}
            sessions_map = {s.year: s for s in sessions.objects.all()}
            drivers_map = {d.driversID: d for d in drivers.objects.all()}
            constructors_map = {c.constructorsID: c for c in constructors.objects.all()}
            engines_map = {em.enginesManufacturersID: em for em in enginesManufacturers.objects.all()}
            tyres_map = {tm.tyreManufacturersID: tm for tm in tyreManufacturers.objects.all()}

            # Funções auxiliares para conversão de tipo e tratamento de valores vazios
            def get_int_or_none(value):
                return int(value) if value else None

            def get_float_or_none(value):
                return float(value) if value else None

            def get_bool_or_false(value):
                return value.lower() in ['true', '1', 't', 'y'] if value else False
            
            def get_duration_or_none(value):
                if not value:
                    return None
                try:
                    # Assume que o formato do CSV pode ser 'HH:MM:SS.ms' ou 'MM:SS.ms' ou 'SS.ms'
                    parts = value.split(':')
                    if len(parts) == 3: # HH:MM:SS.ms
                        hours, minutes, seconds_part = parts
                    elif len(parts) == 2: # MM:SS.ms
                        hours = 0
                        minutes, seconds_part = parts
                    elif len(parts) == 1: # SS.ms
                        hours = 0
                        minutes = 0
                        seconds_part = parts[0]
                    else:
                        return None
                        
                    seconds_str, millis_str = seconds_part.split('.') if '.' in seconds_part else (seconds_part, '0')
                    
                    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds_str)
                    total_milliseconds = int(millis_str)
                    return timedelta(seconds=total_seconds, milliseconds=total_milliseconds)
                except (ValueError, IndexError):
                    return None
                
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                total_rows = 0
                updated_count = 0
                created_count = 0

                with transaction.atomic():
                    for row in reader:
                        total_rows += 1
                        
                        # Mapeia as chaves estrangeiras
                        race_obj = races_map.get(row.get('raceId'))
                        year_obj = sessions_map.get(get_int_or_none(row.get('year')))
                        driver_obj = drivers_map.get(row.get('driverId'))
                        constructor_obj = constructors_map.get(row.get('constructorId'))
                        engine_obj = engines_map.get(row.get('engineManufacturerId'))
                        tyre_obj = tyres_map.get(row.get('tyreManufacturerId'))
                        
                        if not race_obj or not year_obj or not driver_obj:
                            self.stdout.write(
                                self.style.WARNING(f"Aviso: 'raceId', 'year' ou 'driverId' não encontrados. Linha ignorada: {row}")
                            )
                            continue

                        defaults = {
                            'year': year_obj,
                            'round': get_int_or_none(row.get('round')),
                            'positionDisplayOrder': get_int_or_none(row.get('positionDisplayOrder')),
                            'positionNumber': get_int_or_none(row.get('positionNumber')),
                            'positionText': row.get('positionText', ''),
                            'driverNumber': get_int_or_none(row.get('driverNumber')),
                            'driverID': driver_obj,
                            'constructorsID': constructor_obj,
                            'engineManufacturerID': engine_obj,
                            'tyreManufacturersID': tyre_obj,
                            'sharedCar': get_bool_or_false(row.get('sharedCar')),
                            'laps': get_int_or_none(row.get('laps')),
                            'time': get_duration_or_none(row.get('time')),
                            'timeMillis': get_int_or_none(row.get('timeMillis')),
                            'timePenalty': get_duration_or_none(row.get('timePenalty')),
                            'timePenaltyMillis': get_int_or_none(row.get('timePenaltyMillis')),
                            'gap': get_duration_or_none(row.get('gap')),
                            'gapMillis': get_int_or_none(row.get('gapMillis')),
                            'gapLaps': get_int_or_none(row.get('gapLaps')),
                            'interval': get_duration_or_none(row.get('interval')),
                            'intervalMillis': get_int_or_none(row.get('intervalMillis')),
                            'reasonRetired': row.get('reasonRetired', ''),
                            'points': get_float_or_none(row.get('points')),
                            'polePosition': get_bool_or_false(row.get('polePosition')),
                            'qualificationPositionNumber': get_int_or_none(row.get('qualificationPositionNumber')),
                            'qualificationPositionText': row.get('qualificationPositionText', ''),
                            'gridPositionNumber': get_int_or_none(row.get('gridPositionNumber')),
                            'gridPositionText': row.get('gridPositionText', ''),
                            'positionGained': get_int_or_none(row.get('positionsGained')),
                            'pitStops': get_int_or_none(row.get('pitStops')),
                            'fastestLap': get_bool_or_false(row.get('fastestLap')),
                            'driverOfTheDay': get_bool_or_false(row.get('driverOfTheDay')),
                            'grandSlam': get_bool_or_false(row.get('grandSlam')),
                        }

                        obj, created = races_race_results.objects.update_or_create(
                            raceID=race_obj,
                            driverID=driver_obj, 
                            defaults=defaults
                        )

                        if created:
                            created_count += 1
                        else:
                            updated_count += 1

                self.stdout.write(self.style.SUCCESS(f'Importação concluída. {total_rows} linhas processadas.'))
                self.stdout.write(self.style.SUCCESS(f'Criados: {created_count} | Atualizados: {updated_count}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Erro: O arquivo {csv_path} não foi encontrado.'))
        except ValueError as ve:
            self.stdout.write(self.style.ERROR(f'Erro de conversão de tipo: {ve}. Verifique os dados no CSV.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))