import boto3
from botocore.exceptions import ClientError
import logging
import json


class S3Service:
    data = open('teste.json', 'rb')
    s3 = boto3.resource('s3',
    region_name='us-east-1',
    aws_access_key_id=input(),
    aws_secret_access_key=input())

    s3.Bucket('accmeprojeto').put_object(Key='teste.json', Body=data)