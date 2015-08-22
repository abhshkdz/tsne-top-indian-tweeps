import tweepy
import json
import urllib

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

with open('twitter_accounts.json') as data_file:
    data = json.load(data_file)

data = data['results']['collection1']

for i in data:
    handle = i['property2']['text']
    handle = handle[handle.index("@") + 1:handle.rindex(")")]

    print handle

    user = api.get_user(screen_name = handle)
    urllib.urlretrieve(user.profile_image_url, 'images/'+handle)
