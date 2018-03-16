from twython import Twython
from requests import request
import json
import boto3

# ---- BEGIN GET CREDENTIALS ----
aws_credentials = json.load(open('credentials.json'))
AWS_ACCESS_KEY_ID = aws_credentials['aws_access_key_id']
AWS_ACCESS_SECRET_KEY = aws_credentials['aws_access_secret_key']

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_ACCESS_SECRET_KEY)

twitter_credentials = json.load(s3.get_object(Bucket='stackoverflowallstars', Key='credentials.json')['Body'])
APP_TOKEN = twitter_credentials.get('app_token')
APP_TOKEN_SECRET = twitter_credentials.get('app_token_secret')
ACCESS_TOKEN = twitter_credentials.get('access_token')
ACCESS_TOKEN_SECRET = twitter_credentials.get('access_token_secret')
# ---- END GET CREDENTIALS ----

twitter = Twython(APP_TOKEN, APP_TOKEN_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)





# try:
#     img_path = ''
#     img = open(img_path)
#     img_response = twitter.upload_media(media=img)
#     twitter.update_status(media_ids[img_response['media_id']])
# except:
#     print('something went wrong')

twitter.update_status(status='got the keys')
