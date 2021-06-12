from service.sql_server_service import SQLServerService
from repositories.covid_repository import CovidRepository
from service.s3_service import S3Service
from datetime import datetime
from datetime import timedelta
import json 
from sqlalchemy import create_engine
import pandas as pd

def select_option_message():
    print('Selecione a opção desejada para consultas no nosso banco:')
    print('1 - Panorama diário de quantidade de casos confirmados de COVID-19 para o país com maior número de casos.')
    print('2 - Panorama diário de quantidade de mortes de COVID-19 do país com maior número de mortes.')
    print('3 - Total de mortes por COVID-19 dos 10 países do mundo com maiores números de mortos.')
    print('4 - Total de casos confirmados por COVID-19 dos 10 países do mundo com maiores números de casos.')
    print('5 - EXTRA: Total de RECUPERADOS da COVID-19 dos 10 países do mundo com maiores números de recuperados.')
    print('6 - sair')

def continue_or_exit_message():
    print('Você deseja continuar as consultas ou sair?')
    print('1 - continuar')
    print('2 - sair')

def accme_cli():
    print('Bem Vindo(a) ao repositório de dados da Accme para o Covid-19')
    sql_service = SQLServerService()
    opcao_selecionada = None
    while opcao_selecionada != 6:
        select_option_message()
        try:
            opcao_selecionada = int(input())
        except Exception as e:
            print('Digite um número')
        if opcao_selecionada in range(1, 6):
            sql = data_info_query(opcao_selecionada)
            sql_service.read_data(sql)
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
            if opcao_selecionada != 6:
                print("Opção Inválida")
    exit_message()

def exit_message():
    print('Obrigado por utilizar nosso sistema, volte sempre!')

def data_info_query(opcao_selecionada):
    
    if(opcao_selecionada == 1):
        print('opção 1 selecionada')
        return """
        select pais.Country, casos.CountryCode, Max(casos.Confirmed) Confirmed, Date
        from tb_cases as casos
        inner join tb_countries as pais on casos.CountryCode = pais.CountryCode 
        where casos.CountryCode =
        (select CountryCode from (select CountryCode, max(Confirmed) Confirmed from tb_cases group by CountryCode order by Confirmed desc Limit 1)  tabela)
        group by casos.CountryCode, casos.Date 
        order by casos.Date desc
        limit 500
        """
    elif(opcao_selecionada == 2):
        print('opção 2 selecionada')
        return """
        select pais.Country, casos.CountryCode, Max(casos.Deaths) Deaths, Date
        from tb_cases as casos
        inner join tb_countries as pais on casos.CountryCode = pais.CountryCode 
        where casos.CountryCode =
        (select CountryCode from (select CountryCode, max(Deaths) Deaths from tb_cases group by CountryCode order by Deaths desc Limit 1)  tabela)
        group by casos.CountryCode, casos.Date 
        order by casos.Date desc
        limit 500
        """
    elif(opcao_selecionada == 3):
        print('opção 3 selecionada')
        return """
        select pais.Country, casos.CountryCode, Deaths from (select CountryCode, max(Deaths) Deaths from tb_cases group by CountryCode order by Deaths desc) as casos
        inner join tb_countries as pais on casos.CountryCode = pais.CountryCode 
        limit 10;
        """
    elif(opcao_selecionada == 4):
        print('opção 4 selecionada')
        return """
        select pais.Country, casos.CountryCode, Confirmed from (select CountryCode, max(Confirmed) Confirmed from tb_cases group by CountryCode order by Confirmed desc) as casos
        inner join tb_countries as pais on casos.CountryCode = pais.CountryCode 
        limit 10;
        """
    elif(opcao_selecionada == 5):
        print('opção 5 selecionada')
        return """
        select pais.Country, casos.CountryCode, Recovered from (select CountryCode, max(Recovered) Recovered from tb_cases group by CountryCode order by Recovered desc) as casos
        inner join tb_countries as pais on casos.CountryCode = pais.CountryCode 
        limit 10;
        """
    else:
        print('opção inválida')
        return ""


def create_and_write_table(filename, table_name):
    arquivo = open(filename)
    jsons = json.load(arquivo)
    json_lista = list(map(lambda x: json.loads(x), jsons))
    leitura = pd.DataFrame(json_lista)
    #print(leitura)
    print('creating rds engine')
    try:
        engine = create_engine('mysql+mysqlconnector://admin:accme159753@accme-database.c8fsb3usjei0.us-east-2.rds.amazonaws.com/accmedatabase')
    except Exception as e:
        print(e)

    leitura.to_sql(table_name, engine, if_exists='append', index=False)

def main():
    accme_cli()
    #1ª etapa: recuperar as listagem dos países
    #repository = CovidRepository()
    #countriesSlugs = repository.get_all_countries()

    #2ª etapa, separar e guardar no s3
    #repository.get_all_countries_covid_infos(countriesSlugs)
    
    #3ª etapa: recuperar os dados do s3
    #s3_service = S3Service()
    #s3_service.recover_json_file('countries_json.json')
    #print('countries data recovered')
    #s3_service.recover_json_file('covid_infos_json.json')
    #print('covid cases data recovered')

    #4ª etapa: upload dos arquivos no AWS RDS (Banco)
    #create_and_write_table('countries_json.json', 'tb_countries')
    #print('writing data to tb_countries')
    #create_and_write_table('covid_infos_json.json', 'tb_cases')
    #print('writing data to tb_cases')

main()


    