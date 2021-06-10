#Fazendo os imports necessarios para comunicar com a api da AWS S3
import boto3
from boto3 import s3
from botocore.exceptions import ClientError
import logging
import json
import os

#Classe para os serviços de uploads e downloads no S3
class S3Service:
    #metodo para fazer o upload 
    def upload_list_json(self, country_json):
        data = open('altiere.json', 'rb')
        s3 = boto3.resource('s3',
                           region_name='us-east-1',
                           aws_access_key_id='ID',
                           aws_secret_access_key='chave de segurança')

        s3.Bucket('accmeprojeto').put_object(Key=country_json, Body=data)

    #metodo para fazer o download e salvar no pc
    @staticmethod
    def download_list_json():
        s3 = boto3.resource('s3',
                            aws_access_key_id='ID',
                            aws_secret_access_key='chave de segurança')

                   #accmeprojeto -> nome do S3                 
                   #altiere.json -> nome do arquivo no S3
                   #froms3.json  -> nomre que vai salvar no pc
        s3.Bucket('accmeprojeto').download_file('altiere.json', os.path.join(os.getcwd(), 'fromS3.json'))
