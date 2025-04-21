import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

# Initialize the speech engine
engine = pyttsx3.init('sapi5')  # Use 'sapi5' for Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first voice

def speak(audio):
    """Speaks the audio passed as argument."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greets the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you?")

def takeCommand():
    """Listens for user input via microphone and returns the query as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause time in seconds after a phrase
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    return query

def sendEmail(to, content):
    """Sends an email to the specified recipient with the given content.
    You'll need to configure your email settings (less secure app access might be needed).
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Replace with your actual email and password (consider using environment variables)
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on user query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'  # Replace with your music directory
            songs = os.listdir(music_dir)
            if songs:
                random_song = random.choice(songs)
                os.startfile(os.path.join(music_dir, random_song))
            else:
                speak("No music files found in the specified directory.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Replace with your VS Code path
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("To whom should I send?")
                to = input("Enter recipient's email: ")
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I was unable to send the email.")

        elif 'quit' in query or 'exit' in query or 'bye' in query:
            speak("Goodbye!")
            break