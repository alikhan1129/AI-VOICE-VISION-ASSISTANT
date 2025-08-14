
import sounddevice as sd
from core.chat import query
from core.vision import capture_screen, screenshot_and_explain, read_text, identify_objects, describe_scene
from core.utils import remember, recall_memories, search_in_browser, search_file, open_application, tell_date, tell_schedule
from core.shared import engine
from core.security import is_secure_command, verify_password
import speech_recognition as sr


recognizer = sr.Recognizer()



def greet_user():
    greeting_text = "Hello! I am your AI assistant. How can I assist you today?"
    print("AI:", greeting_text)
    engine.say(greeting_text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source, timeout=10)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("User:", text)
        return text.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError as e:
        print(f"Error with speech recognition service: {e}")
        return None
    except Exception as e:
        print(f"Unknown error: {e}")
        return None



def respond(text):
    if is_secure_command(text):
        if not verify_password():
            engine.say("Access denied. Incorrect password.")
            engine.runAndWait()
            return
    if text in ["Sorry, I didn't catch that.", "No speech detected."]:
        engine.say(text)
    else:
        if "open" in text:
            open_application(text)
        elif "date" in text:
            tell_date()
        elif "schedule" in text:
            tell_schedule()
        elif "remember" in text:
            remember(text.replace("remember", "").strip())
        elif "recall" in text:
            recall_memories()
        elif "search in browser" in text:
            search_in_browser(text.replace("search in browser", "").strip())
        elif "search file" in text:
            search_file(text.replace("search file", "").strip())
        elif "capture screen" in text:
            capture_screen()
        elif "screenshot and explain" in text:
            screenshot_and_explain()
        elif "read text" in text:
            read_text()
        elif "identify objects" in text:
            identify_objects()
        elif "describe scene" in text:
            describe_scene()
        else:
            output = query(text)
            if output:
                print("Chatbot:", output)
                engine.say(output)
            else:
                engine.say("Sorry, there was a problem processing your request.")
    engine.runAndWait()

