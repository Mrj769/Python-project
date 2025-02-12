import os
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary

# Set your Gemini API key
genai.configure(api_key="Your_API_Key")  # Replace with your actual Gemini API key

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech rate for clarity

# Function to listen to user input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Speech Recognition Error: {e}")
        return ""

# Function to get response from Gemini API
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API error: {str(e)}"

# Function to speak the response
def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to process commands
def process(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak("Sorry, I couldn't find that song.")
    elif "bye" in c.lower():
        speak("Goodbye sir, have a great day!")
    else:
        # Call Gemini API for an AI response if no predefined command is matched
        ai_response = get_gemini_response(c)
        speak(ai_response)

# Main function to run the program
def main():
    print("Jarvis Activated! Say 'exit' to stop.")
    speak("Hello sir, what's on your mind?")
    
    while True:
        query = listen().lower()
        
        if not query:
            continue
        
        if "exit" in query:
            speak("Goodbye! Please come back soon.")
            break
        
        if query == "jarvis":
            speak("Yes sir, Jarvis at your service. What can I help you with?")
        else:
            # Process the command or get AI response
            process(query)

if __name__ == "__main__":
    main()
