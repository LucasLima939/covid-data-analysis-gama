from service.sql_server_service import SQLServerService
from repositories.covid_repository import CovidRepository

def main():
    
    repository = CovidRepository()
    repository.getAllCountries()
    #service = SQLServerService()
    

main()


    