'''
Created on Mar 10, 2016

@author: timothybeal and textpotential

Anybot.py generates and tweets utterances as Markov chains based on 
a user-given three-word start phrase and a specified fileid.

'''

import markovbot
from random import choice

# enter your own three-word start phrase and fileid (example provided starts with "In the beginning" in the KJV Bible)
utterance = markovbot.markovize("In", "the", "beginning", "kjv.txt", char_limit=130)
tweet = '"' + utterance + '"'
tweet_len = len(tweet)

# enter your twitter api keys and secrets (get these for your account at apps.twitter.com)
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = '' 

# call function to print and (if less than 130 characters) tweet utterance    
print(tweet, '\n', tweet_len)
markovbot.post_tweet(consumer_key, consumer_secret, access_key, access_secret, tweet)
