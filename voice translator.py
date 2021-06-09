import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3 
recognizer=sr.Recognizer()
engine = pyttsx3.init()
with sr.Microphone() as source: 
    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for message..') 
    audio = recognizer.listen(source,timeout=1)
    print('Done recording..') 
try:
    print('Recognizing..')
    result = recognizer.recognize_google(audio,language='ta-IN')
except Exception as ex:
    print(ex)
def trans():
    langinput=input('Type the language you want to convert:')
    translator = google_translator()  
    translate_text = translator.translate(str(result),lang_tgt=str(langinput))  
    print(translate_text)
    engine.say(str(translate_text))
    engine.runAndWait()
trans()
    
