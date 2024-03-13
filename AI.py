import pyttsx3
import speech_recognition as sr
import datetime
import time
import openai
import winsound
import sys
import cv2
import os
import pywhatkit
import pyautogui
import webbrowser
import urllib.parse
import requests
import threading
import numpy as np
import geocoder
from bs4 import BeautifulSoup
import instaloader
from pygame import mixer
from email.mime.multipart import MIMEMultipart, MIMEBase
from requests import get
import pyjokes
import pygetwindow as gw
from VolumeHandControl import volume

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
        TALKING = True
    engine.say(audio)
    print(audio)
    engine.runAndWait()

OPENAI_KEY = "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"

# Set OpenAI API key
openai.api_key = OPENAI_KEY

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message
messages =[{"role": "user", "content": "Please act like JARVIS from Iron man "}]

def close_window_by_title(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)
        if window:
            window[0].close()
            return True
        else:
            print("Window with title '{}' not found.".format(window_title))
            return False
    except Exception as e:
        print("Error:", e)
        return False

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

def encryption_decryption():
    speak("Initiating encryption and decryption module.")
    # Example: Encrypt and decrypt a message
    speak("sir Enter the message you would like to encrypt")
    message = input("your message here: ")
    key = 3  # Example key
    encrypted_message = ''.join([chr(ord(char) + key) for char in message])
    speak("let me just a second")
    time.sleep(2)
    speak("Message encrypted.")
    print("Encrypted message:", encrypted_message)
    time.sleep(3)
    speak("sir do you want me to decrypt the message for you")
    query = takeCommand().lower()
    if "yes" in query:
        speak("okay sir just a second")
        time.sleep(1)
        decrypted_message = ''.join([chr(ord(char) - key) for char in encrypted_message])
        speak("Message decrypted.")
        print("Decrypted message:", decrypted_message)
        speak("Encryption and decryption module deactivated.")
    else :
        speak("alright, you are the boss")
        pass

def get_date():
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%A, %B %d, %Y')}")

def open_new_tab():
    # Function to open a new tab in Edge
    pyautogui.hotkey("ctrl", "t")
    speak("New tab has been opened, sir.")

def close_tab():
    # Function to close the current tab in Edge
    pyautogui.hotkey("ctrl", "w")
    speak("The current tab has been closed, sir.")

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def ReadyChirp1():
    winsound.Beep(600,300)
def ReadyChirp2():
    winsound.Beep(500,300)
camera_thread = None
def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def close_camera():
    cv2.destroyAllWindows()

def volume_up():
    speak("on my ability")
    time.sleep(1)
    pyautogui.press('volumeup')
    speak("Done sir. the volume is now settled up")
    

def volume_down():
    speak("As you wish ")
    time.sleep(1)
    pyautogui.press('volumedown')
    speak("Done sir. the volume is now settled down")

def mute():
    speak("you are the boss")
    time.sleep(1)
    pyautogui.press('volumemute')
    speak("Done sir. the volume is now muted")
    

def adjust_volume(query):
    if 'up' in query:
        volume_up()
    elif 'down' in query:
        volume_down()
    elif 'mute' in query:
        mute()

def takeCommand():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source2:
                ReadyChirp1()
                r.adjust_for_ambient_noise(source2, duration = 0.2)
                print( "Listening....")
                audio2 = r.listen(source2)
                # ReadyChirp2()
                Mytext = r.recognize_google(audio2)
                
                
                return Mytext
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Unknown error occurred")

def wish():
    speak("Initialization of the system")
    time.sleep(2)
            
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 12:
        speak("good morning sir")
    elif 12 < hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("How can i help you today sir")
    

def start():
    wish()
    # volume_thread = threading.Thread(target=start_volume_adjustment)
    global camera_thread 
    while True:
        text = takeCommand()
        messages.append({"role": "user", "content": text})
        response = send_to_chatGPT(messages)
        speak(response)
        print(response)
        query = takeCommand().lower()
        
        if "sleep now" in query:
            speak("Going to sleep. Wake me up when you need assistance.")
            sys.exit()
        
        elif "change password" in query:
            speak("what is the new password sir")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"your new password is {new_pw}")
        
        elif "new tab" in query:
            speak("As you wish ")
            open_new_tab()
        elif "close tab" in query:
            
            close_tab()
        
        elif "game" in query:
            from game import game_play
            game_play()
        
        elif "open stackoverflow" in query:
            speak(" okay sir,searching for the website ")
            webbrowser.open("www.stackoverflow.com")
            speak("successfully found stackoverflow sir")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif " photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    break
        
        elif "open Tiktok" in query:
            speak ("trying to open tiktok for you sir")
            webbrowser.open("www.tiktok.com")
            speak("done sir")
        
        elif "schedule my day" in query:
            tasks = []
            speak("Do you want to clear old tasks sir(Plz speak YES or NO)")
            response = takeCommand().lower()
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
            location = takeCommand().lower()
            search_google_maps(location)
            
        elif "zoom in" in query:
            speak("seem your eyes is probably hurting, if so, you must see a doctor")
            if "my eyes are not" or "do not have" or "my eyes aren't" or "doesnt have " or "dont have" or "does not have" or "no" or "never" or "nah" in query:
                speak("Alrightttt, i was just checking You")
            else:
                speak("i see, im sorry to hear that")
            speak("just a second")
            time.sleep(1)
            pyautogui.hotkey('ctrl', '+')
            speak("Zoomed in.")
            
        elif "zoom out" in query:
            speak("here we go")
            time.sleep(1)
            pyautogui.hotkey('ctrl', '-')
            speak("Zoomed out.")

        elif 'volume' in query:
            speak("Alright, I'm listening to you...")
            speak("Just tell me to set up the volume by saying 'up', set down the volume by saying 'down', or mute the volume by saying 'mute'")
            time.sleep(10)  # Delay for 2 seconds to allow the user to speak after the message
            adjust_volume(query)
        
        elif "encrypt" in query:
            speak("As you wish")
            encryption_decryption()
        
        elif 'date' in query or 'today' in query:
            get_date()

        elif "open google" in query:
            speak("opening google ..")
            epath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(epath)
            speak("Google opened")
            speak("sir, what should i search from google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak(" its Done")
        elif "close google" in query:
            speak("As you wish ")
            window_title = "msedge.exe"
            close_window_by_title(window_title)
            
        elif "open command prompt" in query:
            speak("opening command prompt for you")
            os.system("start cmd")
            speak("cmd opened")
        elif "close command prompt" in query:
            speak("you are the boss")
            window_title = "cmd"
            close_window_by_title(window_title)
        if "open camera" in query:
            if camera_thread is None or not camera_thread.is_alive():
                camera_thread = threading.Thread(target=open_camera)
                camera_thread.start()
        elif "close camera" in query:
            close_camera()
        
            
        elif 'play' in query:
            speak("i see that you are in your mood today")
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            
        elif "ip address" in query:
            speak   ("okay sir, analyzing your ip address")
            ip = get('https://api.ipify.org').text
            speak("ip address found")
            speak(f"your IP address is {ip}")
            

            # detect_hand_claps()
        
        elif "open youtube" in query:
            speak("Okay sir, opening youtube")
            webbrowser.open("www.youtube.com")
            speak("Opened youtube for you sir")
            speak("Sir, what should I search on youtube?")
            yt_query = takeCommand().lower()
            search_youtube(yt_query)
            speak("Done sir")
        
        elif "open linkedin" in query:
            speak("opening linkedin for you sir")
            webbrowser.open("www.linkedIn.com")
            speak("task done sir")
            
        elif ' the time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak('current time is ' + current_time)
            
        elif "restart the system" in query:
            speak("System is restarting. Please wait.")
            os.system("shutdown /r /t 1")
            
        elif "shut down the system" in query:
            speak("Shutting down the system. Goodbye!")
            os.system("shutdown /s /t 1")
            
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
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
                
        elif "instagram profile" in query:
            speak("sir please enter the username correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account?")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder")
            else:
                speak ("as you wish sir")
                
        elif " screenshot" in query:
            speak("sir, please tell me the name for this screenshot")
            name = takeCommand().lower()
            speak("please sir, hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder")
            
        elif "remember that" in query:
            rememberMessage = query.replace("remember that","")
            speak("okay sir. You told " +rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()
        
        elif "activate how to do mod" in query:
            from pywikihow import search_wikihow
            speak("How to do mod is activated sir, please tell me what you want to know")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        
        elif "what did you remember" in query:
            remember = open("Remember.txt","r")
            speak("you told me "+ remember.read())
        
        elif "internet speed" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have{dl} bit per second downloading speed and {up} bit per second uploading speed")
            
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")
        
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
                
            elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

if __name__ == "__main__":
    while True:
        permission= takeCommand()
        if "wake up" in permission:
            start()