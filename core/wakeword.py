import speech_recognition as sr

WAKE_WORD = "yo"

def detect_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Waiting for wake word...")
        try:
            audio = recognizer.listen(source, timeout=10)
            spoken = recognizer.recognize_google(audio).lower()
            print("Heard:", spoken)
            return WAKE_WORD in spoken
        except:
            return False
