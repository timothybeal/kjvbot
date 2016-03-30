'''
Created on Mar 10, 2016

@author: timothybeal

Initiated by a randomly selected three-word starting phrase, 
this kjvbot.py builds its utterance as a Markov chain based on a selection 
from the KJV Bible (the prophets, Gospels, Pauline letters, or Revelation) and then, 
if it is <= 135 characters, tweets it to @kjvbot.

'''

import kjvbot3
from random import choice

w = ["the", "them", "thee", "him"]
l = ["looked", "saw", "beheld", "heard", "turned"]
x = [["Woe", "unto", choice(w), "kjv_prophets.txt"], 
     ["And", "the", "priest", "kjv.txt"], 
     ["And", "I", choice(l), "kjv_revelation.txt"], 
     ["Behold", ",", "I", "kjv_revelation.txt"], 
     ["And", "to", "the", "kjv_revelation.txt"], 
     ["The", "kingdom", "of", "kjv_gospels.txt"], 
     ["Paul", ",", "a", "kjv_paul.txt"]] 

[word1, word2, word3, fileid] = choice(x)

# we can add hashtag for regional meeting
utterance = kjvbot3.markovize(word1, word2, word3, fileid, char_limit=138)
tweet = '"' + utterance + '"'
tweet_len = len(tweet)

# twitter api keys and secrets, you can get these for your account at apps.twitter.com
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = '' 

# call function to tweet utterance    
print(tweet, '\n', tweet_len)
# kjvbot3.post_tweet(consumer_key, consumer_secret, access_key, access_secret, tweet)
