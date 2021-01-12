import speech_recognition as sr
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS

listener = sr.Recognizer() #we are reconigzing the voice of the user

#function for recording audio
def record_audio(ask = False):
    with sr.Microphone() as source:  #this is source of the audio
        #print('Listening...')
        if ask:
            #print(ask)
            selena_speak(ask)
        voice = listener.listen(source) #this will listen to source
            #we have now found the source from microphone
        voice_data = ''
        try:
            voice_data = listener.recognize_google(voice)
            #print(voice_data)
        except sr.UnknownValueError:
            #print("Sorry I didn't get that")
            selena_speak("Sorry I didn't get that")
        except sr.RequestError:
            #print("Sorry, my speech service is down")
            selena_speak("Sorry, my speech service is down")
        return voice_data

def selena_speak(audio_string):
    text_to_speech = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 100000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string) #prints to console
    os.remove(audio_file)

#function for responding to voice instructions by Patrick
def respond(voice_data):
    if 'what is your name' in voice_data:
        #print('My name is Selena')
        selena_speak('My name is Selena')
    if 'your name please' in voice_data:
        #print('My name is Selena')
        selena_speak('My name is Selena')
    if 'what time is it' in voice_data:
        #print(ctime())
        selena_speak(ctime())
    if 'what is the time' in voice_data:
        #print(ctime())
        selena_speak(ctime())
    if 'what day is it' in voice_data:
        #print(ctime())
        selena_speak(ctime())
    if 'what is the day' in voice_data:
        #print(ctime())
        selena_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'http://google.com/search?q=' + search
        webbrowser.get().open(url)
        #print('Here is what I found on google for ' + search)
        selena_speak('Here is what I found on google for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'http://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        #print('Here is the location of ' + location)
        selena_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        #print('bye')
        selena_speak('bye')
        exit()
   
        
time.sleep(1)
#print('Hello there, how can i help you?')
selena_speak('Hello there, how can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
#print(voice_data)

