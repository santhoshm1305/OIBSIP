import speech_recognition as sr
import pyttsx3
from datetime import datetime
from googlesearch import search


# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        print("Attempting to initialize microphone...")
        with mic as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source, timeout=10)  # Added timeout
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not hear that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""
    except OSError as e:
        print(f"OS Error: {e}")
        return ""
    except KeyboardInterrupt:
        print("Process interrupted by user.")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        today = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        try:
            results = list(search(query, num_results=3))
            speak(f"Here are the top results for {query}:")
            for result in results:
                speak(result)
        except Exception as e:
            speak(f"An error occurred while searching: {e}")
    else:
        speak("I didn't understand that command. Please try again.")

def main():
    speak("Voice assistant is ready.")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
