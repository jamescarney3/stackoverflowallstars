from twython import Twython
from requests import request
import json
import boto3

# ---- BEGIN GET CREDENTIALS ----
s3 = boto3.client('s3')
credentials = json.load(s3.get_object(Bucket='stackoverflowallstars', Key='credentials.json')['Body'])

APP_TOKEN = credentials.get('app_token')
APP_TOKEN_SECRET = credentials.get('app_token_secret')
ACCESS_TOKEN = credentials.get('access_token')
ACCESS_TOKEN_SECRET = credentials.get('access_token_secret')
# ---- END GET CREDENTIALS ----

twitter = Twython(APP_TOKEN, APP_TOKEN_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)





# try:
#     img_path = ''
#     img = open(img_path)
#     img_response = twitter.upload_media(media=img)
#     twitter.update_status(media_ids[img_response['media_id']])
# except:
#     print('something went wrong')

twitter.update_status(status='another test from the app')
