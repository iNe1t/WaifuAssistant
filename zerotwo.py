#Code by iNe1t
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('volume', 0.9)

engine.say("Darling")

engine.runAndWait()