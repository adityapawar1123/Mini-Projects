import speech_recognition as sr
import pyaudio
import pyttsx3 
engine = pyttsx3.init()
import random 
from datetime import datetime 

time = datetime.now().hour
greet = "Calc here!"
if 5 <= time < 12 :
   engine.say("Good morning,"+ greet)
   engine.runAndWait()
elif 12 <= time < 16 :
   engine.say("Good afternoon,"+ greet)
   engine.runAndWait()
elif 16 <= time < 22 :
   engine.say("Good evening,"+ greet)
   engine.runAndWait()
else : 
   engine.say("Hey night owl,"+ greet)
   engine.runAndWait()


while True : 
 engine.say("Please speak the first number : ")
 engine.runAndWait()
 def speech_recog(prompt = "Speak now: ") :
  r = sr.Recognizer()

  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)  # Helps with background noise
    
    while True : #Loops for users input until speech not recognized 
     print(prompt)
     audio_text = r.listen(source)  # More time for short words  
     print("Processing....")    
     
     try:
        # using google r.recognize_google(audio_text) recognition
        print("Recognized: "+r.recognize_google(audio_text))
        return r.recognize_google(audio_text)
     #This return statement ends the loop once speech is recognised
     
     except:
         print("Sorry, I did not get that. Try again.")

        
 while True : 
  a1 = speech_recog()  
  if a1.isdigit() == False :
     engine.say("Don't you understand what a number is dumbass?")
     engine.runAndWait()
     print("You didn't enter a number please try again")
  else :
     break 
#This loop fixes the prob of WHAT IF SMONE DOESN'T SPEAK A NUMBER
 a = int(a1)
 print(a)
      
 engine.say("What do you want me to do with this number?")
 engine.runAndWait()

 question1 = speech_recog()

 if question1 in ["square it" ,"square", "raise power to two", "raise power to 2"] : 
        engine.say(f"The square of {a} is {a**2}")
        engine.runAndWait()
        print(f"The square of {a} is {a**2}")

 elif question1 in ["square root", "root", "what's its root", "what's its square root", "what is its square root", "what is its root"] :
        square_root = f"The square root of {a} is {a**0.5}"
        engine.say(square_root)
        engine.runAndWait()
        print(square_root)

 elif question1 in ["increase its power", "exponent", "raise to power"] : 
        engine.say("Enter the power")
        engine.runAndWait()
        
        while True :
             p1 = speech_recog() 
             if p1.isdigit() == False : 
               engine.say("Don't you understand what an exponent is dumbass?")
               engine.runAndWait()
               print("You didn't enter a number please try again")
             else :
               break
        p = int(p1)
           
        power = f"The answer for {a} raise to the power {p} is {a**p}"
        engine.say(power)
        engine.runAndWait()
        print(power) 

 else : 
    engine.say("Please enter your second number")
    engine.runAndWait()
    
    
    while True : 
       b1 = speech_recog()
       if b1.isdigit() == False : 
          engine.say("Don't you understand what a number is dumbass?")
          engine.runAndWait()
          print("You didn't enter a number please try again")
       else : 
          break
    b = int(b1)

    
    engine.say("What do you want me to do with these 2 numbers?")
    engine.runAndWait()
    print("What do you want me to do with these 2 numbers?")
    
    question2 = speech_recog()

    if question2 in ["add", "addition", "add numbers", "add them", "i want you to add them"] :
       sum = f"The sum of {a} and {b} is {a+b}"
       engine.say(sum)
       engine.runAndWait()
       print(sum)

    elif question2 in ["subtract", "subtraction", "subtract numbers", "subtract them", "i want you to subtract them"] : 
       subtract = f"The difference of {a} and {b} is {a-b}"
       engine.say(subtract)
       engine.runAndWait()
       print(subtract)

    elif question2 in ["multiply", "multiplication", "multiply them", "i want you to multiply them"] :
       multiply = f"The product of {a} and {b} is {a*b}"
       engine.say(multiply)
       engine.runAndWait()
       print(multiply)

    elif question2 in ["divide", "division", "divide them", "i want you to divide them"] : 
       if b != 0 :
        divide = f"The quotient of {a} and {b} is {a/b}"
        engine.say(divide)
        engine.runAndWait()
        print(divide)
       else : 
        error = "Division by zero is not possible."
        engine.say(error)
        engine.runAndWait()
        print(error)

    elif question2 in ["remainder", "remainder of", "division remainder", "what's their remainder"] :
     if b != 0 : 
      remainder = f"The remainder of {a} and {b} is {a%b}"
      engine.say(remainder)
      engine.runAndWait()
      print(remainder)
     else : 
      error2 = "Division by zero is not possible, so I can't give you a remainder."
      engine.say(error2)
      engine.runAndWait()
      print(error2)

    else :
     engine.say("I can't perform that operation.")
     engine.runAndWait()
     print("I can't perform that operation.")

 loop_prompts = [
           "Want me to crunch some more numbers?",
           "Need another calculation? Hit me up!",
           "Another one? I got you!",
           "Math ain't over yet! Need more?",
           "I live to calculate! Shall we continue?",
           "I won't judge if you need more help. Want another?",
           "Would you like me to perform another calculation?",
           "Shall I assist you with another one?",
           "Would you like to continue?",
           "Need me to do another one?"]
 loop_prompts_random = random.choice(loop_prompts)

 engine.say(loop_prompts_random)
 engine.runAndWait()
 print(loop_prompts_random+"\nSay yes or no")

 loop_question = speech_recog()

 if loop_question not in ["yes", "yeah", "yea", "yh", "ya", "ok", "okay", "yessir", "yess", "yessirr", "yes sir", "yup", "yupp", "yes please", "please do"] :
   engine.say("Okay sir, have a good day!")
   engine.runAndWait()
   break


