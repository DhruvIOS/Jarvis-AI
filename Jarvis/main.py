import pyttsx3
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from cmd import *
from simple_colors import *


translator = Translator()
listener = sr.Recognizer()


engine = pyttsx3.init()


engine.say("Jarvis Activated")
engine.runAndWait()


try:

    while True:

        with sr.Microphone() as mic:
            print(cyan("Jarvis is listening..."))
            voice = listener.listen(mic)
            speech_text = listener.recognize_google(voice)
            speech_text = speech_text.lower()

            if 'translate' in speech_text:

                translate()

            elif 'date' in speech_text:
                Telldate()

            elif 'joke' in speech_text:
                joke()

            elif 'tell me about' in speech_text:
                wiki(speech_text)

            elif 'deactivate' in speech_text:

                print(red("Jarvis deactivated"))

                engine.say("Jarvis deactivated")
                engine.runAndWait()
                break

            else:
                print(red('Please say the command again'))


except sr.UnknownValueError:
    print("Could not understand")

except sr.RequestError:
    print("Could not request google")

except Exception as e:
    print(e)
