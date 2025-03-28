import pyttsx3
engine = pyttsx3.init()

def tts(text) : 
    engine.say(text)