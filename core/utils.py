import os
import webbrowser
import subprocess
import datetime
from core.shared import engine, memories

def remember(text):
    memories.append(text)
    engine.say("I have remembered that.")
    engine.runAndWait()

def recall_memories():
    if memories:
        for memory in memories:
            print("Memory:", memory)
            engine.say(memory)
    else:
        engine.say("I have nothing to recall.")
    engine.runAndWait()

def search_in_browser(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    engine.say(f"Searching {query} in browser.")
    engine.runAndWait()

def search_file(keyword):
    found_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if keyword.lower() in file.lower():
                found_files.append(os.path.join(root, file))
    if found_files:
        for file in found_files:
            print("Found file:", file)
            engine.say(f"Found file {file}")
    else:
        engine.say("No files found with that keyword.")
    engine.runAndWait()

def open_application(text):
    try:
        app_name = text.replace("open", "").strip()
        subprocess.Popen(["start", app_name], shell=True)
        engine.say(f"Opening {app_name}.")
    except Exception as e:
        engine.say(f"Error opening application: {e}")

def tell_date():
    today = datetime.date.today()
    date_text = today.strftime("%B %d, %Y")
    print("Today's date is:", date_text)
    engine.say(f"Today's date is {date_text}.")

def tell_schedule():
    try:
        with open("schedule.txt", "r") as file:
            schedule = file.read()
            print("Your schedule for today is:", schedule)
            engine.say(f"Your schedule for today is: {schedule}")
    except FileNotFoundError:
        engine.say("Sorry, I couldn't find your schedule.")
