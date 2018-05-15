import tweepy
import textblob

import config

consumer_key = config.tw_consumer_key 
consumer_secret = config.tw_consumer_secret

access_token = config.tw_access_token
access_secret = config.tw_access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Tesla')

for tweet in public_tweets:
  print(tweet.text)
  analysis = textblob.TextBlob(tweet.text)
  print(analysis.sentiment)
  print("\n")
