import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Pleasw wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
    if 'chrome'in text:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
while True:
    cmd()



