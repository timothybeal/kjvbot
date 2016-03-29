'''
Created on Mar 10, 2016

@author: timothybeal
'''

#Initiated by a randomly selected three-word starting phrase, this kjvbot.py builds its utterance as a Markov chain based on a selection from the KJV Bible (the prophets, Gospels, Pauline letters, or Revelation) and then, if it is <= 140 characters, tweets it to @kjvbot.

from collections import defaultdict
from itertools import tee
from random import choice
import random
import re
from nltk.tokenize import sent_tokenize
import tweepy

auth = tweepy.OAuthHandler('000', '000')
auth.set_access_token('000', '000')
api = tweepy.API(auth) 

def nwise(iterable, n=2):
        if len(iterable) < n:
            return
        iterables = tee(iterable, n)
        for i, iter_ in enumerate(iterables):
            for num in range(i):
                next(iter_)
        return zip(*iterables)

def kjvbot(word1, word2, word3, fileid):   
    w = ["the", "them", "thee", "him"]
    l = ["looked", "saw", "beheld", "heard", "turned"]
    x = [["Woe", "unto", random.choice(w), "kjv_prophets.txt"], ["And", "the", "priest", "kjv.txt"], ["And", "I", random.choice(l), "kjv_revelation.txt"], ["Behold", ",", "I", "kjv_revelation.txt"], ["And", "to", "the", "kjv_revelation.txt"], ["The", "kingdom", "of", "kjv_gospels.txt"], ["Paul", ",", "a", "kjv_paul.txt"]] 
    [word1, word2, word3, fileid] = random.choice(x)
      
    with open(fileid) as f:
        text = f.read()
    
    sentences = sent_tokenize(text)
    sent_tokens = defaultdict(list)
    for sentence in sentences:
        tokens = re.findall(r'\w+|[.,?!]', sentence)
        nwise_ = nwise(tokens, n=4)
        if nwise_:
            for token1, token2, token3, token4 in nwise_:
                sent_tokens[token1, token2, token3].append(token4)
    
    token = ''
    
    sentence = [word1, word2, word3]
    
    while token not in set('.?!'):
        last_tokens = tuple(sentence[-3:])
        new_token = choice(sent_tokens[last_tokens])
        sentence.append(new_token)
        token = new_token
    
    len(' '.join(sentence))
    
    spacey_tweet = ' '.join(sentence)
    spacey_tweet = spacey_tweet.replace(' .', '.')
    spacey_tweet = spacey_tweet.replace(' ,', ',')
    spacey_tweet = spacey_tweet.replace(' !', '!')
    spacey_tweet = spacey_tweet.replace(' ?', '?')
    tweet = '"' + spacey_tweet + '"'     
    
    if len(tweet) <= 140:
        print(tweet)
        print(len(tweet))
        api.update_status(tweet)
                    
    if len(tweet) > 140:
        kjvbot(word1, word2, word3, fileid)
            
kjvbot("word1", "word2", "word3", "fileid")
