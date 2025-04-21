import datetime
import speech_recognition as sr # type: ignore
import pyttsx3
import webbrowser
import os
import wikipedia # type: ignore
import smtplib
import random
import getpass

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for female

# --- Helper Functions ---

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, your personal AI assistant. How can I help you, Lucky bhaiya?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Sorry, I didn't catch that.")
        return "none"
    return query

def send_email(to, content):
    sender_email = "your_email@gmail.com"
    sender_password = getpass.getpass("Enter your email password: ")  # Secure input
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        server.quit()
        speak("Email has been sent!")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I was unable to send the email.")

# --- Main Program ---

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if "none" in query:
            continue

        elif "search" in query:
            speak("Searching Wikipedia...")
            query = query.replace("search", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia,")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn’t find any results.")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\rajuk\\Music"  # Change this to your actual music folder
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, random.choice(songs)))
                else:
                    speak("No songs found in your music directory.")
            else:
                speak("Music directory not found.")

        elif "what time is it" in query:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_now}")

        elif "open code" in query:
            code_path = "C:\\Users\\rajuk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Adjust if needed
            if os.path.exists(code_path):
                os.startfile(code_path)
            else:
                speak("VS Code not found.")

        elif "send email" in query:
            try:
                to = input("Enter recipient's email: ")
                content = input("Enter the message: ")
                send_email(to, content)
            except Exception as e:
                print(e)
                speak("I couldn't send the email.")

        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't understand that. Try again.")
