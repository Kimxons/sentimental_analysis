import tweepy #to use Twitter's API
from textblob import TextBlob #for performing sentimental analysis
import re # to clean our tweets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# twitter API creds
consumer_key = 'xx'
consumer_secret = 'xx'

access_token = 'xx'
access_token_secret = 'xx'

def twitter():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	return api

tweets = twitter()
search = tweets.user_timeline(screen_name="JKLive", count=200, lang="en")

print("20 tweets:\n")
for tweets in search[:20]:
	print(tweets.text + '\n')

df = pd.DataFrame([tweets.text for tweets in search], columns=["Tweets"])
df.head(20)

# clean the tweets -- TODO

df["Tweets"] = df["Tweets"].apply(clean_tweets)

polarity = lambda x: TextBlob(x).sentiment.polarity
subjectivity = lambda x: TextBlob(x).sentiment.subjectivity
df["polarity"] = df["Tweets"].apply(polarity)
df["subjectivity"] = df["Tweets"].apply(subjectivity)

plt.title("Sentiment Analysis", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()