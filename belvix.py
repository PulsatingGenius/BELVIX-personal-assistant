import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import re
import requests
import random
import string
from bs4 import BeautifulSoup
from urllib.request import urlopen
import subprocess
import json 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
      engine.say(audio)
      engine.runAndWait()

def time():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("sir the current time is " + strTime)

def date():
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak(date)
        speak(month)
        speak(year)

def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("good morning ")
            speak("welcome back sir")
            time()
            speak("today the date is")
            date()

        elif hour >= 12 and hour < 18:
            speak("good afternoon ,aman")
            speak("welcome back sir")
            time()
            speak("today the date is")
            date()
        else:
            speak("good evening ,aman , how was your day?")
            speak("welcome back sir")
            time()
            speak("today the date is")
            date()

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....,,.")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing..,,.")
            query = r.recognize_google(audio, language='en-in')
            print("user said:", query)

        except Exception as e:
            print(e)

            print("say that again ,please")
            return "none"

        return query

def send_mail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('email', 'password')
        server.send_mail(to, content)
        server.close()


wishme()
query = takecommand()


def main():
    query = takecommand()
    if 'wikipedia' in query.lower():
        speak('searching wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        print(results)
        speak(results)


    elif 'open google' in query.lower():
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open youtube' in query.lower():
    
        url = 'youtube.com'
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
       to = takecommand()
       speak("what should i sent")
       content = takecommand()
       send_mail(to, content)

    elif 'what is the date' in query.lower():
         year = int(datetime.datetime.now().year)
         month = int(datetime.datetime.now().month)
         date = int(datetime.datetime.now().day)
         speak(date)
         speak(month)
         speak(year)
    
    elif "who are you" in query.lower() or 'where are you' in query.lower() or 'what are you' in query.lower():
        setReplies = [' I am BELVIX' + 'In your system'+'I am an example of AI']
        speak(setReplies)
    elif 'hello' in query.lower() or 'hey' in query.lower():
        speak('hey')
    elif 'bye' in query.lower():
       speak("bye have a better day ahead")

    elif 'create a password' in query.lower() or 'give me a password' in query.lower():
        sep = ""
        random.choice(string.ascii_letters)
        password = []
        let1 = random.randint(1,9)
        let2 = random.randint(1,9)
        let3 = random.choice(string.ascii_letters)
        let4 = random.randint(1,9)
        let5 = random.choice(string.ascii_letters)
        let6 = random.choice(string.ascii_letters)
        let7 = random.randint(1,9)
        let8 = random.choice(string.ascii_letters)
        let9 = random.randint(1,9)
        let10 = random.randint(1,9)
        let11 = random.choice(string.ascii_letters)
        let12 = random.randint(1,9)
        let13 = random.choice(string.ascii_letters)
        let14 = random.choice(string.ascii_letters)
        let15 = random.randint(1,9)
        let16 = random.choice(string.ascii_letters)
        print(let1,let2,let3,let4,let5,let6,let7,let8,let9,let10,let11,let12,let13,let14,let15,let16, sep="")
    
    
    elif 'play music' in query.lower():
        reg_ex = re.search('play (.+)', query)
        if reg_ex:
            searchedSong = reg_ex.group(1)
            url = 'https://www.youtube.com/results?q=' + searchedSong
            try:
                source_code = requests.get(url, headers=headers, timeout=15)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, "html.parser")
                songs = soup.findAll('div', {'class': 'yt-lockup-video'})
                song = songs[0].contents[0].contents[0].contents[0]
                hit = song['href']
                webbrowser.open('https://www.youtube.com' + hit)
                speak('Playing ' + searchedSong + ' on Youtube.')
            except Exception as e:
                webbrowser.open(url)
                speak('Searching for ' + searchedSong + ' on Youtube.')   
    

    elif 'joke' in query.lower(): 
        res = requests.get( 'https://icanhazdadjoke.com/', headers={"Accept":"application/json"} )
        
        if res.status_code == requests.codes.ok: 
           speak(str(res.json()['joke'])) 
        else: 
            speak('oops!I ran out of jokes')

    elif 'news' in query.lower():
        try:
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = BeautifulSoup(xml_page, "html.parser")
            news_list = soup_page.findAll("item")
            for news in news_list[:5]:
                speak(news.title.text)
        except Exception as e:
            print(e)
    
    
    elif 'tell me about' in query.lower():
        reg_ex = re.search('tell me about (.*)', query)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                print(wikipedia.summary(topic, sentences=3))
                speak(wikipedia.summary(topic, sentences=3))
        except Exception as e:
            speak(e)

    
    elif 'search' in query.lower():
        reg_ex = re.search('search (.+)', query)
        if reg_ex:
            subject = reg_ex.group(1)
            url = 'https://www.google.com/search?q=' + subject
            webbrowser.open(url)
            speak('Searching for ' + subject + ' on Google.')
    
    
    elif 'current weather' in query.lower():
          api_key = "api key"
          base_url = "http://api.openweathermap.org/data/2.5/weather?"
          speak("which city sir")
          city_name = takecommand()
          complete_url = base_url + "q=" + city_name + "&appid="+ api_key
          response = requests.get(complete_url)
          x = response.json() 
          if x["cod"] != "404": 
                y = x["main"]
                current_temperature = y["temp"] 
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"] 
                weather_description = z[0]["description"]
                speak(" Temperature (in kelvin unit) = " +
                            str(current_temperature) + 
                   "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                   "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                    "\n description = " +
                            str(weather_description))      
          else:
                speak(" City Not Found ")

             
while True:
     main()
    
