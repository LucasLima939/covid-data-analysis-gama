from service.sql_server_service import SQLServerService
from repositories.covid_repository import CovidRepository

def main():
    
    repository = CovidRepository()
    countriesSlugs = repository.get_all_countries()
    repository.get_all_countries_covid_infos(countriesSlugs)
    #service = SQLServerService()
    

main()


    