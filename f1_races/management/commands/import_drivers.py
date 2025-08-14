# f1_races/management/commands/import_drivers.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from f1_races.models import driver

class Command(BaseCommand):
    help = 'Importa dados de pilotos de um arquivo CSV para o banco de dados.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='O caminho completo para o arquivo CSV de pilotos.')

    def handle(self, *args, **kwargs):
        caminho_arquivo = kwargs['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando a importação do arquivo de pilotos: {caminho_arquivo}'))

        registros_criados = 0
        registros_atualizados = 0

        try:
            with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                with transaction.atomic():
                    for row in reader:
                        try:
                            # Processa 'team_colour' para garantir que tenha '#' no início
                            team_colour_value = row.get('team_colour')
                            if team_colour_value and not team_colour_value.startswith('#'):
                                team_colour_value = '#' + team_colour_value
                            
                            # Converte 'driver_number' para o tipo correto
                            row['driver_number'] = int(row['driver_number'])

                            obj, created = driver.objects.update_or_create(
                                driver_number=row['driver_number'], # Chave para buscar/criar
                                defaults={
                                    'broadcast_name': row.get('broadcast_name'),
                                    'first_name': row.get('first_name'),
                                    'full_name': row.get('full_name'),
                                    'last_name': row.get('last_name'),
                                    'team_colour': team_colour_value,
                                    'team_name': row.get('team_name'),
                                    'country_code': row.get('country_code'),
                                    'headshot_url': row.get('headshot_url'),
                                    'name_acronym': row.get('name_acronym'),
                                }
                            )
                            if created:
                                registros_criados += 1
                            else:
                                registros_atualizados += 1
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f'Erro na linha {reader.line_num}: {e} -> {row}'))

            self.stdout.write(self.style.SUCCESS('---------------------------------'))
            self.stdout.write(self.style.SUCCESS(f'Importação de pilotos concluída!'))
            self.stdout.write(self.style.SUCCESS(f'Total de registros criados: {registros_criados}'))
            self.stdout.write(self.style.SUCCESS(f'Total de registros atualizados: {registros_atualizados}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'ERRO: O arquivo "{caminho_arquivo}" não foi encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))