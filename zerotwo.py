#Code by iNe1t
#
#
#
#
# Импортируем
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

# engine.say("Good morning, my darling")

# Настроечки

engine.setProperty('volume', 0.9)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)
r = sr.Recognizer()

#Цикл прослушивания
while True:
    with sr.Microphone(device_index = 1) as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Я вас слушаю")
        engine.say("Готова слушать")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = 'ru-RU')
            text = query.lower()
            print(f'Вы сказали: {query.lower()}')
            if text == "яблоко":
                print("Нет Банан")
                engine.say("Нет банан")
        except:
            print("EGGOG")
            engine.say("Что то не так")
        engine.runAndWait()