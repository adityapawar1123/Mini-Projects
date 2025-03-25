import speech_recognition as sr
import pyaudio
import pyttsx3 
engine = pyttsx3.init()
import random 
from datetime import datetime 

def is_number(n) : 
    try :
        num = float(n)
        return True 
    except ValueError:
        tts("You entered a invalid number")
        return False 

def tts(talk) :
    engine.say(talk)
    engine.runAndWait()
    print(talk)

time = datetime.now().hour
greet = "Calc here!"
if 5 <= time < 12 :
   tts("Good morning,"+ greet)
elif 12 <= time < 16 :
   tts("Good afternoon,"+ greet)
elif 16 <= time < 22 :
   tts("Good evening,"+ greet)
else : 
   tts("Hey night owl,"+ greet)


while True : 
 tts("Please speak the first number")
 print("We are facing some speech recognition issues right now. So if your number is under or equal to 10,\nLet's say your number is 7 then please say \"seven point zero\" instead of \"seven\"")
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
        recognized_text = r.recognize_google(audio_text)
        print("Recognized: "+recognized_text)
        return recognized_text
     #This return statement ends the loop once speech is recognised
     
     except:
         print("Sorry, I did not get that. Try again.")

        
 while True : 
  a1 = speech_recog()  
  if is_number(a1) == False :
     tts("Don't you understand what a number is dumbass?")
     print("You didn't enter a number please try again")
  else :
     break 
 a = float(a1)
#This loop fixes the prob of WHAT IF SMONE DOESN'T SPEAK A NUMBER
      
 tts("What do you want me to do with this number?")

 question1 = speech_recog()

 if question1 in ["square it" ,"square", "raise power to two", "raise power to 2"] : 
        tts(f"The square of {a} is {a**2}")
   

 elif question1 in ["square root", "root", "what's its root", "what's its square root", "what is its square root", "what is its root"] :
        square_root = f"The square root of {a} is {a**0.5}"
        tts(square_root)

 elif question1 in ["increase its power", "exponent", "raise to power"] : 
        tts("Enter the power")
        print("We are facing some speech recognition issues right now. So if your number is under or equal to 10,\nLet's say your number is 7 then please say \"seven point zero\" instead of \"seven\"\nThanks for your cooperation!")

        while True :
             p1 = speech_recog() 
             if is_number(p1) == False : 
               tts("Don't you understand what an exponent is dumbass?")
               print("You didn't enter a number please try again")
             else :
               break
        p = float(p1)  
        power = f"The answer for {a} raise to the power {p} is {a**p}"
        tts(power)

 else : 
    tts("Please enter your second number")
    print("We are facing some speech recognition issues right now. So if your number is under or equal to 10,\nLet's say your number is 7 then please say \"seven point zero\" instead of \"seven\"")


    while True : 
       b1 = speech_recog()
       if is_number(b1) == False : 
          tts("Don't you understand what a number is dumbass?")
          print("You didn't enter a number please try again")
       else : 
          break
    b = float(b1)

    
    tts("What do you want me to do with these 2 numbers?")
    
    question2 = speech_recog()

    if question2 in ["add", "addition", "add numbers", "add them", "i want you to add them"] :
       sum = f"The sum of {a} and {b} is {a+b}"
       tts(sum)

    elif question2 in ["subtract", "subtraction", "subtract numbers", "subtract them", "i want you to subtract them"] : 
       subtract = f"The difference of {a} and {b} is {a-b}"
       tts(subtract)

    elif question2 in ["multiply", "multiplication", "multiply them", "i want you to multiply them"] :
       multiply = f"The product of {a} and {b} is {a*b}"
       tts(multiply)

    elif question2 in ["divide", "division", "divide them", "i want you to divide them"] : 
       if b != 0 :
        divide = f"The quotient of {a} and {b} is {a/b}"
        tts(divide)
   
       else : 
        error = "Division by zero is not possible."
        tts(error)

    elif question2 in ["remainder", "remainder of", "division remainder", "what's their remainder"] :
     if b != 0 : 
      remainder = f"The remainder of {a} and {b} is {a%b}"
      tts(remainder)

     else : 
      error2 = "Division by zero is not possible, so I can't give you a remainder."
      tts(error2)

    else :
     tts("I can't perform that operation.")


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

 tts(loop_prompts_random)
 print("Say yes or no")
 print("We are facing some speech recognition issues right now. So if you wanna continue, please say \"yes sir\\yes please\\yes calc\\yes calculator\" instead of \"yes\"\nThanks for your cooperation! ")

 loop_question = speech_recog()

 if loop_question not in ["yes", "yeah", "yea", "yh", "ya", "ok", "okay", "yessir", "yess", "yessirr", "yes sir", "yup", "yupp", "yes please", "please do", "yes calc", "yes calculator"] :
   tts("Okay sir, have a good day!")
   break