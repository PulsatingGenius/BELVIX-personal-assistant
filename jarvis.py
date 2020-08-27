import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning ")

    elif hour >=12 and hour <18:
        speak("good afternoon ,aman")
    else:
        speak("good evening ,aman , how was your day?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....,,.")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..,,.")
        query = r.recognize_google(audio,language='en-in')
        print("user said:",query)

    except Exception as e:
        print(e)

        print("say that again ,please")
        return  "none"

    return query

def send_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('amangd1618@gmail.com','75o6QY2f81X7Pn1g')
    server.send_mail(to ,content)
    server.close()


wishme()
query = takecommand()


if 'wikipedia' in query.lower():
    speak('searching wikipedia....')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences = 3)
    print(results)
    speak(results)
    

elif 'open youtube' in query.lower():
    
    url = 'youtube.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open google' in query.lower():
    
    url = 'google.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open facebook' in query.lower():
    
    url = 'facebook.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    

elif 'open github' in query.lower():
    url = 'github.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'what is the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak("aman  the time is " + strTime)

elif 'vs code' in query.lower():
    code_path = "C:\\Program Files\\Microsoft VS Code\\code.exe"
    os.startfile(code_path)

elif 'send a mail' in query.lower():
    speak("to whom ")
    to =  takecommand()
    speak("what should i sent")
    content = takecommand()
    send_mail(to, content)

