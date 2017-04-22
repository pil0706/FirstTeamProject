#-*- coding: utf-8 -*-
from tweepy import StreamListener
from tweepy import Stream
import tweepy
import sys
import jsonpickle
import datetime
import os

consumer_key = 'TcSyTjO8ycNRXWUIxxP0rbBFG'
consumer_secret = 'm6uNwnPkMwJkMqWwB4DPqRNlpmfdnEHyJcgiQUsI0tYjpiHaBi'
access_token = '142620900-cOv68WHjBU6WPxPRTGVcxbIaICeSweNGnsxgDNXR'
access_secret = 'QBrzkiCDx8auR5CtjcB8KYdsqnwUXrDFB5LGi51pjgpRQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Problem connecting to API")
    sys.exit(-1)

#start

searchQuery = "문재인 or 홍준표 or 안철수 or 유승민 or 심상정"
maxTweets = 500 #10000000 Max
tweetsPerQry = 100 #100 Max
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
fName = 'tweets' + timestamp  +'.json'

# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))







