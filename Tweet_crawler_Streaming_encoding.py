#-*- coding: utf-8 -*-
import os
import sys
import jsonpickle
import tweepy
import json
import codecs

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#필 Tweet API
consumer_key = 'Nn27riqMonpUdKbcwnIcvNsMd'
consumer_secret = 'eeJckTn1C5yq6vCFxMoBbkjDOgh9ZMhQJtOpI5ogZgLfOuALGu'
access_token = '153467658-vYrO9QedH95zM92FA2VzrTVQ54QzKsA2w2GgH6Ph'
access_token_secret = 'qeJXZvay5uhKPS9E5aM2nMXqPBYxTyLDzYNk6X5qeutMt'

#이부분은 인코딩때문에 해봄.
import pprint
class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, _object, context, maxlevels, level):
        if isinstance(_object, unicode):
            return "'%s'" % _object.encode('utf8'), True, False
        elif isinstance(_object, str):
            _object = unicode(_object, 'utf8')
            return "'%s'" % _object.encode('utf8'), True, False
        return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)

class StdOutListener(StreamListener):
    def on_data(self, data):
        #여기 인코딩부분 고친걸로 함 테스트
        MyPrettyPrinter().pprint(data)
        print MyPrettyPrinter().pformat(data)

        #json 저장하는거 (multi line으로 나옴. multi line json to single line 으로 나중에 변환 필요)
        with open('Crawled_Data.json', 'a') as tf:
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
    stream.filter(track=[u'문재인', u'심상정', u'안철수', u'홍준표', u'유승민'])