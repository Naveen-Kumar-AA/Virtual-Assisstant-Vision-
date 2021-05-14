import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from tkinter import *
import requests
from os import startfile
import speedtest
from tkinter import simpledialog


def get_input():
    global keyboard_input
    keyboard_input = (simpledialog.askstring("Get input", "Ask me something."))
    get_keyboard_input(keyboard_input)

def use_keyboard():
    global keyboard_input
    keyboard_input = (simpledialog.askstring("Get input", "Ask me something."))
    return keyboard_input

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



def getQuery():
    while(True):
        Query=recognise().lower()
        if "hello" in Query:
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
            apiKey = "b8d8d009a677db24d890aae925df992e"
            url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Enter your city name : ")
            cityName = recognise().lower()
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
            startfile("E:\\Movies\\" + movie + ".mkv")
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
            startfile("C:\\Users\\Naveen Kumar\\Desktop\\" + app_name)
        elif "text mode" in Query:
            speak("Switching to text mode. Type in your keyboard.")
            return get_input()

        elif "tata" in Query:
            speak("Bye. See you soon again")
            print("Bye. See you soon again")
            exit()



def get_keyboard_input(keyboardInput):
    Query=keyboardInput
    while(True):

        if "hello" in Query:
            Greet()
        elif "open google" in Query:
            speak("What do you want to search from google?")
            google_search = use_keyboard()
            speak("searching" + google_search)
            webbrowser.open("https://www.google.com/search?q=" + google_search)

        elif "open youtube" in Query:
            speak("WHat do you want to search from youtube")
            yt_search = use_keyboard()
            speak("seearching" + yt_search)
            webbrowser.open("https://www.youtube.com/results?search_query=" + yt_search)

        elif "show me the latest news around the world" in Query:
            speak("fetching latest news")
            webbrowser.open("https://www.thehindu.com/")
            speak("Here are some headlines from  the  hindu")

        elif "weather" in Query:
            apiKey = "b8d8d009a677db24d890aae925df992e"
            url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Enter your city name : ")
            cityName = use_keyboard()
            fullUrl = url + "appid=" + apiKey + "&q=" + cityName
            output = requests.get(fullUrl)
            temp = output.json()
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

        elif "what is the time now" in Query:
            hour = datetime.datetime.now().hour
            speak(hour)
            speak("hours")
            min = datetime.datetime.now().minute
            print(hour, "Hrs", min, "minutes")
            speak(min)
            speak("minutes")

        elif "tell me today's date" in Query:
            date = datetime.date.today()
            speak(date)
            print("Today's date :", date)

        elif "from playlist" in Query:
            speak("Which song do you want to hear?")
            gaana_search = use_keyboard()
            speak("Playing " + gaana_search)
            webbrowser.open("https://gaana.com/search/" + gaana_search)

        elif "play movie" in Query:
            speak("Which movie do you want to play?")
            movie = use_keyboard()
            speak("Playing " + movie)
            startfile("E:\\Movies\\" + movie + ".mkv")

        elif "from map" in Query:
            speak("Which place do you want to search from maps?")
            map_search = use_keyboard()
            webbrowser.open("https://www.google.com/maps/place/" + map_search)

        elif "speed test" in Query:
            speak("Checking internet speed")
            speed = speedtest.Speedtest()
            download = speed.download()
            upload = speed.upload()
            print("Download speed : ", download / 1000000, "Mbps")
            print("Upload speed : ", upload / 1000000, "Mbps")

        elif "from windows" in Query:
            speak("Which app do you want to open?")
            app_name = use_keyboard()
            startfile("C:\\Users\\Naveen Kumar\\Desktop\\" + app_name)
        elif "voice mode" in Query:
            speak("Switching to voice mode. Speak something")
            getQuery()
        elif "tata" in Query:
            speak("Bye. See you soon again")
            print("Bye. See you soon again")

            exit()
        Query = use_keyboard()


if __name__ =='__main__':
    vision = Tk()
    vision.title("Vision")
    vision.iconbitmap("vision icon.ico")
    #while(True):
    #   if(invokeVision()):
    #       break;
    #getQuery()

    #button1 = Button(vision, text="vision")
    #button1.bind("<Button-1>", getQuery)
    #button1.pack()
    global keyboard_input
    keyboard_input=""

    frame = Frame(vision,width=650,height=250)
    mic_button = PhotoImage(file = "mic.png")
    keyboard_button = PhotoImage(file = "keyboard.png")
    button1 = Button(frame, image = mic_button, command=getQuery)
    button2 = Button(frame, image = keyboard_button, command=get_input)
    button1.pack(side=LEFT)
    button2.pack(side=RIGHT)
    frame.pack(side=BOTTOM)
    bg_file=PhotoImage(file="vision.png")
    bg_label=Label(vision,image=bg_file)
    bg_label.pack()


    vision.geometry("579x586")
    vision.mainloop()
