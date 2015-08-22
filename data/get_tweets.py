import tweepy
import json
import codecs
import requests
import time

requests.packages.urllib3.disable_warnings()

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

save_folder = 'tweets/'

with open('twitter_accounts.json') as data_file:
    data = json.load(data_file)

data = data['results']['collection1']

for i in data:
    try:
        handle = i['property2']['text']
        handle = handle[handle.index("@") + 1:handle.rindex(")")]
        print handle
        tweets = tweepy.Cursor(api.user_timeline, screen_name=handle).items(500)
        for j in tweets:
            codecs.open(save_folder+handle, 'a', 'utf-8').write(j.text)
    except tweepy.TweepError as e:
        print e
        time.sleep(60*15)
        continue
    except StopIteration:
        break
