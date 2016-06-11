"""
Created on Mar 10, 2016

@author: timothybeal and textpotential

The functions used to create a markov chain utterance and tweet, if desired.
Requires tweepy.

Example:
>>> from markovbot import Markovizer
>>> markovizer = Markovizer('/Users/jbarber/kjv.txt')
>>> markovizer.create_utterance('In the beginning')  # three-word string
'In the beginning of his way shall save a soul from death : I pray God '
'that it be read also in the prophets of Israel, and he will smite her '
'power in the ram to stand before thee all the commandments of the LORD, '
'I pray thee, let us straitly threaten them, that they may not pass away '
'from me : that which thou sowest, thou sowest not that body that shall '
'be, if he say unto thee, thou shalt sleep with thy fathers ; even '
'the king spake and said unto them, Your blood be glory for ever and '
'ever.'
>>> markovizer.create_utterance('Who told thee that')  # four-word string
'Who told thee that thou wast as one of them, and said, Tell him, '
'and said, My father and my brethren, and their flocks, and their herds, '
'and all that he did in Egypt, And all that he did, behold, they are '
'written among the sayings of the seers.'
>>> markovizer.create_utterance('Who told thee that', char_limit=140)
'Who told thee that thou wast naked and bare.'
>>> markovizer.utterance
'Who told thee that thou wast naked and bare.'
"""

from collections import defaultdict
from itertools import tee
from random import choice
import re
from nltk.tokenize import sent_tokenize
import tweepy


def nwise(iterable, n=2):
    """nwise([1, 2, 3, 4], n=3) => [(1, 2, 3), (2, 3, 4)]"""
    if len(iterable) < n:
        return
    iterables = tee(iterable, n)
    for i, iter_ in enumerate(iterables):
        for num in range(i):
            next(iter_)
    return zip(*iterables)


class Markovizer(object):
    """
    Creates a markov chain sentence from a given text.

    Parameters
    ----------
    input : string, '' is default.
        If input is a file path, the text to train the markovizer will
        be drawn from that file.

        Otherwise the input is expected to be a text string that
        that markovizer will use to construct the probability
        distribution.

    encoding : string, 'utf-8' is default.
        The encoding will be the encoding used to open the file,
        if input is a file path.

    token_pattern : raw string
        The pattern to use to find the tokens in the intial sentence.
    """
    def __init__(self, text, encoding='utf-8',
                 token_pattern=r'\w+|[^\w\s]'):
        try:
            with open(text, encoding=encoding) as f:
                self.text = f.read()
        except FileNotFoundError:
            self.text = text
        self.token_pattern = token_pattern
        self.prob_dist = None
        self.utterance = None
        # new seed lengths need to rerun create_prob_dist
        self.seed_lengths = set()

    def _build_sentence(self, seed):
        """
        Constructs a markov chain sentence from the probability
        distribution.
    
        Parameters
        ----------
        seed : list
            The words that will start the sentence.
        """
        token = ''
        tokens = seed[:]  # copy seed list
        seed_length = len(seed)
        if not self.prob_dist or seed_length not in self.seed_lengths:
            self.create_prob_dist(current_state_len=len(seed))
            self.seed_lengths.add(seed_length)

        while token not in set('.?!'):
            last_tokens = tuple(tokens[-seed_length:])
            new_token = choice(self.prob_dist[last_tokens])
            tokens.append(new_token)
            token = new_token
        
        sentence = ' '.join(tokens)
        sentence = re.sub(r'\s+([.,?!])',r'\1', sentence)

        return sentence
    
    def create_prob_dist(self, current_state_len=3):
        """
        Convert a text file into a dictionary of current-state keys and
        possible next-state values. (Not *technically* a probability
        distribution.)
    
        {(word1, word2, word3, ...): [next1, next2, ...], ...}
    
        Parameters
        ----------
        current_state_len : integer, 3 by default.
            The number of tokens to be used for the current state. Must
            be >= 1.
        """
        sentences = sent_tokenize(self.text)
        state_nexts = defaultdict(list)
        for sentence in sentences:
            tokens = re.findall(self.token_pattern, sentence)
            nwise_ = nwise(tokens, n=current_state_len + 1)
            if nwise_:
                for tokens in nwise_:
                    curr_state = tuple(tokens[:-1])
                    next_state = tokens[-1]
                    state_nexts[curr_state].append(next_state)

        self.prob_dist = state_nexts
    
    def create_utterance(self, sent_start, char_limit=None):
        """
        Create a markov chain from a sentence start using
        a given probability distribution and returning the chain
        as a string.
    
        Parameters
        ----------
        sent_start : string
            A string of one or more words that occurs in the the original
            text.
    
        char_limit : integer, None by default.
            If None, do not use a character limit.
    
            Otherwise, do not return a markov string unless the total number
            of characters is <= this character limit.
        """
        too_long = True
        
        while too_long:
            sentence = re.findall(self.token_pattern, sent_start)
        
            utterance = self._build_sentence(sentence)
            len_utterance = len(utterance)
             
            if char_limit != None and len_utterance > char_limit:
                too_long = True
            else:
                too_long = False

        self.utterance = utterance
        return utterance
             
    def post_tweet(self, consumer_key, consumer_secret, access_key,
                   access_secret):
        """
        Post the current utterance via tweepy.
    
        Parameters
        ----------
        consumer_key : string
            The consumer key for the twitter api.
    
        consumer_secret : string
            The consumer secret for the twitter api.
    
        access_key : string
            The access key for the twitter api.

        access_secret : string
            The access secret for the twitter api.
        """
        if not self.utterance:
            raise Exception('You need to create an utterance first!')
        elif len(self.utterance) > 140:
            raise Exception('Your utterance is too long to tweet!')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth) 
        api.update_status(self.utterance)
