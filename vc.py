import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def handle_commands(query):
    if "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open google" in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open notepad" in query:
        os.system("notepad")
        speak("Opening Notepad")
    elif "exit" in query or "stop" in query:
        speak("Goodbye Ashi!")
        exit()
    else:
        speak("Sorry, I can't do that yet.")

def main():
    speak("Hello Ashi, I'm your voice assistant. How can I help you?")
    while True:
        query = listen()
        if query:
            handle_commands(query)

main()