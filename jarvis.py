import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

Recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def process(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "bye" in c.lower():
        speak("bye sir,have a good day")

if __name__ == "__main__":
    speak("hello sir say somethink")
    while True:
        r=sr.Recognizer()
    
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "robot"):
                speak("Yes sir,jarvis at your service,say what can i help you")
                with sr.Microphone() as source:
                    print("Jarvis is listening....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    process(command)
                    
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said")
        except sr.RequestError as e:
            print("Error; {0}".format(e))
