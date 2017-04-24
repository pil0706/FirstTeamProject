#-*- coding: utf-8 -*-
import os
import sys
import jsonpickle
import tweepy
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#필 Tweet API
consumer_key = 'Nn27riqMonpUdKbcwnIcvNsMd'
consumer_secret = 'eeJckTn1C5yq6vCFxMoBbkjDOgh9ZMhQJtOpI5ogZgLfOuALGu'
access_token = '153467658-vYrO9QedH95zM92FA2VzrTVQ54QzKsA2w2GgH6Ph'
access_token_secret = 'qeJXZvay5uhKPS9E5aM2nMXqPBYxTyLDzYNk6X5qeutMt'


class StdOutListener(StreamListener):
    def on_data(self, data):
        json_encoded = json.dumps(data)
        print json_encoded

        #json 저장하는거 (multi line으로 나옴. multi line json to single line 으로 나중에 변환 필요)
        with open('tweet_data.json', 'a') as tf:
            tf.write(data)
        return True

        #원래는 그냥 아래 코드 프린트 데이터 하면 되는데 인코딩 때문에 저렇게 함
        #print data
        #return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=[u'문재인', u'심상정', u'안철수',u'홍준표',u'유승민'])