import pyttsx3
engine = pyttsx3.init()

import pyjokes
joke = pyjokes.get_joke()

from datetime import datetime
time = datetime.now().hour

engine.say("Hey there! My name is jokingo, I'm a joke teller. What's your name?")
engine.runAndWait()
a = input("Hey there! My name is jokingo, I'm a joke teller. What's your name? ")

if a.lower() in ["no", "nah", "nope", "i don't wanna tell you my name", "no thanks", "i ain't telling you my name"] :
#We used [] lists here so the user can type all these inputs and they'll be treated the same. 
#we used .lower so that these inputs wont be case sensitive and work either way. 
#To tell the program to check list inputs we use "in" not ==
#In .lower() type everything in lower case so it'll case insensitive everything
 engine.say('''Ohh you dont wanna tell me ur name and still wanna hear a joke? \nHere's the joke : YOUR LIFE. Piss off now''')
 print('''Ohh you dont wanna tell me ur name and still wanna hear a joke? \nHere's the joke : YOUR LIFE. Piss off now''')
 engine.runAndWait()


elif 5 < time <= 12:
  engine.say(f"Good morning {a}! Here's a joke for you : {joke}")
  print(f"Good morning {a}! Here's a joke for you : {joke}")
  engine.runAndWait()

elif 12 < time <= 17:
  engine.say(f"Good afternoon {a}! Here's a joke for you : {joke}")
  print(f"Good afternoon {a}! Here's a joke for you : {joke}")
  engine.runAndWait()
  
elif 17 < time <= 22:
  engine.say(f"Good evening {a}! Here's a joke for you : {joke}")
  print(f"Good evening {a}! Here's a joke for you : {joke}")
  engine.runAndWait()
  
else :
 engine.say(f"Looks like you're a night owl {a}! Here's a joke for you : {joke}")
 print(f"Looks like you're a night owl {a}! Here's a joke for you : {joke}")
 engine.runAndWait()

print("What are you looking at, laugh now bwahaha.")
engine.say("What are you looking at, laugh now bwahaha.")
engine.runAndWait()