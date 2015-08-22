import tweepy
import json
import urllib

auth = tweepy.OAuthHandler('r7vYBxN39T0awds0GN3tmlPNz', 'CiUw7Runi4WaWy7OG6pyu0vPHt1Z1qgzr0bnvZmAAZj6DWqTaH')
auth.set_access_token('84902368-HcIcBVcQSdRTeOdjmpKPJQsgP1Qxu1YBPzTyTRsTN', '7nkHvc5G5E9eEnMtfymw5zETdRaBWOdf3FFgDBPngpKmm')

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
