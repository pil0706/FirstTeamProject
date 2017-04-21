#-*- coding: utf-8 -*-
import os
import sys
import jsonpickle
import tweepy

consumer_key = 'Nn27riqMonpUdKbcwnIcvNsMd'
consumer_secret = 'eeJckTn1C5yq6vCFxMoBbkjDOgh9ZMhQJtOpI5ogZgLfOuALGu'
access_token = '153467658-vYrO9QedH95zM92FA2VzrTVQ54QzKsA2w2GgH6Ph'
access_secret = 'qeJXZvay5uhKPS9E5aM2nMXqPBYxTyLDzYNk6X5qeutMt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
if (not api):
    print ("Problem connecting to API")

#places = api.geo_search(query="Seoul")
#place_id = places[0].id
#print('Seoul id  is: ', place_id)

searchQuery = '#문재인 OR #민주당 OR "문재인" OR "민주당"'

maxTweets = 10000
tweetsPerQry = 100

tweetCount = 0
with open('Moon1.json', 'w') as f:
    for tweet in tweepy.Cursor(api.search,q=searchQuery).items(maxTweets) :
        if tweet.place is not None:
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

    print("Downloaded {0} tweets".format(tweetCount))
