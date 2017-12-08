import tweepy
# import nltk
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib
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
pos_count = 0
neg_count =1

tweets = api.home_timeline(count=50)
for tweet in tweets:
    print (tweet.created_at, tweet.text)
    # tokens = nltk.word_tokenize(tweet.text)
    # for token in tokens:
    #     print token
    # frequency = nltk.FreqDist(tweet.text)
    # frequency.plot()
    opinion = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
    print (opinion.sentiment)
    if opinion.sentiment.classification == 'pos':
        pos_count += 1
    else:
        neg_count +=1

print('Postive Tweets:', pos_count)
print('Negative Tweets:', neg_count)

if(pos_count>neg_count):
    print('Your Timeline is Happy')
elif(neg_count>pos_count):
    print('Your Timeline is not happy')
else:
    print('Your Timeline is neutral')


