'''
Created on Dec 4, 2015

@author: timothybeal
'''
#Thanks to @TheHigherDead
#This initial stab at kjvbot.py generates biblical mashups as sequences of randomly selected formal elements from the prophets and Psalms and tweets them to @kjvbot.

import random
import tweepy

auth = tweepy.OAuthHandler('000', '000')
auth.set_access_token('000', '000')
api = tweepy.API(auth)

words1 = ['And God said,', 'After these things,', 'Lo,', 'A voice cries out,', 'But behold,', 'Truly I tell you,', 'Thus saith the LORD:', 'And it will come to pass,', 'And the LORD said,', 'After these things,', 'And he said,', 'And she said,', 'Therefore,', 'Give ear to my words:', 'For, lo,', 'Behold,', 'The fool hath said in his heart,', 'And it shall come to pass,', 'For, behold,', 'And in that day,', 'And now,', 'Therefore,', 'And in that day thou shalt say,', 'Therefore said I,', 'Then answered I,', 'Because of this,', 'And I answered again,']
words2 = ['in due season,', 'with a mighty hand,', 'with outstretched arm,', 'with a shout,', 'in time to come,', 'before the sun goes down,', 'with a rod,', 'by the sword,', 'with shouts of joy,', 'with great gladness,', 'by his name,']
words3 = ['I', 'he', 'she','the LORD of hosts', 'God', 'Abraham', 'Moses', 'the man', 'the lion', 'the lamb', 'the serpant', 'the woman', 'the angel of the LORD', 'the land', 'my people', 'my children', 'the nations', 'this land', 'Zion', 'Samaria', 'Judah', 'the hand of the LORD', 'the LORD', 'the LORD God', 'LORD of hosts', 'man', 'Israel', 'the people', 'the king',  'the son', 'men',  'women', 'the house', 'children', 'the land', 'these things', 'my hand', 'the earth', 'Jerusalem', 'the city', 'the father', 'the mother', 'the daughter', 'the shepherd', 'the name,' 'the heart', 'the day', 'that place', 'that day', 'time', 'Judah', 'the word',  'evil', 'heaven', 'brethren', 'words', 'fire', 'this thing', 'the law', 'fathers', 'life', 'hands', 'eyes', 'fear', 'a voice', 'the priest',  'the spirit', 'servants', 'the soul', 'the servant', 'the glory', 'peace', 'gold', 'your mouth', 'death', 'priests', 'cities', 'the sword', 'sin', 'the face', 'water', 'the sea', 'work', 'blood', 'your wife', 'flesh', 'the woman', 'the brother', 'the end', 'the kingdom', 'the nations', 'power', 'sight', 'the altar', 'kings', 'enemies', 'the congregation', 'bread', 'night', 'silver', 'the world', 'wisdom', 'judgment', 'the multitude', 'love', 'the wilderness', 'the covenant', 'the tabernacle', 'the temple', 'righteousness', 'holiness']
words4 = ['will']
words5 = ['bring forth', 'kill', 'annihilate', 'know', 'take', 'put an end to', 'lie with', 'smite', 'give over', 'love', 'deliver', 'hear', 'see', 'choose', 'build', 'inherit', 'establish', 'find', 'seek', 'understand', 'judge', 'defile', 'fear', 'deliver', 'save', 'raise', 'pursue', 'make', 'send', 'fight', 'feed', 'save', 'write', 'destroy']
words6 = ['my', 'his', 'her', 'your', 'our', 'the']
words7 = ['god', 'God', 'gods', 'man', 'people', 'king', 'son', 'men',  'women', 'house', 'children', 'hands', 'land', 'things', 'hand', 'earth', 'sons', 'city', 'father', 'mother', 'daughter', 'name', 'heart', 'days', 'place', 'time', 'word',  'evil', 'heaven', 'brethren', 'words', 'fire', 'thing', 'law', 'fathers', 'life', 'eyes', 'fear', 'voice', 'priest',  'spirit', 'servants', 'soul', 'servant', 'glory', 'peace', 'gold', 'mouth', 'death', 'priests', 'cities', 'sword', 'weapons', 'sheep', 'sin', 'face', 'water', 'sea', 'work', 'blood', 'wife', 'flesh', 'woman', 'brother', 'head', 'year', 'end', 'kingdom', 'nations', 'power', 'sight', 'altar', 'kings', 'enemies', 'congregation', 'bread', 'night', 'silver', 'world', 'wisdom', 'judgment', 'multitude', 'love', 'wilderness', 'covenant', 'tabernacle', 'temple', 'righteousness', 'holiness']
words8 = ['(Hezekiah 8:3)', '(Hezekiah 1:3)', '(Elisha 6:8)', '(Elisha 2:4)','(Elisha 16:5)','(Elisha 1:3)', '(Ahaz 12:1)', '(Ahaz 9:8)','(Ahaz 15:1)','(Ahaz 3:6)','(Ahaz 3:16)','(Ahaz 2:4)', '(Jonadab 1:10)', '(Jonadab 1:10)','(Jonadab 1:10)','(Jonadab 10:1)','(Jonadab 11:3)','(Jonadab 61:9)','(Jonadab 3:16)','(Hannah 33:2)', '(Hannah 33:2)','(Hannah 33:2)','(Hannah 3:16)','(Hannah 13:12)','(Elijah 2:6)', '(Elijah 2:6)', '(Elijah 6:8)', '(Elijah 1:6)', '(Elijah 2:6)', '(Elijah 3:16)', '(Joash 15:30)', '(Joash 15:30)', '(Joash 15:30)', '(Joash 5:3)', '(Joash 1:32)', '(Joash 3:16)', '(Joash 1:1)', '(1 Saul 4:7)', '(1 Saul 3:16)', '(2 Saul 4:3)', '(1 Saul 22:3)', '(2 Saul 5:7)', '(1 Saul 12:8)', '(2 Saul 2:9)', '(2 Saul 20:1)', '(3 Lamentations 3:9)', '(4 Lamentations 11:3)', '(3 Lamentations 10:4)', '(2 Lamentations 16:16)', '(2 Lamentations 12:8)', '(3 Lamentations 3:16)', '(4 Lamentations 2:1)', '(3 Lamentations 4:7)']

word1 = random.choice(words1)
word2 = random.choice(words2)
word3 = random.choice(words3)
word4 = random.choice(words4)
word5 = random.choice(words5)
word6 = random.choice(words6)
word7 = random.choice(words7)
word8 = random.choice(words8)

kjvbot = '"' + word1 + ' ' + word2 + ' ' + word3 + ' ' + word4 + ' ' + word5 + ' ' + word6 + ' ' + word7 + '."  ' + word8

api.update_status(kjvbot)
    
print(kjvbot)
print(len(kjvbot))

