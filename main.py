import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import calendar
import smtplib
import math
from geopy.geocoders import Nominatim

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
geolocator = Nominatim(user_agent="geoapiExercises")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'calculate' in command:
        # Extracting the mathematical expression from the command
        expression = command.replace('calculate', '')
        try:
            result = eval(expression)
            talk('The result is ' + str(result))
        except Exception as e:
            talk('Sorry, I could not calculate that.')
    elif 'calendar' in command:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        talk('Here is your calendar:')
        cal = calendar.month(year, month)
        talk(cal)
    elif 'send email' in command:
        # Add your email sending functionality here
        # Make sure to configure SMTP server and provide email credentials
        pass
    elif 'solve' in command:
        # Extracting the math problem from the command
        problem = command.replace('solve', '')
        try:
            solution = eval(problem)
            talk('The solution is ' + str(solution))
        except Exception as e:
            talk('Sorry, I could not solve that problem.')
    elif 'reminder' in command or 'alarm' in command:
        # Implement reminder/alarm functionality here
        pass
    elif 'where am i' in command:
        try:
            location = geolocator.geocode("me")
            talk("You are in " + location.address)
        except Exception as e:
            talk("Sorry, I could not determine your location.")
    else:
        talk('Please say the command again.')


while True:
    run_alexa()