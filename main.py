import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import musiclib
import requests
from openai import OpenAI
import pygame
from gtts import gTTS

tts=gTTS('hello.mp3')
tts.save('hello.mp3')

def speakg(text):
    tts=gTTS('hello.mp3')
    tts.save('hello.mp3')
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temp.mp3')    

newsapi="ab2xxxxxxxxxxxxxxxxxxx"

def speakq(text):
    os.system(f'espeak "{text}"')

speakq("Hello Dipanshu")




def aiprocess(command):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-03dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    )

    completion = client.chat.completions.create(
    extra_headers={
       "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
         "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
         },
      model="nvidia/nemotron-3-super-120b-a12b:free",
      messages=[
       {
      "role": "user",
      "content": command
        }
       ]
    )
    return(completion.choices[0].message.content)

   




recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait() 

def speak2(text):
    engine.say(text)
    engine.runAndWait() 

          
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")    
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")    
    elif c.lower().startswith("manipur"):
        song=c.lower().split(" ")[0]
        link=musiclib.music[song]
        webbrowser.open(link)  
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=ab25fe106xxxxxxxxxxxxxxxxxx") 
       
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            
            for article in articles:
                speakq(article['title'])
                print(article['title'])
            
    else:
        
        output=aiprocess(c)
        speakq(output)
        print(output)
             
             
           
           
            
                
    
if __name__=="__main__":
    speak("Initializing Jarvis..")
    while True:
        #Listen for the wake word "jarvis"
        #obtain audio from the microphone
        
        r=sr.Recognizer()
        print("Recognizing...")
        
            
            
        try:
            with sr.Microphone() as source:
                  print("Listening...")
                  audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speakq("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvise is Active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    
                    processcommand(command)
                
                       
            print(command)
        except Exception as e:
            print("Error;{0}",format(e))
                
            
    
        
