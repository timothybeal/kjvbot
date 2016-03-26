'''
Created on Mar 10, 2016

@author: timothybeal

The functions used to create a markov chain and tweet if desired.
'''

from collections import defaultdict
from itertools import tee
from random import choice
import re
from nltk.tokenize import sent_tokenize
import tweepy

def nwise(iterable, n=2):
        if len(iterable) < n:
            return
        iterables = tee(iterable, n)
        for i, iter_ in enumerate(iterables):
            for num in range(i):
                next(iter_)
        return zip(*iterables)

def markovize(word1, word2, word3, fileid):   
    
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
    
    spacey_utterance = ' '.join(sentence)
    spacey_utterance = re.sub(r'\s+([.,!/])',r'\1', spacey_utterance)
     
    return spacey_utterance
            
def post_tweet(key,secret,tweet):

    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth) 
    api.update_status(tweet)
    