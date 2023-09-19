import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

listener = sr.Recognizer()
alexa = pyttsx3.init()

def talk(talk):
    alexa.say(talk)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # talk("hey boss how are you ")
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except : pass
    return command

def run_alexa():
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M')
        print(time)
        talk(time)

    elif 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif "you are done now" in command:
        talk("okay boss im going now")
        print("okay boss im going now")
        return True

while True:
    should_exit = run_alexa()
    if should_exit:
        break