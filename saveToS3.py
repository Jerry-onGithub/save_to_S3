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


name="1234"+".csv"  #name of your file
s3 = boto3.resource('s3', aws_access_key_id="", aws_secret_access_key= "")  #set your aws_access_key_id and aws_secret_access_key
bucket = ''     #your bucket name
client = boto3.client("s3", aws_access_key_id="", aws_secret_access_key= "")    #set your aws_access_key_id and aws_secret_access_key

#save file function
def saveFile():
    data=[[1, 1, 1]]     #set this to your data
    df = pd.DataFrame(data, columns=['a', 'b', 'c'])    #can change this your column values
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    
    #s3.Object(bucket, name).put(Body=csv_buffer.getvalue())
    s3.upload_file('/tmp/' + name, bucket, 'orders_csv/{}'.format(name))    #change 'orders_csv' to the name of your path location


#check if file already exists 
def check():
    file='604873.csv'   #name of file to be checked
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

#if you want to delete file, you can use this function
def delete(key): 
    s3.Object(bucket, key).delete()
    
#upload an image
def uploadImage():
    filename='user_photo.jpg'   #name of image to be uploaded
    try:
        response = client.upload_file('C:/Users/.../.../user_photo.jpg', bucket, 'orders_images/user_photo.jpg')    #change the local path and S3 path according to your own
    
    except ClientError as e:
        logging.error(e)
        return False
    return True

uploadImage()
#delete('orders_csv/user_photo.jpg')
       
