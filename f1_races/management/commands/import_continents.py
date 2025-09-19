# f1_races/management/commands/import_sessions_engines_manufacturers.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from f1_races.models import sessions_engines_manufacturers, sessions, enginesManufacturers

class Command(BaseCommand):
    help = 'Importa e atualiza dados de fabricantes de motores de sessões de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='O caminho para o arquivo CSV de fabricantes de motores de sessões.')

    def handle(self, *args, **options):
        csv_path = options['csv_file']
        
        try:
            # Pré-carrega os objetos relacionados para busca rápida
            sessions_map = {s.year: s for s in sessions.objects.all()}
            engines_map = {em.enginesManufacturersID: em for em in enginesManufacturers.objects.all()}

            # Funções auxiliares para conversão de tipo e tratamento de valores vazios
            def get_int_or_none(value):
                return int(value) if value else None

            def get_float_or_none(value):
                return float(value) if value else None
                
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                total_rows = 0
                updated_count = 0
                created_count = 0

                with transaction.atomic():
                    for row in reader:
                        total_rows += 1
                        
                        # Mapeia as chaves estrangeiras
                        year_obj = sessions_map.get(get_int_or_none(row.get('year')))
                        engine_obj = engines_map.get(row.get('engineManufacturerId'))

                        if not year_obj or not engine_obj:
                            self.stdout.write(
                                self.style.WARNING(f"Aviso: 'year' ou 'engineManufacturerId' não encontrados. Linha ignorada: {row}")
                            )
                            continue

                        # Mapeia a coluna 'totalRaceStarts' do CSV, que não está no modelo,
                        # para evitar KeyError
                        row.pop('totalRaceStarts', None)

                        defaults = {
                            'positionNumber': get_int_or_none(row.get('positionNumber')),
                            'positionText': row.get('positionText', ''),
                            'bestStartingGridPosition': get_int_or_none(row.get('bestStartingGridPosition')),
                            'bestRaceResult': get_int_or_none(row.get('bestRaceResult')),
                            'totalRaceEntries': get_int_or_none(row.get('totalRaceEntries')),
                            'totalRaceWins': get_int_or_none(row.get('totalRaceWins')),
                            'totalRaceLaps': get_int_or_none(row.get('totalRaceLaps')),
                            'totalPodiums': get_int_or_none(row.get('totalPodiums')),
                            'totalPodiumRaces': get_int_or_none(row.get('totalPodiumRaces')),
                            'totalPoints': get_float_or_none(row.get('totalPoints')),
                            'totalPolePositions': get_int_or_none(row.get('totalPolePositions')),
                            'totalFastestLaps': get_int_or_none(row.get('totalFastestLaps')),
                        }
                        
                        obj, created = sessions_engines_manufacturers.objects.update_or_create(
                            year=year_obj,
                            enginesManufacturerID=engine_obj,
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