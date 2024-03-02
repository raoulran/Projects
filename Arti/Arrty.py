import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit 
import wikipedia
import webbrowser
import smtplib
import sys
import time
import urllib.parse
import pyjokes
import pyautogui
import time
import requests
import cv2
import numpy as np
from plyer import notification
import PyPDF2
import geocoder
from bs4 import BeautifulSoup
import instaloader
from pygame import mixer
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email import message
from requests import get

from INTRO import play_gif
play_gif

for i  in range(3):
    a = input("Enter Password to open Arti: ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if(a==pw):
        print("WELCOME SIR! PLZ SPEAK [WAKE UP TO LOAD ME UP")
        break
    elif(i==2 and a!=pw):
        exit()
        
    elif(a!=pw):
        print("try again")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=0, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        print("Can you repeat sir...")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('raoulran2@gmail.com', 'guow yvtr cbhj ecza')
    server.sendmail('raoulran2@gmail.com', to, content)
    server.close()

def search_google_maps(query):
    base_url = "https://www.google.com/maps/search/?api=1"
    query_string = urllib.parse.urlencode({"query": query})
    search_url = f"{base_url}&{query_string}"
    webbrowser.open(search_url)
    speak(f"Here is the location for {query} on Google Maps.")

def search_youtube(query):
    # Find the YouTube search bar on the screen
    search_box_location = pyautogui.locateOnScreen('youtube_search.png', confidence=0.8)
    if search_box_location:
        # Click on the search bar
        pyautogui.click(search_box_location)
        # Type the query
        pyautogui.write(query)
        pyautogui.press('enter')
        speak(f"Here are the search results for {query} on YouTube.")
    else:
        speak("Sorry, I couldn't find the YouTube search bar.")

def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak("good morning sir")
    elif 12 < hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("i am Arti, please tell me how I can help you")

def encryption_decryption():
    speak("Initiating encryption and decryption module.")
    # Example: Encrypt and decrypt a message
    speak("sir Enter the message you would like to encrypt")
    message = input("your message here: ")
    key = 3  # Example key
    encrypted_message = ''.join([chr(ord(char) + key) for char in message])
    speak("Message encrypted.")
    print("Encrypted message:", encrypted_message)
    time.sleep(3)
    speak("sir do you want me to decrypt the message for you")
    query = take_command().lower()
    if "yes" in query:
        speak("okay sir just a second")
        time.sleep(1)
        decrypted_message = ''.join([chr(ord(char) - key) for char in encrypted_message])
        speak("Message decrypted.")
        print("Decrypted message:", decrypted_message)
        speak("Encryption and decryption module deactivated.")

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=eb05bdda40074d76b7d0dcb948fd7cda"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"todays {day[i]} news is: {head[i]}")

def open_new_tab():
    # Function to open a new tab in Edge
    pyautogui.hotkey("ctrl", "t")
    speak("New tab has been opened, sir.")

def close_tab():
    # Function to close the current tab in Edge
    pyautogui.hotkey("ctrl", "w")
    speak("The current tab has been closed, sir.")

def pdf_reader():
    book = open('py3.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number I have to read")
    pg = int(input("please enter the page number here: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def get_date():
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%A, %B %d, %Y')}")

def start():
    wish()
    while True:
        query = take_command().lower()

        if "sleep now" in query:
            speak("Going to sleep. Wake me up when you need assistance.")
            sys.exit()

        if "wake up" in query:
            speak("I'm awake now. How can I assist you?")

        elif "change password" in query:
            speak("what is the new password sir")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"your new password is {new_pw}")

        elif "schedule my day" in query:
            tasks = []
            speak("Do you want to clear old tasks sir(Plz speak YES or NO)")
            response = take_command().lower()
            if "yes" in response:
                with open("tasks.txt", "w") as file:
                    file.write(f"")
                    file.close()
                    no_tasks = int(input("Enter the number of tasks sir:- "))
                    i = 0
                    for i in range(no_tasks):
                        tasks.append(input("Enter the task:- "))
                        file = open("tasks.txt","a")
                        file.write(f"{i}. {tasks[i]}\n")
                        file.close()
            elif "no" in response:
                i = 0
                no_tasks = int(input("Enter the number of tasks sir:- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task:- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()

        elif "search in google maps" in query:
            speak("Sure, sir. What location would you like to search for?")
            location = take_command().lower()
            search_google_maps(location)

        elif "zoom in" in query:
            pyautogui.hotkey('ctrl', '+')
            speak("Zoomed in.")

        elif "zoom out" in query:
            pyautogui.hotkey('ctrl', '-')
            speak("Zoomed out.")

        elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

        elif "game" in query:
            from game import game_play
            game_play()

        elif " current temperature" in query:
            search = "temperature Cheltenham Road, Gloucester, England"
            url =f"https://www.bing.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            
            temp_element = data.find("div", class_="BNeawe")
            if temp_element is not None:
                temp = temp_element.text
                speak(f"Current {search} is {temp}")
            else:
                speak(f"Sorry, I couldn't find the  {search}.")

        elif " current weather" in query:
            search = "weather Cheltenham Road, Gloucester, England"
            url =f"https://www.bing.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp_element = data.find("div", class_="BNeawe")
            if temp_element is not None:
                temp = temp_element.text
                speak(f"Current {search} is {temp}")
            else:
                speak(f"Sorry, I couldn't find the  {search}.")

        elif "open google" in query:
            speak("opening google sir..")
            epath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(epath)
            speak("Google opened")
            speak("sir, what should i search from google")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")
            speak("Done sir")

        elif "open command prompt" in query:
            speak("opening command prompt sir")
            os.system("start cmd")
            speak("cmd opened")

        elif "open notepad" in query:
            speak("Opening Notepad, sir.")
            os.system("start notepad")
            speak("Notepad has been opened.")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif "pause" in query:
            pyautogui.press("k")
            speak("video played sir")

        elif "ip address" in query:
            speak   ("okay sir, analyzing your ip address")
            ip = get('https://api.ipify.org').text
            speak("ip address found")
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("A moment sir...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "encrypt decrypt" in query:
            encryption_decryption()

        elif "open youtube" in query:
            speak("Okay sir, opening youtube")
            webbrowser.open("www.youtube.com")
            speak("Opened youtube for you sir")
            speak("Sir, what should I search on youtube?")
            yt_query = take_command().lower()
            search_youtube(yt_query)
            speak("Done sir")

        elif "open stackoverflow" in query:
            speak(" okay sir,searching for the website ")
            webbrowser.open("www.stackoverflow.com")
            speak("successfully found stackoverflow sir")

        elif "open Tiktok" in query:
            speak ("trying to open tiktok for you sir")
            webbrowser.open("www.tiktok.com")
            speak("done sir")

        elif "open linkedin" in query:
            speak("opening linkedin for you sir")
            webbrowser.open("www.linkedIn.com")
            speak("task done sir")

        elif "email" in query:
            speak("what should i say?")
            query = take_command().lower()
            if "send a file" in query:
                email = 'raoulran2@gmail.com'
                password = 'Raoulran2006'
                send_to_email = 'fkaminy@gmail.com'
                speak("okay sir, what is the subject for this email")
                query = take_command().lower()
                subject = query
                speak("and sir, what is the message for this email")
                query2 = take_command().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here: ")

                speak("please wait, i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('content-Disposition', "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been successfully sent to your grand-ma sir")

            else:
                email = 'raoulran2@gmail.com'
                password = 'Raoulran2006'
                send_to_email = 'carine.nouaketstudy@outlook.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("email has been successfully sent to your mum sir")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif ' the time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak('current time is ' + current_time)

        elif 'date' in query or 'today' in query:
            get_date()

        elif "hello" in query or "hi" in query:
            speak("Nice to meet you again sir, do you have any request sir")

        elif "how are you" in query:
            speak("i am good sir. what about you sir")

        elif "see" in query:
            speak("i dont know sir i am a virtual assistant, i dont have eyes to see")
            speak("the only tip that i can give you sir is to pay attention to details")

        elif "nice" in query:
            speak("Thank you sir, its always a pleasure to assist you ")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "restart the system" in query:
            speak("System is restarting. Please wait.")
            os.system("shutdown /r /t 1")  # /r is for restart, /t is for time delay (1 second delay here)

        elif "shut down the system" in query:
            speak("Shutting down the system. Goodbye!")
            os.system("shutdown /s /t 1")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "close" in query:
            speak("Closing the current window.")
            pyautogui.hotkey('alt', 'f4')

        elif "where i am" in query or "where we are" in query:
            speak("Wait sir, let me check.")
            try:
                g = geocoder.ip('me')
                location = g.geojson
                city = location['features'][0]['properties']['city']
                country = location['features'][0]['properties']['country']
                speak(f"Sir, I believe we are in {city} city, {country} country.")
            except Exception as e:
                speak("Sorry sir, I'm unable to determine our location at the moment.")

        elif "where is" in query:
            location_name = query.split("where is", 1)[1].strip()

            speak(f"Wait sir, let me check where {location_name} is.")
            try:
                g = geocoder.osm(location_name)
                location = g.geojson
                city = location['features'][0]['properties']['city']
                country = location['features'][0]['properties']['country']
                speak(f"Sir, {location_name} is located in {city} city, {country} country.")
            except Exception as e:
                speak(f"Sorry sir, I'm unable to determine the location of {location_name} at the moment.")

        elif "instagram profile" in query:
            speak("sir please enter the username correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account?")
            condition = take_command().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder")
            else:
                pass

        elif " screenshot" in query:
            speak("sir, please tell me the name for this screenshot")
            name = take_command().lower()
            speak("please sir, hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder")

        elif "read pdf" in query:
            pdf_reader()

        elif "activate how to do mod" in query:
            from pywikihow import search_wikihow
            speak("How to do mod is activated sir, please tell me what you want to know")
            how = take_command()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            speak("okay sir. You told " +rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()

        elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

        elif "what did you remember" in query:
            remember = open("Remember.txt","r")
            speak("you told me "+ remember.read())

        elif "volume up" in query:
            from Keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in query:
            from Keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()

        elif 'volume mute' in query:
            pyautogui.press("volumemute")
            speak("volume muted sir")

        elif "internet speed" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have{dl} bit per second downloading speed and {up} bit per second uploading speed")

        elif "translate" in query:
            from Translator import translategl
            query = query.replace("translate","")
            translategl(query)
        
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")
        
        elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
        
        elif "how much power left" in query or "how much much power we have" in query or "battery" in query:
            speak("let me check sir")
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir the system has {percentage} percent battery")
            if percentage >=75:
                speak("we have enough power to continue our work sir")
            elif percentage>=40 and percentage<75:
                speak("we should connect the system to charging point to charge the battery sir")
            elif percentage>=15 and percentage<40:
                speak("we dont have enough power to work sir, please connect to charging")
            elif percentage<15:
                speak("we have very low power , the system will turn off soon. Please connect to charging sir")
        
        elif "hide folder"  in query:
            speak("sir please tell me you want to hide this folder or make it visible to everyone")
            condition = take_command().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all files in this folder are now hidden to everyone")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible for everyone")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")


if __name__ == "__main__":
    while True:
        permission= take_command()
        if "wake up" in permission:
            start()
