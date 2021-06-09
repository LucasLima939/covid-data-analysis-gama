from enum import unique
import covid_repository
import sql_server_service
import s3Service
import boto3

def main():
    #repository = covid_repository.CovidRepository()
    #countriesSlugs = repository.get_all_countries()
    #repository.get_all_countries_covid_infos(countriesSlugs)
    #sql_server_service.SQLServerService()

    #countries_list = ['{"Country": "Japan", "CountryCode": "JP", "Lat": "36.2", "Lon": "138.25"}', '{"Country": "Cambodia", "CountryCode": "KH", "Lat": "12.57", "Lon": "104.99"}', '{"Country": "Cyprus", "CountryCode": "CY", "Lat": "35.13", "Lon": "33.43"}', '{"Country": "Moldova", "CountryCode": "MD", "Lat": "47.41", "Lon": "28.37"}']
    #s3_service = s3Service.S3Service()
    #s3_service.upload_(countries_list)
    #s3_service.s3_client.upload_fileobj(open('teste.json',encoding='utf-8'), 'accmeprojeto', 'teste.json')

    #data = open('teste.json', 'rb')
    #s3 = boto3.resource('s3',
    #region_name='us-east-1',
    #aws_access_key_id='',
    #aws_secret_access_key='')

    #s3.Bucket('accmeprojeto').put_object(Key='teste.json', Body=data)


   
main()