import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

#For Setting Voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#For Speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#For Wishing the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <12:
        pyttsx3.speak("Good Morning")
    elif hour>= 12 and hour<18:
        pyttsx3.speak("Good Afternoon")
    else:
        pyttsx3.speak("Good Evening")
    pyttsx3.speak("I am Jarvis, Please tell me how can I help you?")

#Takes microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

#For sending email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your email", "your password")
    server.sendmail("your email", to ,content)
    server.close()


if __name__ == "__main__":
    pyttsx3.speak("Hello Sir")  
    wishMe()
    while True:
        query = takeCommand()
        query.lower()

        #Logic For executing task based on query
        if 'Wikipedia' in query:
            pyttsx3.speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            pyttsx3.speak("According To Wikipedia")
            print(results)
            pyttsx3.speak(results)

        elif "open YouTube" in query:
            pyttsx3.speak("Launching YouTube") 
            webbrowser.open("www.youtube.com")

        elif "open Google" in query:
            pyttsx3.speak("Launching Google") 
            webbrowser.open("www.google.com")

        elif "open stack" in query:
            pyttsx3.speak("Opening stackoverflow") 
            webbrowser.open("www.stackoverflow.com")

        elif "play music" in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'quit' in query:
            pyttsx3.speak("Thanks For using")
            exit()
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%H:%S")
            speak("The Time is {0}".format(strTime))
            print(strTime)
        elif "open code" in query:
            pyttsx3.speak("Launching Code")
            os.system("code")

        elif "send email" in query:
            try:
                speak("What Should I say?")
                content = str(input("Type the E-mail here.."))
                to = "To Reciever's Email"
                sendEmail(to, content)
                speak("Email Has been sent!")
            except Exception as e:
                speak("Error, E-mail was not sent, please try again later...")

        