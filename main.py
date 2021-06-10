from service.sql_server_service import SQLServerService
from repositories.covid_repository import CovidRepository
from service.s3_service import S3Service
from datetime import datetime
from datetime import timedelta

def select_option_message():
    print('Selecione a opção desejada para consultas no nosso banco:')
    print('1 - Panorama diário de quantidade de casos confirmados de COVID-19 para o país com maior número de casos.')
    print('2 - Panorama diário de quantidade de mortes de COVID-19 do país com maior número de mortes.')
    print('3 - Total de mortes por COVID-19 dos 10 países do mundo com maiores números de mortos.')
    print('4 - Total de casos confirmados por COVID-19 dos 10 países do mundo com maiores números de casos.')
    print('5 - sair')

def continue_or_exit_message():
    print('Você deseja continuar as consultas ou sair?')
    print('1 - continuar')
    print('2 - sair')

def accme_cli():
    print('Bem Vindo(a) ao repositório de dados da Accme para o Covid-19')
    opcao_selecionada = None
    while opcao_selecionada != 5:
        select_option_message()
        try:
            opcao_selecionada = int(input())
        except Exception as e:
            print('Digite um número')
        if opcao_selecionada in range(1, 5):
            show_data_info(opcao_selecionada)
            continuar_operacao = None
            while continuar_operacao not in range(1,3):
                continue_or_exit_message()
                try:
                    continuar_operacao = int(input())
                except Exception as e:
                    print('Digite um número')
                if continuar_operacao not in range(1,3):
                    print('Operação inválida')
            if(continuar_operacao == 2):
                break

        else:
            if opcao_selecionada != 5:
                print("Opção Inválida")
    exit_message()

def exit_message():
    print('Obrigado por utilizar nosso sistema, volte sempre!')

def show_data_info(opcao_selecionada):
    print('data_info')

def main():
    accme_cli()

    #repository = CovidRepository()
    #countriesSlugs = repository.get_all_countries()
    #repository.get_all_countries_covid_infos(countriesSlugs)
    
    #service = SQLServerService()
    
    #countries_list = ['{"Country": "Japan", "CountryCode": "JP", "Lat": "36.2", "Lon": "138.25"}', '{"Country": "Cambodia", "CountryCode": "KH", "Lat": "12.57", "Lon": "104.99"}', '{"Country": "Cyprus", "CountryCode": "CY", "Lat": "35.13", "Lon": "33.43"}', '{"Country": "Moldova", "CountryCode": "MD", "Lat": "47.41", "Lon": "28.37"}']
    #s3_service = S3Service()
    #success = s3_service.upload_object(countries_list, 'teste-lucas-lima.json')
    #print(success)

main()


    