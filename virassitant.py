import speech_recognition as sr 
import wikipedia
import pyttsx3

engine=pyttsx3.init()
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise...Please wait')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording')

try:
    print('Printing your message...Please wait')
    text=recognizer.recognize_google(recordedaudio,language='en-US')
    print('Your Message:{}',format(text))

except Exception as ex:
    print(ex)

#Input data
wikisearch=wikipedia.summary(text)
engine.say(wikisearch)
engine.runAndWait()