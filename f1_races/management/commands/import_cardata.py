import csv
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

# IMPORTANTE: Substitua 'dados_carro' pelo nome real do seu app Django.
from f1_races.models import car_data 

class Command(BaseCommand):
    help = 'Importa dados de telemetria de um arquivo CSV para o banco de dados.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='O caminho completo para o arquivo CSV a ser importado.')

    def handle(self, *args, **kwargs):
        caminho_arquivo = kwargs['csv_file_path']
        self.stdout.write(self.style.SUCCESS(f'Iniciando a importação do arquivo: {caminho_arquivo}'))

        registros_criados = 0
        registros_atualizados = 0

        try:
            with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
                # DictReader é ideal pois usa o cabeçalho do CSV como chaves do dicionário.
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        # O método update_or_create é perfeito para a sua regra 'unique_together'.
                        # Ele usará os campos a seguir para buscar um registro.
                        obj, created = car_data.objects.update_or_create(
                            driver_number=row['driver_number'],
                            session_key=row['session_key'],
                            date=row['date'],
                            # O dicionário 'defaults' contém os campos que serão atualizados
                            # ou usados para criar o novo registro.
                            defaults={
                                'speed': row['speed'],
                                'throttle': row['throttle'],
                                'brake': row['brake'],
                                'n_gear': row['n_gear'],
                                'meeting_key': row['meeting_key'],
                            }
                        )
                        
                        if created:
                            registros_criados += 1
                            self.stdout.write(self.style.SUCCESS(f'Registro criado: {obj}'))
                        else:
                            registros_atualizados += 1
                            self.stdout.write(self.style.WARNING(f'Registro atualizado: {obj}'))

                    except ValidationError as e:
                        self.stdout.write(self.style.ERROR(f'Erro de validação na linha {reader.line_num}: {row}'))
                        self.stdout.write(self.style.ERROR(f'Detalhes do erro: {e}'))
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(f'Erro de coluna na linha {reader.line_num}: a coluna {e} não foi encontrada no CSV.'))
                        self.stdout.write(self.style.ERROR('Verifique se o cabeçalho do CSV corresponde aos campos esperados.'))
                        # Interrompe a execução se uma coluna essencial estiver faltando.
                        return


        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'ERRO: O arquivo "{caminho_arquivo}" não foi encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))

        # Relatório final da importação
        self.stdout.write(self.style.SUCCESS('---------------------------------'))
        self.stdout.write(self.style.SUCCESS('Importação concluída!'))
        self.stdout.write(self.style.SUCCESS(f'Total de registros criados: {registros_criados}'))
        self.stdout.write(self.style.SUCCESS(f'Total de registros atualizados: {registros_atualizados}'))

