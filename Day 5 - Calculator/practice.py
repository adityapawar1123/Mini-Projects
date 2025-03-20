import speech_recognition as sr
import pyaudio
import pyttsx3 

engine = pyttsx3.init()

# Initialize recognizer class (for recognizing the r.recognize_google(audio_text))
r = sr.Recognizer()

# Reading Microphone as source
# listening the r.recognize_google(audio_text) and store in audio variable
with sr.Microphone() as source:
    engine.say("Hey, calc here! Please speak the first number : ")
    engine.runAndWait()
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    # recoginze_() method will throw a request
    # error if the API is unreachable,
    # hence using exception handling
    
try:
        # using google r.recognize_google(audio_text) recognition
        print("Text: "+r.recognize_google(audio_text))
except:
         print("Sorry, I did not get that")

a = int(r.recognize_google(audio_text))
print(a)

engine.say("What do you want me to do with this number?")
engine.runAndWait()

with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
try:
        print("Text: "+r.recognize_google(audio_text))
except:
        print("Sorry, I did not get that")


if r.recognize_google(audio_text) in ["square it" ,"square", "raise power to two", "raise power to 2"] : 
        engine.say(f"The square of {a} is {a**2}")
        engine.runAndWait()
        print(f"The square of {a} is {a**2}")

elif r.recognize_google(audio_text) in ["square root", "root", "what's its root", "what's its square root", "what is its square root", "what is its root"] :
        square_root = f"The square root of {a} is {a**0.5}"
        engine.say(square_root)
        engine.runAndWait()
        print(square_root)

elif r.recognize_google(audio_text) in ["increase its power", "exponent", "raise to power"] : 
        engine.say("Enter the power")
        engine.runAndWait()
        with sr.Microphone() as source:
         print("Talk")
         audio_text = r.listen(source)
         print("Time over, thanks")
        try:
            print("Text: "+r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")

        p = int(r.recognize_google(audio_text))
        power = f"The answer for {a} raise to the power {p} is {a**p}"
        engine.say(power)
        engine.runAndWait()
        print(power) 

else : 
    engine.say("Please enter your second number")
    engine.runAndWait()
    with sr.Microphone() as source:
         print("Talk")
         audio_text = r.listen(source)
         print("Time over, thanks")
    try:
         print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")
    b = int(r.recognize_google(audio_text))
    print(b)

    
    engine.say("What do you want me to do with these 2 numbers?")
    engine.runAndWait()
    with sr.Microphone() as source:
     print("Talk")
     audio_text = r.listen(source)
     print("Time over, thanks")
    try:
     print("Text: "+r.recognize_google(audio_text))
    except:
     print("Sorry, I did not get that")

#Code works perfectly fine till this line

    if r.recognize_google(audio_text) in ["add", "addition", "add numbers", "add them", "i want you to add them"] :
       sum = f"The sum of {a} and {b} is {a+b}"
       engine.say(sum)
       engine.runAndWait()
       print(sum)



    elif r.recognize_google(audio_text) in ["subtract", "subtraction", "subtract numbers", "subtract them", "i want you to subtract them"] : 
       subtract = f"The difference of {a} and {b} is {a-b}"
       engine.say(subtract)
       engine.runAndWait()
       print(subtract)

    elif r.recognize_google(audio_text) in ["multiply", "multiplication", "multiply them", "i want you to multiply them"] :
       multiply = f"The product of {a} and {b} is {a*b}"
       engine.say(multiply)
       engine.runAndWait()
       print(multiply)

 
  




