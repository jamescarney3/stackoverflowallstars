from requests import request
import json
import os
import random

import boto3
from twython import Twython

queue_prefix = 'queue/'
archive_prefix = 'archive/'
bucket_id = 'stackoverflowallstars'

# ---- BEGIN GET CREDENTIALS ----
aws_credentials = json.load(open('credentials.json'))
AWS_ACCESS_KEY_ID = aws_credentials['aws_access_key_id']
AWS_ACCESS_SECRET_KEY = aws_credentials['aws_secret_access_key']

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_ACCESS_SECRET_KEY)

twitter_credentials = json.load(s3.get_object(Bucket=bucket_id, Key='credentials.json')['Body'])
APP_TOKEN = twitter_credentials.get('app_token')
APP_TOKEN_SECRET = twitter_credentials.get('app_token_secret')
ACCESS_TOKEN = twitter_credentials.get('access_token')
ACCESS_TOKEN_SECRET = twitter_credentials.get('access_token_secret')
# ---- END GET CREDENTIALS ----


# ---- MAKE TWYTHON CLIENT ----
twitter = Twython(APP_TOKEN, APP_TOKEN_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# ---- PICK A SCREENSHOT AND TWEET IT ----
queue_objects = s3.list_objects(Bucket=bucket_id, Prefix=queue_prefix).get('Contents')
queue_img_keys = sorted([obj['Key'] for obj in queue_objects if obj['Key'] != queue_prefix])

if len(queue_img_keys):
    img_key = queue_img_keys[0]
    local_file_name = '/tmp/{}'.format(os.path.basename(img_key))
    s3.download_file(bucket_id, img_key, local_file_name)

    try:
        img = open(local_file_name, 'rb')
        img_response = twitter.upload_media(media=img)
        twitter.update_status(media_ids=[img_response['media_id']])

        s3.upload_file(local_file_name, bucket_id, 'archive/{}'.format(os.path.basename(img_key)))
        s3.delete_object(Bucket=bucket_id, Key=img_key)
    except:
        print 'something went wrong'

else:
    archive_img_keys = sorted([obj['Key'] for obj in archive_objects if obj['Key'] != archive_prefix])

    img_key = random.choice(archive_img_keys)
    local_file_name = '/tmp/{}'.format(os.path.basename(img_key))
    s3.download_file(bucket_id, img_key, local_file_name)

    img = open(local_file_name, 'rb')
    img_response = twitter.upload_media(media=img)
    twitter.update_status(media_ids=[img_response['media_id']])
