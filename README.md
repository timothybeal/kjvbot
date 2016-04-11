# kjvbot
Repository of work in progress by Timothy Beal, Case Western Reserve University, and Michael Hemenway, Iliff School of Theology, with patient instruction and tremendous help from Justin Barber, and in collaboration with Micah Saxton and Pamela Eisenbaum. Our main focus so far has been kjvbot.py, a little markovian bot that autogenerates King James Version biblical sounding utterances and sends them as tweets to @KJVBot via Twitter's API.

We have now created a module, markovbot.py, that can be deployed to auto-generate and tweet utterances from any text based on any three-word start phrase.

Kjvbot3.py is an example of how the module markovbot.py could be used: it generates and tweets utterances to @KJVBot based on randomly selected three-word start phrases within particular sections of the KJV Bible (prophets, Gospels, Revelation, or the entire text).

Anybot.py provides a generic module that, working from markovbot.py, enables you to generate and tweet Markov chain utterances based on any three-word start phrase within any text.

The older markovizer programs were early attempts to generate Markov chains based on particular texts. They simply autogenerate and print utterances (no tweeting). Version 1 begins with a single start word and the whole KJV Bible, whereas version 2 begins with a three-word start phrase and a fileid specified by the user.

Kjvbot_beta.py is where we began. Built from the code behind @TheHigherDead, this module generates biblical mashups as sequences of randomly selected formal elements from the prophets and Psalms and then tweets them to @KJVBot.




