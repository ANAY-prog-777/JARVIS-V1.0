import datetime
import os




from ai_brain import generate_response


import speech_recognition as sr
import pyttsx3
import webbrowser

from ai_brain import generate_response

engine = pyttsx3.init()

def say(text):

    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            
        try:
            
            print("SPEAK YOUR COMMAND........")
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 0.6
            audio = r.listen(source)
            query = r.recognize_google(audio , language='en-in')
            print(F"USER SAID : {query}")
            return query
     
        except Exception as e:
            print("SAY THAT AGAIN PLEASE...., SORRRY FROM JARVIS")
            say("SAY THAT AGAIN PLEASE, SORRY FROM JARVIS")
            return "None"

say("JARVIS , AT YOUR TIPS SIR , HOW MAY I HELP YOU TODAY?")
while True:
    print("PROCESSING YOUR COMMAND")
    query = take_command()

    if query == "None":
        continue
# AM I COOKED CHAT
    command_executed = False

    sites = [['youtube', 'https://www.youtube.com/'],['google', 'https://www.google.com/'],['facebook', 'https://www.facebook.com/'],['instagram', 'https://www.instagram.com/'],['twitter', 'https://twitter.com/'] ,['hackclub', 'https://hackclub.com/'],['github', 'https://www.github.com/'], ['hack club', 'https://hackclub.com/'], ['linkedin', 'https://www.linkedin.com/'], ['gmail', 'https://mail.google.com/'], ['spotify', 'https://www.spotify.com/'], ['netflix', 'https://www.netflix.com/'], ['whatsapp', 'https://web.whatsapp.com/'], ['discord', 'https://discord.com/'], ['reddit', 'https://www.reddit.com/'], ['quora', 'https://www.quora.com/'], ['stack overflow', 'https://stackoverflow.com/']]
    for site in sites:
        if f'open {site[0]}'.lower() in query.lower():

            say(f'opening{site[0]}')
            webbrowser.open(site[1])

            # DD A FEATURE U WANT SPECIFICALLY:

    if 'time' in query:
        now = datetime.datetime.now()
        strfTime = now.strftime("%I %M %p")  
        say(f"SIR, THE TIME RIGHT NOW IS {strfTime}")
        print(f"--> THE TIME RIGHT NOW IS: {strfTime}")

    if 'open notepad'.lower() in query.lower():
        say("opening notepad")
        os.startfile("C:\\Windows\\System32\\notepad.exe")

        # THIS PART WAS THE HARDEST

    if not command_executed:
        print("Thinking...")
        ai_response = generate_response(query)
        print(f"JARVIS: {ai_response}")
    say(ai_response)