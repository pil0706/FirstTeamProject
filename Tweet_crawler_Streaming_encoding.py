#-*- coding: cp949 -*-
import os
import sys
import jsonpickle
import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#reload(sys)
#sys.setdefaultencoding('utf8')
#sys.setdefaultencoding('cp949')


consumer_key = 'Nn27riqMonpUdKbcwnIcvNsMd'
consumer_secret = 'eeJckTn1C5yq6vCFxMoBbkjDOgh9ZMhQJtOpI5ogZgLfOuALGu'
access_token = '153467658-vYrO9QedH95zM92FA2VzrTVQ54QzKsA2w2GgH6Ph'
access_token_secret = 'qeJXZvay5uhKPS9E5aM2nMXqPBYxTyLDzYNk6X5qeutMt'

import pprint
class MyPrettyPrinter(pprint.PrettyPrinter):
	def format(self, _object, context, maxlevels, level):
		if isinstance(_object, unicode):
			return "'%s'" % _object.encode('utf8'), True, False
		elif isinstance(_object, str):
			_object = unicode(_object,'utf8')
			return "'%s'" % _object.encode('utf8'), True, False
		return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)

class StdOutListener(StreamListener):

    def on_data(self, data):
        #���� ���ڵ��κ� ��ģ�ɷ� �� �׽�Ʈ
        MyPrettyPrinter().pprint(data)
        print MyPrettyPrinter().pformat(data)


        #print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=[u'������', u'�ɻ���', u'��ö��'])