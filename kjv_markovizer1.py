'''
Created on Feb 23, 2016

@author: timothybeal and his mom

This simple module builds its utterance as a Markov chain based on a 
single starting word from the entire text of the KJV Bible.

'''

import re
from nltk.tokenize import sent_tokenize
from collections import defaultdict
from random import choice

with open(file="kjv.txt", encoding="UTF8") as kjv:
    kjv_text = kjv.read()
    
sentences = sent_tokenize(kjv_text)

# create an empty dictionary with list as the default value type.
token_nextwords = defaultdict(list)

for sentence in sentences:
    # use re to word tokenize each sentence, making each word or period a token.
    tokens = re.findall(r"\w+|[.]", sentence)
    previous = None
    for word in tokens:
        if not previous:
            previous = word
            continue
        else:
            # build dictionary with each word as a key and value as list of all words that 
            # immediately follow it in the text
            token_nextwords[previous].append(word)
            previous = word   

# Define starting word
present_word = "Behold"

print(present_word)

# until a period is selected, randomly choose a word to follow each word
# from the list keyed to each word in the dictionary and 
# string them together with spaces
while present_word != ".":
    next_ = choice(token_nextwords[present_word])
    present_word = next_
    print(next_, end=" ")
