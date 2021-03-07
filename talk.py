import pyttsx3

engine = pyttsx3.init()

engine.setProperty('volume', 0.9)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)

engine.say("Hello World")

engine.runAndWait()