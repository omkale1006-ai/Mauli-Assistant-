import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import datetime
import pyjokes

# Assistant name
assistant_name = "Mauli"

# Text-to-speech engine setup
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Greeting function
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk(f"Good morning! I am your assistant {assistant_name}.")
    elif 12 <= hour < 18:
        talk(f"Good afternoon! I am your assistant {assistant_name}.")
    else:
        talk(f"Good evening! I am your assistant {assistant_name}.")

    talk("Please say your command.")

# Voice input capture function 
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        voice = listener.listen(source)

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said:", command)
    except:
        talk("Sorry, I didn't understand.")
        return ""

    return command

# Process and act on command
def run_assistant():
    command = take_command()

    if "open youtube" in command:
        talk("Opening YouTube")
        pywhatkit.playonyt("open youtube")

    elif "play song" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "search" in command:
        search = command.replace("search", "")
        talk(f"Searching {search}")
        pywhatkit.search(search)

    elif "open excel" in command:
        file_path = "C:\\Users\\YourUsername\\Documents\\example.xlsx"  # Change to your file path
        try:
            os.startfile(file_path)
            talk("Opening Excel file")
        except Exception as e:
            talk("Sorry, I couldn't open the Excel file.")
            print(e)

    elif "what is time" in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {current_time}")
    
    elif "what is todays date" in command:
        today = datetime.datetime.now().strftime('%A, %d %B %Y')
        talk(f"Today is {today}")

    elif "give one joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif "exit" in command or "stop" in command:
        talk(f"Goodbye! {assistant_name} is signing off.")
        exit()

    else:
        talk(f"Sorry, {assistant_name} doesn't understand this command.")

# Main loop
greet_user()  # 👈 Mauli will greet at start
while True:
    run_assistant()
