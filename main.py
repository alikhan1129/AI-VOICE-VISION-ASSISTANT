import time
from core.shared import engine
from core.voice import listen, respond, greet_user
from core.wakeword import detect_wake_word


greet_user()

while True:
    try:
        if detect_wake_word():
            engine.say("I'm listening.")
            engine.runAndWait()
            user_input = listen()

            if user_input in ["good bye", "exit"]:
                print("Goodbye!")
                engine.say("Goodbye!")
                engine.runAndWait()
                break

            elif user_input:
                respond(user_input)

        time.sleep(1)

    except KeyboardInterrupt:
        print("Interrupted by user")
        engine.say("Goodbye!")
        engine.runAndWait()
        break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        engine.say("An error occurred. Please try again.")
        engine.runAndWait()
        time.sleep(1)

engine.stop()
