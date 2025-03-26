import requests 
import random

import speech_recognition as sr
import pyaudio
def tts(talk) :
    engine.say(talk)
    engine.runAndWait()
    print(talk)

from datetime import datetime
time = datetime.now().hour

import pyttsx3 
engine = pyttsx3.init()
    
q1name = [
    "Hey there! My name is jokingo, I'm a joke teller. What's your name?",
    "Yo! Jokingo here, what's your name?",
    "Ayo Jokingo on board! What's your name?",
    "What's up pal, im Jokingo the joke teller, what's your name?",
    "Jokingo the joke teller this side, what's your name?",
    "Wassup! I'm Jokingo, your personal joke machine. What should I call you?",
    "Yo yo yo! Jokingo in the house! What's your name, buddy?",
    "Hey hey! I'm Jokingo, the king of jokes. What's your name?",
    "Knock knock! It's Jokingo. Who's there? Oh wait… you tell me your name first!",
    "Salutations, human! I am Jokingo, the ultimate joke dispenser. Who am I speaking to?",
    "Oi mate! Jokingo here, ready to crack you up. What's your name?",
    "Attention! The Joke Commander, Jokingo, has arrived. What's your name, soldier!",
    "Yo, it's Jokingo! The only AI funnier than your math teacher's jokes. What's your name?",
    "Hey! I'm Jokingo, your daily dose of laughter. And you are…?",
    "Ayy, Jokingo reporting for duty! What's your name, partner?",
]
q1name_random = random.choice(q1name)
    
tts(q1name_random)
name = input("Please enter your name: ").capitalize()

no_name_roasts = [
   "Oh you don't wanna tell me your name? Cool, I don't wanna tell you a joke. Fair trade. Bye.",
   "No name, no jokes. That's the rule. Now shoo.",
   "You wanna stay anonymous? Fine. My jokes will stay undisclosed too. NEXT!",
   "Oh, so we're playing the 'no name' game? Too bad, I'm playing the 'no jokes for you' game.",
   "Bruh, if you can't even introduce yourself, you definitely don't deserve my premium humor. Consider yourself Jokingo-blocked.",
   "Damn, you must be the first person I've met with a name so bad you don't wanna say it. No jokes for you, shameful creature.",
   "I see what you're doing. You're trying to be all mysterious. Newsflash: It's not working. Also, no jokes for you.",
   "If I had a penny for every joke I'm about to tell you, I'd have exactly zero pennies.",
   "No name? Lemme make this simple—no name, no jokes, no discussion. Move along peasant.",
   "I tell jokes, not riddles. And you not giving your name is the biggest riddle here. Solve that first then come back.",
   "Why should I crack a joke for someone who can't even crack a simple introduction?",
   "You're unknown. My jokes are unknown. That makes us even. Goodbye.",
   "No name huh? Looks like the only joke here is YOU.",
   "Bruh at this point I'd rather tell jokes to a rock. At least it has a name—Dwayne.",
   "You don't wanna introduce yourself? Fine, I won't introduce you to my jokes. Fair trade. Bye.",
   "Ohh you dont wanna tell me ur name and still wanna hear a joke? \nHere's the joke : YOUR LIFE. Piss off now."
]
no_name_roasts_random = random.choice(no_name_roasts)

int_name_roasts = [
    "Oh wow, your name is a number? What's next, your birthday is in binary?🤡",
    "So, you're telling me your parents looked at you and said, yeah, this one's a seven?💀",
    "Oh great, I'm talking to a barcode now.😀",
    "Wow, a number? What are you, a robot serial code?🤡",
    "Ah yes, a human calculator. Do you also respond to math equations?",
    "Your name is a number? What's next, your siblings are coordinates?🤡",
    "Oh look, it's the missing digit of pi!🤡",
    "Nice try, but I ain't calling you One, Two, or Three.😀",
    "I bet your best friend's name is an equation.",
    "A number? Lemme guess, your favorite song is 867-5309?"
   ] 

if name.strip().lower() in ["no", "nah", "nope", "i don't wanna tell you my name", "no thanks", "i ain't telling you my name"] :

  tts(no_name_roasts_random)
  print("Should've just said the name instead, run the code again to hear a joke (TELL YOUR NAME THIS TIME FOR GOD'S SAKE)")
  exit()

elif name.strip().isdigit() :
   
   int_name_roasts_random = random.choice(int_name_roasts)
   tts(int_name_roasts_random)
   
   tts("Well looks like no jokes for you then 🥰")
   
   print("Restart the programme and enter a proper name for god's sake this time, you fckin calculator🤡")
   exit()

elif name.replace(".", "").isdigit():

    int_name_roasts_random = random.choice(int_name_roasts)
    tts(int_name_roasts_random)
    
    tts("Well looks like no jokes for you then 🥰")
    
    print("Restart the programme and enter a proper name for god's sake this time, you fckin calculator🤡")
    exit()
   
else :   
 if 5 < time <= 12:
  tts(f"Good morning {name}!")

 elif 12 < time <= 17:
  tts(f"Good afternoon {name}!")
  
 elif 17 < time <= 22:
  tts(f"Good evening {name}!")
  
 else :
  tts(f"Looks like you're a night owl {name}!")
  

q2_category = [
   f"What genre of jokes do you wanna listen to {name}?👀",
   f"So you up for what kinda jokes today {name} ?",
   f"What are you staring at {name} ? Tell me the genre of jokes you wanna hear, bruh this is getting exhausting🙄",
   f"What's your mood today {name} ? What kinda jokes do you wanna hear?👀",
   f"Okay {name}, so what kind of jokes do you wanna hear?"
]
q2_category_random = random.choice(q2_category)
tts(q2_category_random)

tts("The available categories are mentioned below")

print("Available categories are:\n\t1. Programming\n\t2. Miscellaneous\n\t3. Dark\n\t4. Pun(dad jokes)\n\t5. Spooky\n\t6. Christmas\n\t7. Any(includes all categories)")
category_chosen = input("Enter the category of jokes you wanna hear: ").capitalize().strip()



def get_joke_any(category=category_chosen):

  while True :
     try:
      url = f"https://v2.jokeapi.dev/joke/{category}"
      response = requests.get(url)
      joke = response.json() 

      if joke.get("type") == "single":
        return joke.get("joke", "Oops! Couldn't fetch a joke this time.😬")
            
#In return joke.get("joke", "Oops! Couldn't fetch a joke this time."). This isnt a tuple and the "," isn't seperating
#anything, thats how the .get() method works in python since we are accessing a dictionary of the API.
#So if the API works normally and a "joke" key exists, it'll get you a joke but if the API doesnt workk normally and 
#fails to fetch the "joke" key or the "joke" key aint available then it'll print the "Oops! Couldn't fetch a joke this time."
#key which will give u an error msg instead of crashing the program

#check out learning.py for a better explanation with example
      elif joke.get("type") == "twopart":
            return f"{joke.get('setup', 'Oops! Something went wrong.😬')}\n{joke.get('delivery', '')}"
            
      else:
            return "Oops! The joke sever returned something unexpected.😭"
    
     except requests.exceptions.RequestException as e:
      engine.say("Looks like you are not connected to the internet. Do you wanna retry ?")
      engine.runAndWait()
      retry1 = input("Do you wanna retry?(yes/no): ").lower().strip()
      
      if retry1 not in ["ofc", "ofcc", "ofcourse", "why not", "why not?", "ofccc", "obv", "obviously", "absolutely", "yess mf", "yes mf", "yesss mf", "yes", "yess", "yesss", "yeah", "yeahh", "yeahhh", "yos", "yoss", "yosss", "yessirrr", "yessir", "yessirr", "hell yeah", "hell yeahh", "ya", "yh", "yaa", "yup", "yupp", "ok", "okay", "okayy", "okayyy", "okiess", "okiesss", "okie", "okies"] :
        tts("Okay exiting program! Get an internet connection next time you visit me dumbass!")
        exit()
      else : 
        print(f"Network error: {e}, retrying...")
        continue  # This will retry instead of crashing

     except Exception as e:
        engine.say("Oops! There was a problem on our side fetching the joke, do you wanna retry ?")
        engine.runAndWait()
        retry2 = input("Do you wanna retry?(yes/no): ").lower().strip()

        if retry2 not in ["ofc", "ofcc", "ofcourse", "why not", "why not?", "ofccc", "obv", "obviously", "absolutely", "yess mf", "yes mf", "yesss mf", "yes", "yess", "yesss", "yeah", "yeahh", "yeahhh", "yos", "yoss", "yosss", "yessirrr", "yessir", "yessirr", "hell yeah", "hell yeahh", "ya", "yh", "yaa", "yup", "yupp", "ok", "okay", "okayy", "okayyy", "okiess", "okiesss", "okie", "okies"] :
          tts("Okay exiting program, sorry for inconvinience. Try again in a few hours, our servers will be up by then!")
          exit()
        
        else : 
          return f"Error fetching joke: {e}. Retrying..."


joke_final = get_joke_any(category = category_chosen)
engine.say(joke_final)
print(f"Here's the joke:\n{joke_final}")
engine.runAndWait()

while True : 
 
  q3_joke_loop = [
   "Wanna hear another joke?😎",
   "You up for another joke?😎",
   "How about another joke?👀",
   "Shall I hit you with another joke?👀",
   "Another one? I got plenty!😁",
   "Still in the mood for more jokes?👀",
   "Should I bless you with another joke?😂",
   "You ready for another one?",
   "Still wanna hear more, or are your ribs hurting already?😂😂",
   "One more? I promise it's a good one!😁" ]
  q3_joke_loop_random = random.choice(q3_joke_loop)
  tts(q3_joke_loop_random)

  joke_loop_input = input("Do you wanna hear another joke?(yes/no): ")

  if joke_loop_input.strip().lower() in [
        "not funny",
    "that was bad",
    "lame",
    "meh",
    "mid",
    "trash",
    "horrible",
    "terrible",
    "awful",
    "boring",
    "cringe",
    "bruh",
    "👎",
    "weak",
    "bad joke",
    "try again",
    "stop",
    "stfu",
    "shut up",
    "booo",
    "do better",
    "flop",
    "yawn",
    "0/10",
    "not even close",
    "that sucked",
    "delete this",
    "ew",
    "eww",
    "who wrote this?",
    "pain",
    "i've heard better",
    "could be better",
    "was that a joke?",
    "bro...",
    "ugh"] :
    not_funny_roasts = [  
    f"Not funny? Damn {name}, you must be fun at funerals.",  
    f"{name}, your personality is so dry, even the desert called to say 'chill'.",  
    f"If humor was oxygen, you'd be gasping for air right now, {name}.",  
    f"Bro, even a rock has better comedic timing than you, {name}.",  
    f"Not funny? Nah, {name}, your humor just got patch notes and still sucks.",  
    f"{name}, I'd say 'get a sense of humor' but that requires a personality upgrade first.",  
    f"Lmao {name}, I bet you read joke books like they're horror stories.",  
    f"Damn {name}, your existence is already tragic, and now your humor is too?",  
    f"Not funny? {name}, neither is your entire life but you don't see me complaining.",  
    f"{name}, you laugh like a Windows shutdown sound.",  
    f"Your humor is so dead, I'm sending my condolences, {name}.",  
    f"Bruh, even cavemen had better jokes than you, {name}.",  
    f"{name}, you probably think watching paint dry is peak entertainment.",  
    f"Bro, even NPCs react more than you do, {name}.",  
    f"Your humor is like a Nokia 3310—old, unbreakable, and completely useless in today's world.",  
    f"{name}, your reaction time is slower than Internet Explorer loading a meme.",  
    f"Not funny? Damn, {name}, even the crickets are side-eyeing you.",  
    f"I'd suggest a sense of humor, {name}, but I don't think it's in stock for you.",  
    f"Lmaoo {name}, if laughter is medicine, you must be allergic.",  
    f"Bro, even Siri got better comedic timing than you, {name}.",  
    f"{name}, I could explain the joke, but explaining jokes to NPCs isn't worth my time.",  
    f"Not funny? Alright, {name}, go ahead and tell a joke—oh wait, your life already is one.",  
    f"{name}, your humor is so broken, even an update wouldn't fix it.",  
    f"Lmaooo {name}, you got the personality of an Excel spreadsheet.",  
    f"Bro, I bet even AI-generated jokes are funnier than you, {name}.",  
    f"{name}, even Google Translate has more expression than you.",  
    f"Not funny? Bro, your laugh button is more dysfunctional than your WiFi.",  
    f"{name}, your humor is so lifeless, even zombies wouldn't bite it.",  
    f"Lmaoo {name}, your comedic taste is as bland as boiled chicken.",
    f"Ohh that wasn't funny huh? You know what's funny {name}? Your life." ]  
    
    not_funny_roasts_random = random.choice(not_funny_roasts)
    tts(not_funny_roasts_random)
    
    print("\nThat was Jokingo 3.0 for you, hope you had fun\nRun again for more jokes(and roasts) :)")
    break 

  elif joke_loop_input.strip().lower() not in ["ofc", "ofcc", "ofcourse", "why not", "why not?", "ofccc", "obv", "obviously", "absolutely", "yess mf", "yes mf", "yesss mf", "yes", "yess", "yesss", "yeah", "yeahh", "yeahhh", "yos", "yoss", "yosss", "yessirrr", "yessir", "yessirr", "hell yeah", "hell yeahh", "ya", "yh", "yaa", "yup", "yupp", "ok", "okay", "okayy", "okayyy", "okiess", "okiesss", "okie", "okies"] :
    exit_roasts = [
                   f"Okay whatever {name} you lame ass🙄", 
                   f"Fine, whatever {name}, go be boring somewhere else.",
                   f"Alright, party pooper {name}, go touch grass or something.",
                   f"Damn {name}, who hurt you?",
                   f"Okay fine, I didn't wanna tell you jokes anyway.🙄",
                   f"Bruh {name}, you got the personality of a dry biscuit.",
                   f"Alright, Mr./Ms. Fun Police, I'll stop.",
                   f"Your loss, {name}. Hope your life stays as dry as your sense of humor.",
                   f"Okay, I see how it is. I try to make you laugh, and you just reject me like my crush did.",
                   f"Damn, I thought we had something special, {name}. Guess not. 💔",
                   f"Alright {name}, go back to being a humorless NPC.",
                   f"Bet. I'll just sit here, unloved and ignored, like Internet Explorer in 2025.",
                   f"No jokes? No problem. I'll just cry in binary. 😢 01000011 01110010 01111001",
                   f"Aight {name}, go be a disappointment somewhere else.",
                   f"Wow {name}, rejecting jokes? That's crazy. Couldn't be me.",
                   f"Fine. I'll just entertain myself like I always do. Ohh the sadness never fades 💔. Nah just kidding, fuck off i don't care"
                   ]
    exit_roasts_random = random.choice(exit_roasts)
    tts(exit_roasts_random)
    
    print("\nThat was Jokingo 3.0 for you, hope you had fun\nRun again for more jokes(and roasts) :)")
    break
    
  else : 
   tts("You wanna continue with the same category of jokes right?")
   
   q4_switch_category = input(("Do you want to continue with the same category of jokes?(yes/no): "))
   if q4_switch_category.strip().lower() not in ["ofc", "ofcc", "ofcourse", "why not", "why not?", "ofccc", "obv", "obviously", "absolutely", "yess mf", "yes mf", "yesss mf", "yes", "yess", "yesss", "yeah", "yeahh", "yeahhh", "yos", "yoss", "yosss", "yessirrr", "yessir", "yessirr", "hell yeah", "hell yeahh", "ya", "yh", "yaa", "yup", "yupp", "ok", "okay", "okayy", "okayyy", "okiess", "okiesss", "okie", "okies"] :
     tts("Select a category") 
     print("Available categories are:\n\t1. Programming\n\t2. Miscellaneous\n\t3. Dark\n\t4. Pun(dad jokes)\n\t5. Spooky\n\t6. Christmas\n\t7. Any(includes all categories)")
     
     switch_category_input = input("Enter the category of jokes you wanna hear: ").strip().capitalize()
     
     joke_final = get_joke_any(category = switch_category_input)
     engine.say(joke_final)
     print(f"Here's the joke:\n{joke_final}")
     engine.runAndWait()

   else : 
     joke_final = get_joke_any(category = category_chosen)
     engine.say(joke_final)
     print(f"Here's the joke:\n{joke_final}")
     engine.runAndWait()
     

