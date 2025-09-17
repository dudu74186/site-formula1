# f1_races/management/commands/import_races.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from f1_races.models import races, sessions, grandPrix, circuits
from datetime import datetime, time

class Command(BaseCommand):
    help = 'Importa e atualiza dados de corridas de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='O caminho para o arquivo CSV de corridas.')

    def handle(self, *args, **options):
        csv_path = options['csv_file']
        
        try:
            # Pré-carrega os objetos relacionados para busca rápida
            sessions_map = {s.year: s for s in sessions.objects.all()}
            grand_prix_map = {gp.grandPrixID: gp for gp in grandPrix.objects.all()}
            circuits_map = {c.circuitsID: c for c in circuits.objects.all()}

            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                total_rows = 0
                updated_count = 0
                created_count = 0

                # Funções auxiliares para conversão de tipo e tratamento de valores vazios
                def get_int_or_none(value):
                    return int(value) if value else None

                def get_float_or_none(value):
                    return float(value) if value else None

                def get_date_or_none(value):
                    try:
                        return datetime.strptime(value, '%Y-%m-%d').date() if value else None
                    except (ValueError, TypeError):
                        return None
                        
                def get_time_or_none(value):
                    try:
                        return datetime.strptime(value, '%H:%M:%S').time() if value else None
                    except (ValueError, TypeError):
                        return None

                def get_bool_or_false(value):
                    return value.lower() == 'true' if value else False
                
                with transaction.atomic():
                    for row in reader:
                        total_rows += 1
                        
                        # Mapeia as chaves estrangeiras
                        year_obj = sessions_map.get(get_int_or_none(row.get('year')))
                        grand_prix_obj = grand_prix_map.get(row.get('grandPrixId'))
                        circuits_obj = circuits_map.get(row.get('circuitId'))
                        
                        defaults = {
                            'year': year_obj,
                            'round': get_int_or_none(row.get('round')),
                            'date': get_date_or_none(row.get('date')),
                            'time': get_time_or_none(row.get('time')),
                            'grandPrixID': grand_prix_obj,
                            'officialName': row.get('officialName'),
                            'qualifyingFormat': row.get('qualifyingFormat'),
                            'sprintQualifyingFormat': row.get('sprintQualifyingFormat'),
                            'circuitsID': circuits_obj,
                            'direction': row.get('direction'),
                            'courseLength': get_float_or_none(row.get('courseLength')),
                            'turns': get_int_or_none(row.get('turns')),
                            'laps': get_int_or_none(row.get('laps')),
                            'distance': get_float_or_none(row.get('distance')),
                            'scheduledLaps': get_int_or_none(row.get('scheduledLaps')),
                            'scheduledDistance': get_float_or_none(row.get('scheduledDistance')),
                            'driversChampionshipDecider': get_bool_or_false(row.get('driversChampionshipDecider')),
                            'constructorsChampionshipDecider': get_bool_or_false(row.get('constructorsChampionshipDecider')),
                            'preQualifyingDate': get_date_or_none(row.get('preQualifyingDate')),
                            'preQualifyingTime': get_time_or_none(row.get('preQualifyingTime')),
                            'freePractice1Date': get_date_or_none(row.get('freePractice1Date')),
                            'freePractice1Time': get_time_or_none(row.get('freePractice1Time')),
                            'freePractice2Date': get_date_or_none(row.get('freePractice2Date')),
                            'freePractice2Time': get_time_or_none(row.get('freePractice2Time')),
                            'freePractice3Date': get_date_or_none(row.get('freePractice3Date')),
                            'freePractice3Time': get_time_or_none(row.get('freePractice3Time')),
                            'freePractice4Date': get_date_or_none(row.get('freePractice4Date')),
                            'freePractice4Time': get_time_or_none(row.get('freePractice4Time')),
                            'qualifying1Date': get_date_or_none(row.get('qualifying1Date')),
                            'qualifying1Time': get_time_or_none(row.get('qualifying1Time')),
                            'qualifying2Date': get_date_or_none(row.get('qualifying2Date')),
                            'qualifying2Time': get_time_or_none(row.get('qualifying2Time')),
                            'qualifyingDate': get_date_or_none(row.get('qualifyingDate')),
                            'qualifyingTime': get_time_or_none(row.get('qualifyingTime')),
                            'sprintQualifyingDate': get_date_or_none(row.get('sprintQualifyingDate')),
                            'sprintQualifyingTime': get_time_or_none(row.get('sprintQualifyingTime')),
                            'sprintRaceDate': get_date_or_none(row.get('sprintRaceDate')),
                            'sprintRaceTime': get_time_or_none(row.get('sprintRaceTime')),
                            'warmingUpDate': get_date_or_none(row.get('warmingUpDate')),
                            'warmingUpTime': get_time_or_none(row.get('warmingUpTime'))
                        }

                        obj, created = races.objects.update_or_create(
                            racesID=row['id'],
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
            self.stdout.write(self.style.ERROR(f'Erro de conversão de tipo: {ve}. Verifique os dados numéricos e de data no CSV.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))