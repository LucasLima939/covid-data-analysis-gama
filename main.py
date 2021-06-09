from service.sql_server_service import SQLServerService
from repositories.covid_repository import CovidRepository
from service.s3_service import S3Service
from datetime import datetime
from datetime import timedelta

def main():
    
    repository = CovidRepository()
    #countriesSlugs = repository.get_all_countries()
    #repository.get_all_countries_covid_infos(countriesSlugs)
    #service = SQLServerService()
    
    #countries_list = ['{"Country": "Japan", "CountryCode": "JP", "Lat": "36.2", "Lon": "138.25"}', '{"Country": "Cambodia", "CountryCode": "KH", "Lat": "12.57", "Lon": "104.99"}', '{"Country": "Cyprus", "CountryCode": "CY", "Lat": "35.13", "Lon": "33.43"}', '{"Country": "Moldova", "CountryCode": "MD", "Lat": "47.41", "Lon": "28.37"}']
    #s3_service = S3Service()
    #success = s3_service.upload_object(countries_list)
    #print(success)

    date = datetime(2020,1,1,1,1,1)
    i=0
    while i < 6:
        date += timedelta(days=7)
        print(date.strftime("%Y-%m-%dT%H:%M:%SZ"))
        i += 1

main()


    