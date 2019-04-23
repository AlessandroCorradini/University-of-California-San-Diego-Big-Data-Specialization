#!/usr/bin/python

import json
import sys
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

class TweetStreamListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        if "created_at" in tweet:
            print tweet["created_at"][4:-10] + " " + tweet["text"][:70] + "\n"
        return True
    
    def on_error(self, status):
        print status

auth = []
f = open("auth", "r")
for line in f:
    auth.append(line.strip())
f.close()

try:
    listener = TweetStreamListener()
    auth_key = OAuthHandler(auth[0], auth[1])
    auth_key.set_access_token(auth[2], auth[3])
    live_twitter_stream = Stream(auth_key, listener)
    live_twitter_stream.filter(track=[sys.argv[1]])
except KeyboardInterrupt, e:
    sys.exit()
