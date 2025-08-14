# f1_races/management/commands/create_driver_session_relations.py

import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from f1_races.models import driver, sessions

class Command(BaseCommand):
    help = 'Cria relacionamentos entre pilotos e sessões a partir de um arquivo CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='O caminho completo para o arquivo CSV de relacionamentos.')

    def handle(self, *args, **kwargs):
        caminho_arquivo = kwargs['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando a criação de relacionamentos do arquivo: {caminho_arquivo}'))

        relacionamentos_criados = 0

        try:
            with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                with transaction.atomic():
                    for row in reader:
                        try:
                            # 1. Busque a instância do piloto (driver)
                            driver_obj = driver.objects.get(driver_number=row['driver_number'])

                            # 2. Busque a instância da sessão (sessions)
                            session_obj = sessions.objects.get(session_key=row['session_key'])

                            # 3. Use o .add() para criar o relacionamento ManyToMany
                            driver_obj.sessions.add(session_obj)
                            
                            relacionamentos_criados += 1
                        
                        except driver.DoesNotExist:
                            self.stdout.write(self.style.WARNING(
                                f"Linha {reader.line_num}: Piloto com número {row['driver_number']} não encontrado. Pulando."
                            ))
                        except sessions.DoesNotExist:
                            self.stdout.write(self.style.WARNING(
                                f"Linha {reader.line_num}: Sessão com chave {row['session_key']} não encontrada. Pulando."
                            ))
                        except KeyError as e:
                            self.stdout.write(self.style.ERROR(
                                f"Erro na linha {reader.line_num}: A coluna {e} não foi encontrada no CSV. Verifique o cabeçalho."
                            ))
                            return # Sai do comando em caso de erro crítico

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'ERRO: O arquivo "{caminho_arquivo}" não foi encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))

        self.stdout.write(self.style.SUCCESS('---------------------------------'))
        self.stdout.write(self.style.SUCCESS('Criação de relacionamentos concluída!'))
        self.stdout.write(self.style.SUCCESS(f'Total de relacionamentos criados: {relacionamentos_criados}'))