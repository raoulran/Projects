import pyttsx3
import speech_recognition as sr
import random

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
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}")
    except Exception as e:
        speak("Can you repeat sir...")
        return "None"
    return query

def game_play():
    speak(" SIR LETS PLAYYYY")
    print("LETS PLAYYYYYYYY")
    i = 0
    Me_score = 0
    com_score = 0
    
    while (i<5):
        choose = ("rock", "paper", "scissors")
        com_choose = random.choice(choose)
        query = take_command(). lower()
        if (query == "rock" or query =="stone"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
            elif(com_choose == "paper"):
                speak("paper")
                com_score += 1
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
            else:
                speak("Scissors")
                Me_score +=1
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
                
        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
            elif(com_choose == "paper"):
                speak("paper")
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
            else:
                speak("Scissors")
                com_score +=1
                print(f"Score :- Me :- {Me_score} :com : {com_score}")        
                
        elif (query == "scissors") or (query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                com_score += 1
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
            elif(com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
            else:
                speak("Scissors")
                print(f"Score :- Me :- {Me_score} :com : {com_score}")
        i += 1
    print(f"FINAL SCORE :Me :- {Me_score} : ARTI :- {com_score}")