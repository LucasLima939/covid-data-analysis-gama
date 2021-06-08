import boto3
from botocore.exceptions import ClientError
import logging

s3_client = boto3.client('s3',
                         aws_access_key_id='Seu id no IAM da AWS',
                         aws_secret_access_key='Senha de acesso seguro do IAM AWS'
                         )


def upload_object(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True


upload_object('C:/Users/Franc/OneDrive/Documentos/Altiere/Accenture/texto2.txt', 'accmeprojeto')
