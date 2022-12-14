from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
from simple_colors import *
import pyttsx3
from googletrans import Translator
import time
from datetime import date
import wikipedia
import pyjokes


engine = pyttsx3.init()

translator = Translator()
listener = sr.Recognizer()


def translate():
    lngTgt = None

    languageSelected = None

    try:

        while True:

            with sr.Microphone() as mic:
                print("[ 1 ] Hindi ")

                print("[ 2 ] Gujarati ")

                print("[ 3 ] Spanish")

                engine.say("Say 1 for Hindi")
                engine.say("Say 2 for Gujarati")
                engine.say("Say 3 for Spanish")

                engine.runAndWait()

                # tts = gTTS('What lanuage you want to translate to')
                # tts.save('lanSelect.mp3')

                # playsound('lanSelect.mp3')
                engine.say("What lanuage you want to translate to")

                print('What lanuage you want to translate to')

                engine.runAndWait()

                voice = listener.listen(mic)
                speech_text = listener.recognize_google(voice)
                speech_text = speech_text.lower()

                if 'exit' in speech_text:
                    print(red("Jarvis Going to home "))

                    engine.say("Jarvis going to home")
                    engine.runAndWait()
                    break

                else:

                    if speech_text == '1':
                        lngTgt = 'hi'
                        languageSelected = "Hindi"

                    elif speech_text == '2':
                        lngTgt = 'gu'
                        languageSelected = "Gujarati"

                    else:
                        lngTgt = 'es'
                        languageSelected = "Spanish"

                engine.say("What text you want to translate")

            with sr.Microphone() as source:

                print("What text you want to translate")

                engine.runAndWait()

                voice = listener.listen(source)
                speech_text = listener.recognize_google(voice)
                speech_text = speech_text.lower()

                if 'exit' in speech_text:
                    print(red("Jarvis Going to home "))

                    engine.say("Jarvis going to home")
                    engine.runAndWait()
                    break

                else:
                    print(blue(f'Selcted language{languageSelected}', 'bold'))
                    translated = translator.translate(speech_text, dest=lngTgt)
                    translated_text = translated.text

                    print('Translation for', red(speech_text, 'bold'),
                          'is', green(translated_text, 'bold'))
                    voice = gTTS(translated_text, lang=lngTgt)
                    voice.save('voice.mp3')
                    playsound('voice.mp3')

    except sr.UnknownValueError:
        print("Could not understand")

    except sr.RequestError:
        print("Could not request google")

    except Exception as e:
        print(e)

translate()
def Telldate():
    curr_time = time.strftime("%I:%M:%p", time.localtime())
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    print(magenta(f'It is {d2} at {curr_time}'))
    engine.say(f'It is {d2} at {curr_time}')
    # print('date')

    engine.runAndWait()


def wiki(speech_text):

    speech_text = speech_text.lower()
    person = speech_text.replace("tell me about ", '')
    info = wikipedia.summary(person, 1)

    print(magenta(info))
    engine.say(info)
    engine.runAndWait()


def joke():
    """
    Takes bar and does some things to it.
    """

    tellJoke = pyjokes.get_joke()

    print(magenta(tellJoke))

    engine.say(tellJoke)
    engine.runAndWait()
