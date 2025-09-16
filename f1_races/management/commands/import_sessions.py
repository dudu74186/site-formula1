# f1_races/management/commands/import_sessions.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from f1_races.models import sessions

class Command(BaseCommand):
    help = 'Importa dados de sessões de um arquivo CSV para o banco de dados.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='O caminho completo para o arquivo CSV de sessões.')

    def handle(self, *args, **kwargs):
        caminho_arquivo = kwargs['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando a importação do arquivo de sessões: {caminho_arquivo}'))

        registros_criados = 0
        registros_atualizados = 0

        try:
            with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                with transaction.atomic():
                    for row in reader:
                        try:
                            # Converte 'year' e outras chaves numéricas para o tipo correto.
                            row['year'] = int(row['year'])
                            
                            obj, created = sessions.objects.update_or_create(
                                session_key=row['session_key'], # Chave para buscar/criar o objeto
                                defaults={ # Campos a serem atualizados ou usados na criação
                                    'circuit_key': row.get('circuit_key'),
                                    'circuit_short_name': row.get('circuit_short_name'),
                                    'country_code': row.get('country_code'),
                                    'country_key': row.get('country_key'),
                                    'country_name': row.get('country_name'),
                                    'date_end': row.get('date_end'),
                                    'date_start': row.get('date_start'),
                                    'gmt_offset': row.get('gmt_offset'),
                                    'location': row.get('location'),
                                    'meeting_key': row.get('meeting_key'),
                                    'session_name': row.get('session_name'),
                                    'session_type': row.get('session_type'),
                                    'year': row['year'],
                                }
                            )
                            if created:
                                registros_criados += 1
                            else:
                                registros_atualizados += 1
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f'Erro na linha {reader.line_num}: {e} -> {row}'))
                            
            self.stdout.write(self.style.SUCCESS('---------------------------------'))
            self.stdout.write(self.style.SUCCESS(f'Importação de sessões concluída!'))
            self.stdout.write(self.style.SUCCESS(f'Total de registros criados: {registros_criados}'))
            self.stdout.write(self.style.SUCCESS(f'Total de registros atualizados: {registros_atualizados}'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'ERRO: O arquivo "{caminho_arquivo}" não foi encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))