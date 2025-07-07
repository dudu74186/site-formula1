import csv
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

# IMPORTANTE: Substitua 'dados_carro' pelo nome real do seu app Django.
from f1_races.models import driver

class Command(BaseCommand):
    """
    Comando de gerenciamento do Django para importar dados de telemetria de um arquivo CSV 
    para o modelo car_data.
    """
    help = 'Importa dados de telemetria de um arquivo CSV para o banco de dados.'

    def add_arguments(self, parser):
        """
        Adiciona o argumento da linha de comando para o caminho do arquivo CSV.
        """
        parser.add_argument('csv_file_path', type=str, help='O caminho completo para o arquivo CSV a ser importado.')

    def handle(self, *args, **kwargs):
        """
        A lógica principal do comando de importação.
        """
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
                        # Processa o campo 'team_colour' para garantir que tenha '#' no início
                        team_colour_value = row.get('team_colour')
                        team_colour_value = '#' + team_colour_value

                        # O método update_or_create é perfeito para a sua regra 'unique_together'.
                        # Ele usará 'full_name' e 'session_key' para buscar um registro existente.
                        obj, created = driver.objects.update_or_create(
                            full_name=row['full_name'],
                            session_key=row['session_key'],
                            # O dicionário 'defaults' contém os campos que serão atualizados
                            # ou usados para criar o novo registro.
                            defaults={
                                'broadcast_name': row.get('broadcast_name'),
                                'driver_number': row.get('driver_number'),
                                'first_name': row.get('first_name'),
                                'last_name': row.get('last_name'),
                                'meeting_key': row.get('meeting_key'),
                                'team_colour': team_colour_value, # Usa o valor processado
                                'team_name': row.get('team_name'),
                                'country_code': row.get('country_code'),
                                'headshot_url': row.get('headshot_url'),
                                'name_acronym': row.get('name_acronym'),
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

