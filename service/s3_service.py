import boto3
from botocore.exceptions import ClientError
import logging
import json

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client('s3',
                            aws_access_key_id='AKIA2YDDKTIHRZHHPUDA',
                            aws_secret_access_key='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'
                            )


    def upload_object(self, file_name, bucket, object_name=None):
        if object_name is None:
            object_name = file_name

        try:
            response = self.s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False

        return True
    
    def upload_list_json(self, json_list):
       self.s3_client.Object('accmeprojeto', 'countries_list.json').put(Body=(bytes(json.dumps(json_list).encode('UTF-8'))))
        


    #upload_object('C:/Users/Franc/OneDrive/Documentos/Altiere/Accenture/texto2.txt', 'accmeprojeto')
