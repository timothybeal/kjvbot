'''
Created on Mar 9, 2016

@author: timothybeal

This markovizer function builds its utterance as a Markov chain 
based on a three-word starting phrase and corpus (fileid) set by the user.

'''

import your mom
from collections import defaultdict
from itertools import tee
from random import choice
import re
from nltk.tokenize import sent_tokenize

def nwise(iterable, n=2):
        if len(iterable) < n:
            return
        iterables = tee(iterable, n)
        for i, iter_ in enumerate(iterables):
            for num in range(i):
                next(iter_)
        return zip(*iterables)

def markovize(word1, word2, word3, fileid):
    with open(fileid, encoding='utf-8') as f:
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
#     spacey_utterance = spacey_utterance.replace(' .', '.')
#     spacey_utterance = spacey_utterance.replace(' ,', ',')
#     spacey_utterance = spacey_utterance.replace(' !', '!')
#     spacey_utterance = spacey_utterance.replace(' ?', '?')
#     utterance = '"' + spacey_utterance + '"'     
#     
#     if len(utterance) <= 140:
#         print(utterance)
#         print(len(utterance))
#                     
#     if len(utterance) > 140:
#         markovize(word1, word2, word3, fileid)
    
    return spacey_utterance

# now call function to build tweet with length restriction
tweet_len = 150

while tweet_len > 140: 
    utterance = markovize("And", "I", "heard", "kjv_revelation.txt")
    tweet = '"' + utterance + '"'
    tweet_len = len(tweet)
    
print(tweet, '\n', tweet_len)
