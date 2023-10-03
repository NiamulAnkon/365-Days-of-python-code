import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
  record = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening......")
    record.adjust_for_ambient_noise(source)
    audio = record.listen(source)

  try:
    print("recognizing...")
    data = record.recognize_google(audio)
    return data
  except sr.UnknownValueError:
    print("Not understanding :(")


def speech_tx(x):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)
  rate = engine.getProperty('rate')
  engine.setProperty('rate', 150)
  engine.say(x)
  engine.runAndWait()


if __name__ == "__main__":

    while True:
        data_1 = sptext().lower()

          
        if "your name" in data_1:
          name = "my name is jarvis"
          speech_tx(name)

        elif "old are you" in data_1:
            age = "i am 11 years old"
            speech_tx(age)

        elif "time" in data_1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speech_tx(time)

        elif "youtube" in data_1:
            webbrowser.open('https://www.youtube.com/')
            message_1 = "turning on youtube"
            speech_tx(message_1)

        elif "channel" in data_1:
            webbrowser.open("https://www.youtube.com/@ATHECALPLAYS/videos")
            message_2 = "turning on your youtube channel"
            speech_tx(message_2)

        elif "joke" in data_1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speech_tx(joke_1)

        elif "song" in data_1:
            adders = "D:\song"
            lissong = os.listdir(adders)
            print(lissong)
            os.startfile(os.path.join(adders, lissong[0]))
            message_3 = "playing song for you"
            speech_tx(message_3)

        elif "do you love me" in data_1:
            reply = "yes i do love ou and i am not gonna let you die alone"
            speech_tx(reply)

        elif "exit" in data_1:
            speech_tx("Thank you sir")
            break