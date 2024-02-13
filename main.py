import win32com.client
import speech_recognition as sr
import webbrowser as wb
import openai
import pygame
import subprocess
import datetime
import os
from config import apikey
 
speaker =win32com.client.Dispatch("SAPI.SpVoice")


# reseearch on webdriver for loging into any social media accounts
chatstr=""

def chat(s):
    global chatstr
    openai.api_key = apikey

    chatstr+=f'User said:{s}\n EchoMind said:'
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=chatstr,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    try:
        speaker.speak((response["choices"][0]["text"]))
        chatstr += f'{response["choices"][0]["text"]}\n'
        return response["choices"][0]["text"]
    except Exception as e:
        print("some error occured",e)

# OpenAi integeration model:-Davinci-003
def ai(prompt):
    openai.api_key = apikey

    text=prompt
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    try:
        # print(response["choices"][0]["text"])
        text+=response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdiir("Openai")
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt","w") as f:
            f.write(text)
    except Exception as e:
        print("some error occured",e)
    
#understanding the speech through microphone
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"things said {query}")
            return query
        except Exception as e:
            return ("Some error occured can you please say it again")
    
text="ai"
speaker.speak(text)

while 1:
    print("please enter the text to speak")
    s=takecommand()
    # speaker.speak(s)
    # for opening different websites through assistant
    websites=[["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],["wikipedia","https://www.wikipedia.org/"],["hotstar homepage","https://www.hotstar.com/in/home"]]
    for site in websites:
        if f"open {site[0]}" in s.lower():
            wb.open(site[1])
            speaker.speak(f"opening {site[0]} sir")
            print("listening...")
    musiclist=[["karan song","./music/Admirin'-You(PaglaSongs).mp3"],["dhundhala","./music/Dhundhala(PaglaSongs).mp3"],["heeriye","./music/Heeriye-Heeriye-Aa(PaglaSongs).mp3"],["hua main","./music/128-Hua Main - Animal 128 Kbps.mp3"],["soulmate","./music/Maybe-My-Soulmate-Died(PaglaSongs).mp3"],["pehle bhi main","./music/Pehle-Bhi-Main(PaglaSongs).mp3"]]
    for song in musiclist:
        if f"play {song[0]}" in s.lower():
            try:
                pygame.mixer.init()
                print(song[1])
                pygame.mixer.music.load(song[1])
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            except pygame.error as e:
                print(f"Error playing the music: {e}")

    if "what's the time" in s.lower():
        exactime=datetime.datetime.now().strftime("%H:%M:%S")
        speaker.speak(exactime)

    apps = [["edge", "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"],["chrome","C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"]]

    for app in apps:
        if f"launch {app[0]}" in s.lower():
            # Use 'runas' to execute the command with elevated privileges
            subprocess.Popen(app[1])

    if "using artificial intelligence".lower() in s.lower():
        ai(prompt=s)
    elif "quit".lower() in s.lower():
        exit()
    elif "reset chat".lower()  in s.lower():
        chatstr=""
    else:
        print("chatting...")
        chat(s)
