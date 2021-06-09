import boto3
from botocore.exceptions import ClientError
import logging
import json

class S3Service:
    def __init__(self):
        self.s3 = boto3.resource('s3',
        region_name='us-east-1',
        aws_access_key_id='',
        aws_secret_access_key='')


    def upload_object(self, json_list, object_name):
        

        try:
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
