import speech_recognition as sr
import threading

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300  # fixed sensitivity (faster)
recognizer.dynamic_energy_threshold = False

voice_command = ""

def listen_in_background():

    global voice_command

    with sr.Microphone() as source:

        print("Voice listener started...")

        # Small calibration (only once)
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        while True:
            try:
                audio = recognizer.listen(
                    source,
                    timeout=0.5,          # wait max 0.5 sec
                    phrase_time_limit=1.5 # short speech window
                )

                text = recognizer.recognize_google(audio).lower()
                print("Voice heard:", text)

                if "help" in text or "doctor" in text or "water" in text:
                    voice_command = text

            except sr.WaitTimeoutError:
                pass
            except:
                pass


def start_voice_listener():
    thread = threading.Thread(target=listen_in_background, daemon=True)
    thread.start()