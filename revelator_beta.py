'''
Created on Dec 10, 2015

@author: timothybeal
'''
#Thanks to @TheHigherDead
#Like the first version of kjvbot.py, revelator.py generates biblical mashups as sequences of randomly selected formal elements from the prophets and Psalms and tweets them to @kjvbot.


#needed for forming sentences by stringing randomly selected words/phrases from each POS list below
import random
#the thing that allows you to go into your Twitter api account and post to it
import tweepy
#enter your Twitter api authentication and access token
auth = tweepy.OAuthHandler('000', '000')
auth.set_access_token('000', '000')
#this is used later with the update_status function(?) to post a new status built from the POV lists below
api = tweepy.API(auth)
#make lists of KJV words and phrases grouped into lists of formal elements within a typical vision intro in Revelation
word1 = ['After this I looked,', 'And being turned, I saw,', 'And I saw,', 'Then there appeared a great wonder,', 'And I saw another sign,', 'And after that I looked,', 'And I saw heaven opened,', 'And when I looked,', 'Then I arose,', 'So I went in and saw,', 'Then I looked,', 'And when I looked,', 'And I turned to see,' ]
word2 = ['and, behold,', 'behold,', 'lo,', 'and, lo,',  ]
#humanoid subject(s) 
word3 = ['three foul spirits', 'one like the Son of Man', 'another angel', 'another mighty angel', 'the woman clothed with the sun', 'a great red dragon', 'Michael', 'the child', 'a great multitude', 'an eagle', 'the inhabitants of the earth', 'the dead', 'the prophets', 'the saints', 'the living one', 'Satan', 'the Spirit', 'a flying eagle', 'four living creatures', 'the second living creature', 'the third living creature', 'the fourth living creature', 'the Lamb', 'a white horse', 'a black horse', 'a voice of thunder','the rider','the angel standing in the sun','Death','the New Jerusalem','the holy city', 'the Almighty', 'the great day', 'pestilence', 'the bridegroom', 'the whore', 'the Lord of lords', 'the King of kings', 'a scarlet beast', 'Abaddon', 'the dragon', 'the face of death']
#ing intransitive verbs 
word4 = ['shining', 'coming', 'turning', 'singing', 'standing', 'ascending', 'rising', 'burning', 'rushing', 'crying out', 'flying', 'sitting', 'mourning', 'weeping']
#prepositions
word5 = ['in', 'above', 'beneath', 'over', 'upon', 'within', 'under', 'beside']
#places and plural objects 
word6 = ['the elders', 'Babylon', 'seven lampstands', 'the book of life', 'the water of life', 'their works', 'the first things', 'a voice from heaven','the plague', 'huge hailstones', 'the thirsty', 'the blood of the saints', 'the blood of the prophets', 'the Alpha and the Omega', 'the beginning and the end', 'the spring', 'Hades', 'blasphemous words', 'the morning star', 'the whole world', 'the great city', 'the smoke of her burning', 'the millstone', 'the bride', 'the magnates', 'the blood of prophets', 'her wealth', 'the merchants', 'your dainties', 'your splendor', 'the hail', 'their kingdom', 'his splendor', 'the cup full of abominations', 'the impurities of her fornication', 'the wilderness', 'harpists playing harps', 'mid-heaven', 'heaven', 'blasphemous names', 'the lake of fire', 'an eternal gospel', 'demonic spirits', 'the beast and its image', 'a sharp sickle', 'the temple', 'the harvest', 'Apollyon', 'the great river Euphrates', 'a rainbow', 'the moon', 'ten horns', 'seven heads', 'seven diadems', 'the nations', 'a rod of iron', 'pillars of fire', 'the sun', 'the earth', 'the four winds', 'the sea', 'the land', 'his trumpet', 'a great mountain', 'the ships', 'Hades', 'the waters', 'a cloud', 'the second woe', 'the third woe', 'Death and Hades', 'your nakedness', 'a sea of glass', 'the scroll', 'the throne', 'seven horns', 'seven eyes', 'golden bowls', 'a harp', 'incense', 'the blood', 'the elders', 'a white horse', 'a black horse', 'a voice of thunder', 'a crown', 'a pair of scales', 'the mountain', 'the island', 'seven bowls', 'smoke and sulpher']
#transitive action ing verbs 
word7 = ['reading', 'guarding', 'sending forth', 'holding', 'throwing', 'anointing', 'holding', 'blessing', 'judging', 'touching', 'following', 'wearing', 'watching']
#singular objects 
word8 = ['the book of life', 'the mouth of the dragon', 'the mouth of the beast', 'the false prophet', 'the spring', 'the morning star', 'the millstone', 'the bride', 'her wealth', 'your splendor', 'the hail', 'the wilderness', 'the woman', 'the number of the beast', 'the sound of many waters', 'the sound of loud thunder', 'an eternal gospel', 'the false prophet', 'the beast and its image', 'a sharp sickle', 'Apollyon', 'the beast', 'a great portent', 'the agony', 'his trumpet', 'the second woe', 'the third woe', 'your nakedness', 'an eagle', 'the scroll', 'a harp', 'incense', 'blood', 'a voice of thunder', 'a black horse', 'a white horse', 'a pair of scales', 'a golden crown']
#citations 
word9 = ['(Revelator 2:19)', '(Revelator 14:3)', '(Revelator 1:16)', '(Revelator 6:8)', '(Revelator 6:5)', '(Revelator 6:66)', '(Revelator 2:2)', '(Revelator 4:4)', '(Revelator 8:26)', '(Revelator 11:11)', '(Revelator 17:2)', '(Revelator 1:3)', '(Revelator 4:7)', '(Revelator 5:17)', '(Revelator 1:29)', '(Revelator 15:13)', '(Revelator 12:3)', '(Revelator 21:5)', '(Revelator 3:16)']
#make random selections      
word1 = random.choice(word1)
word2 = random.choice(word2)
word3 = random.choice(word3)
word4 = random.choice(word4)
word5 = random.choice(word5)
word6 = random.choice(word6)
word7 = random.choice(word7)
word8 = random.choice(word8)
word9 = random.choice(word9)
#put randomly selected elements into a quotation plus reference
revelator = '"' + word1 + ' ' + word2 + ' ' + word3 + ' ' + word4 + ' ' + word5 + ' ' + word6 + ', ' + word7 + ' ' + word8 + '."  '  + word9
#send new status to @KJVBot 
api.update_status(revelator)
#print what was sent and its character length (keeping under 144)    
print(revelator)
print(len(revelator))
