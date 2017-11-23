import tweepy
import nltk
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#set access token and secret

auth.set_access_token(access_token, access_token_secret)

# creating api object
api = tweepy.API(auth)

tweets = api.home_timeline()
for tweet in tweets:
    print tweet.created_at, tweet.text
    tokens = nltk.word_tokenize(tweet.text)
    for token in tokens:
        print token
