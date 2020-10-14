import tweepy #to use Twitter's API
from textblob import TextBlob #for performing sentimental analysis
import re # to clean our tweets
import pandas as pd
import numpy as np

# twitter API creds
consumer_key = 'xx'
consumer_secret = 'xx'

access_token = 'xx'
access_token_secret = 'xx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Kenya")
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)