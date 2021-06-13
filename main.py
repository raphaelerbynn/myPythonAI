import random

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import googlesearch

engine = pyttsx3.init()
r = sr.Recognizer()
# with sr.Microphone() as source:
#     print('Listening...')
#     r.pause_threshold = 2
#     audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio)
#         print(query)
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[0].id)
#
#         engine.say('Hi '+query+', Welcome')
#         engine.runAndWait()
#     except Exception as e:
#         print(e)
#         engine.say('Sorry I didn\'t hear you well...')
#         engine.runAndWait()


def speak(text):
    engine.setProperty('rate', 199)
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as mic:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(mic)

        try:
            print('Command captured')
            query = r.recognize_google(audio)
            print(query)

        except Exception as e:
            print(e)
            return None
        return query


def welcome_address():
    time = datetime.datetime.now().time().strftime('%I %M')
    hour = datetime.datetime.now().hour
    date = datetime.datetime.now().date().isoformat()
    print(time)
    if 6 <= hour < 12:
        greetings = 'Good morning, '
    elif 12 <= hour < 16:
        greetings = 'Good afternoon, '
    else:
        greetings = 'Good evening, '
    speak(
        """Hello """+greetings+"""boss. Today is """+date+""". The time is """+time+"""This is Mountain at your service... """
    )


def ask_of_health():
    health_questions = ['How do you do?', 'Hope you are fine?', 'You good?']
    ques = random.randint(0, len(health_questions)-1)
    # ques = 1
    print(len(health_questions))
    speak(health_questions[ques])

    query = take_command()
    try:
        if ques == 1 or ques == 2:
            answers = ['fine', 'blessed', 'good', 'fit', 'well', 'yeah', 'yes']
            if any(ans in query for ans in answers):
                if any(ans in query for ans in ['not', 'no', 'nope']):
                    speak('Get well soon')
                else:
                    speak('Thank God, This is all I can do for now')
            elif any(ans in query for ans in ['not', 'no', 'nope']):
                speak('Get well soon')
            else:
                speak('Wish I understand that!')

        else:
            if query == 'how do you do':
                speak('haha, Bless God')
            else:
                speak('haha, the answer should be how do you do.')

    except TypeError:
        speak('You did not talk')


def capabilities():
    while start:

        command = str(take_command()).lower()
        print(command)

        if "go away" in command or "offline" in command or "exit" in command:
            opt = ["Ok, I'm quitting now", "have a nice day, bye bye", "See you soon boss", "Nice being at your service, bye"]
            speak(opt[random.randint(0, len(opt)-1)])
            start = False

        elif "hey" == command or "mountain" == command:
            speak("yes boss...")

        elif "search" in command:
            try:
                speak("searching...")
                if "wikipedia" in command:
                    command = command.replace("wikipedia", "")
                if "on" in command:
                    command = command.replace("on", "")
                command = command.replace("search", "")
                print(command)
                result = wikipedia.summary(command, sentences=2)
                print(result)
                speak(result)

            except wikipedia.exceptions.WikipediaException as e:
                print(e)
                speak("i did not get you")



if __name__ == '__main__':
    welcome_address()
    ask_of_health()

    speak("how may I help you?")
    start = True
    while start:

        command = str(take_command()).lower()
        print(command)

        if "go away" in command or "offline" in command or "exit" in command:
            opt = ["Ok, I'm quitting now", "have a nice day, bye bye", "See you soon boss", "Nice being at your service, bye"]
            speak(opt[random.randint(0, len(opt)-1)])
            start = False

        elif "hey" == command or "mountain" == command:
            speak("yes boss...")

        elif "search" in command:
            try:
                speak("searching...")
                if "wikipedia" in command:
                    command = command.replace("wikipedia", "")
                if "on" in command:
                    command = command.replace("on", "")
                command = command.replace("search", "")
                print(command)
                result = wikipedia.summary(command, sentences=2)
                print(result)
                speak(result)

            except wikipedia.exceptions.WikipediaException as e:
                print(e)
                speak("i did not get you")

    take_command()
