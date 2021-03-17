import speech_recognition as sr
import yagmail

recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording..!')
try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your message:{}'.format(text))

except Exception as ex:
    print(ex)

#Automate mails:

reciever=' Receiver's email id'
message=text
sender=yagmail.SMTP('Sender's email id ')
sender.send(to=reciever,subject='This is an automated mail',contents=message)