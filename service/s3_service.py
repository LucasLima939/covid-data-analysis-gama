import boto3
from botocore.exceptions import ClientError
import logging
import json
import os

class S3Service:
    def __init__(self):
        self.s3 = boto3.resource('s3',
        region_name='us-east-1',
        aws_access_key_id='AKIA2YDDKTIH4WTX2RNG',
        aws_secret_access_key='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')
        print('initialized s3 service')

    
    #metodo para fazer o download e salvar no pc
    def recover_json_file(self, object_name):
                    #accmeprojeto -> nome do S3                 
                    #object_name -> nome do arquivo no S3
                    #froms3.json  -> nomre que vai salvar no pc
                    #os.path.join(os.getcwd(), object_name) recupera o caminho do sistema
        try:
            self.s3.Bucket('accmeprojeto').download_file(object_name, os.path.join(os.getcwd(), object_name))
        except Exception as e:
            print(e)


    def upload_object(self, json_list, object_name):
        try:
            print('uploading object with name: ' + object_name)
            data = json.dumps(json_list)
            response = self.s3.Bucket('accmeprojeto').put_object(Key=object_name+'.json', Body=data)
            print(response)
            return True
        except ClientError as ce:
            logging.error(ce)
            return False
        except Exception as e:
            print(e)
            return False
