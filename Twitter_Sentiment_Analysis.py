import tweepy
from textblob import TextBlob

consumer_key = '1Zhm0krQV7hiP1fWnyYH5IZlx'
consumer_secret = 'Pkyj4LbbNH4r2B9NJgWo1xFIbLv7nsCcJr6X18RwhqtfCIGj3N'

access_token = '979802802364051456-Oo2zhibedp4EeBtzupxf7XBVeAM45br'
access_token_secret = '3VrSDugBiQv1gV6a9mdFieSrEPRzijCOGcLlH10MOV5HI'

auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

bitcoin_tweets = api.search('bitcoin')

for tweet in bitcoin_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)