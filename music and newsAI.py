#Modules required

import speech_recognition as sr 
from GoogleNews import GoogleNews
import pyttsx3

#Intialization
googlenews = GoogleNews()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

#Commands
def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source,timeout=1)
        print("Done recording..!")
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)

    if 'headlines' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Today news')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    if 'tech' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Tech')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    if 'politics' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Politics')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    if 'sports' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Sports')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    if 'cricket' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('cricket')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')
cmd()