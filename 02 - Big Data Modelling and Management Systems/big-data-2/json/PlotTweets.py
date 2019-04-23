#!/usr/bin/python

import json
import matplotlib.pyplot as plt
import sys
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

class TweetStreamListener(StreamListener):

    def __init__(self):
        
        self.max_sec = 30

        fig = plt.figure()
        self.ax = fig.add_subplot(111)
        self.ax.set_autoscalex_on(False)
        self.ax.set_xlim(0, self.max_sec)
        self.ax.set_autoscaley_on(True)
        #self.ax.set_ylim(minVal,maxVal)

        plt.xlabel('Seconds')
        plt.ylabel('Count')
        fig.show()

        self.x = []
        self.y = []

        self.count = 0
        self.last_ts = "0"


    def on_data(self, data):
        tweet = json.loads(data)
        if "created_at" in tweet:
            ts = tweet["created_at"][11:-11]
            if ts == self.last_ts:
              self.count = self.count + 1
            else:
                #print(self.count)
                
                self.x.append(len(self.x))
                self.y.append(self.count)
                lines = plt.plot(self.x,self.y)
                plt.setp(lines,color='b')
                plt.draw()

                self.count = 1
                self.last_ts = ts

                if len(self.x) > self.max_sec:
                    return False

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
    raw_input("Press <enter> to quit.")
except KeyboardInterrupt, e:
    sys.exit()
