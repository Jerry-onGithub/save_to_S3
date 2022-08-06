# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 21:00:57 2022

@author: Jerry
"""


from io import StringIO # python3; python2: BytesIO 
import boto3
import pandas as pd
import botocore
import codecs
import csv
import io
import logging
from botocore.exceptions import ClientError
import os


name="1234"+".csv"
s3 = boto3.resource('s3', aws_access_key_id="AKIAW3S276MPSQLCK2NI", aws_secret_access_key= "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")
bucket = 'jbot' 
client = boto3.client("s3", aws_access_key_id="AKIAW3S276MPSQLCK2NI", aws_secret_access_key= "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")

def saveFile():
    data=[[1, 1, 1]]
    df = pd.DataFrame(data, columns=['a', 'b', 'c'])
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    
    #s3.Object(bucket, name).put(Body=csv_buffer.getvalue())
    s3.upload_file('/tmp/' + name, bucket, 'orders_csv/{}'.format(name))



def check():
    file='604873.csv'
    try:
        s3.Object(bucket, file).load()
        
        #obj = client.get_object(Bucket= bucket, Key= file) 
        # for row in csv.DictReader(codecs.getreader("utf-8")(obj["Body"])):
        #     print(row['Name'])
        
        # data = obj['Body'].read().decode('utf-8')
        # writer_buffer = io.StringIO()
        
        print("Exists")
        return True
    
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("Not exist")
            # The object does not exist.
            ...
        else:
            print("Something else has gone wrong.")
            # Something else has gone wrong.
            raise
        return False

def delete(key): 
    s3.Object(bucket, key).delete()
    
def uploadImage():
    filename='user_photo.jpg'
    try:
        response = client.upload_file('C:/Users/Jerry/Desktop/user_photo.jpg', bucket, 'orders_images/user_photo.jpg')
    
    except ClientError as e:
        logging.error(e)
        return False
    return True

uploadImage()
#delete('orders_csv/user_photo.jpg')
       