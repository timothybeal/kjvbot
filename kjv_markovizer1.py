'''
Created on Feb 23, 2016

@author: timothybeal
'''

#This simple module builds its utterance as a Markov chain based on a single starting word from the entire text of the KJV Bible.

import re
from nltk.tokenize import wordpunct_tokenize, sent_tokenize
from collections import defaultdict
from random import choice

with open(file="kjv.txt", encoding="UTF8") as kjv:
    kjv_text = kjv.read()
    
sentences = sent_tokenize(kjv_text)

token_nextwords = defaultdict(list)

for sentence in sentences:
    tokens = re.findall(r"\w+|[.]", sentence)
    previous = None
    for word in tokens:
        if not previous:
            previous = word
            continue
        else:
            token_nextwords[previous].append(word)
            previous = word   

present_word = "Behold"

print(present_word)

while present_word != ".":
    next_ = choice(token_nextwords[present_word])
    present_word = next_
    print(next_, end=" ")
