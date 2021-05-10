import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from tkinter import *
from PIL import Image,ImageTk
import requests
import json
from os import startfile
import speedtest


def speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[0].id')
    engine.say(audio)
    engine.runAndWait()
def Greet():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
    speak("I am vision. How can I help you")
    print("I am vision. How can I help you")
def invokeVision():
    Query = recognise().lower()
    if "hello vision" in Query:
        Greet()
        return True
def getQuery():
    while(True):
        Query=recognise().lower()
        if "hello vision" in Query:
             Greet()
        elif "open google" in Query:
            speak("What do you want to search from google?")
            google_search = recognise().lower()
            speak("searching"+ google_search)
            webbrowser.open("https://www.google.com/search?q=" + google_search)
            continue
        elif "open youtube" in Query:
            speak("WHat do you want to search from youtube")
            yt_search = recognise().lower()
            speak("seearching"+yt_search)
            webbrowser.open("https://www.youtube.com/results?search_query=" + yt_search)
            continue
        elif "show me the latest news around the world" in Query:
            speak("fetching latest news")
            webbrowser.open("https://www.thehindu.com/")
            speak("Here are some headlines from  the  hindu")
            continue
        elif "weather" in Query:
            apiKey = "get your api by signing up"
            url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Enter your city name : ")
            cityName = input("Enter your city name : ")
            fullUrl = url + "appid=" + apiKey + "&q=" + cityName
            output = requests.get(fullUrl)
            temp=output.json()
            print(temp)
            if temp["cod"] != "404":
                x = temp['main']
                x1 = temp['coord']
                speak("Here is the weather forecast of ")
                speak(cityName)
                print("Weather forecast in ", cityName, ":")
                print("Current temperature :", int((x['temp'] - 273.15)), '\N{DEGREE SIGN}'"C")
                print("Humidity :", x['humidity'], "%")
                print("Pressure :", x['pressure'], "hPa")
                print("Located at ", x1['lon'], "longitude and ", x1['lat'], "latitude")
            continue
        elif "what is the time now" in Query:
            hour =datetime.datetime.now().hour
            speak(hour)
            speak("hours")
            min=datetime.datetime.now().minute
            print(hour, "Hrs", min, "minutes")
            speak(min)
            speak("minutes")
            continue
        elif "tell me today's date" in Query:
            date=datetime.date.today()
            speak(date)
            print("Today's date :",date)
            continue
        elif "from playlist" in Query:
            speak("Which song do you want to hear?")
            gaana_search = recognise().lower()
            speak("Playing " + gaana_search)
            webbrowser.open("https://gaana.com/search/" + gaana_search)
            continue
        elif "play movie" in Query:
            speak("Which movie do you want to play?")
            movie = recognise().lower()
            speak("Playing " + movie)
            startfile("movie path (sample path - E:\\movies\\" + movie + ".mkv")
            continue
        elif "from map" in Query:
            speak("Which place do you want to search from maps?")
            map_search = recognise().lower()
            webbrowser.open("https://www.google.com/maps/place/" + map_search)
            continue
        elif "speed test" in Query:
            speak("Checking internet speed")
            speed = speedtest.Speedtest()
            download = speed.download()
            upload = speed.upload()
            print("Download speed : ", download/1000000,"Mbps")
            print("Upload speed : ", upload/1000000,"Mbps")
            continue
        elif "from windows" in Query:
            speak("Which app do you want to open?")
            app_name = recognise().lower()
            startfile("enter your desktop path (sample path - c:\\users\\<name>\\desktop)" + app_name)
        elif "tata" in Query:
            speak("Bye. See you soon again")
            print("Bye. See you soon again")
            exit()
def recognise():
    s=sr.Recognizer()
    with sr.Microphone() as input:
        print("Listening.......")
        audio = s.listen(input)
        try:
            print("Recognising....")
            query=s.recognize_google(audio,language='en-in')
        except Exception :
            print("Can you say that again ")
            return "none"
        return query
if __name__ =='__main__':
    while(True):
        if(invokeVision()):
            break;
    getQuery()
