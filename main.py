from playsound import playsound
from threading import Thread, Event

import random
import keyboard
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib  #for sending email
import getpass
import os


engine = pyttsx3.init()
r = sr.Recognizer()


def speak(text):
    engine.setProperty('rate', 178)
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as mic:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(mic, duration=1)
        audio = r.listen(mic)

        try:
            print('Command captured')
            query = r.recognize_google(audio)
            print(query)

        except Exception as e:
            print(e)
            return None
        return query



def send_mail(to, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    speak("please enter your credentials")
    email = str(input("Enter email: "))
    pw = getpass.getpass("Enter password: ")
    server.login(email, pw)
    server.sendmail(email, to, msg)
    server.close()


def play_music():
    songs_dir = "C:\\Users\\MOUNTAIN\\Music"
    songs = os.listdir(songs_dir)
    for item in songs:
        if item.__contains__(".mp3"):
            pass
        else:
            songs.remove(item)

    os.startfile(os.path.join(songs_dir, songs[0]))

    # basedir = 'C:\Users\MOUNTAIN\Music'
    # songs_dir = []
    #
    # def search_music():
    #
    #     for s_dir in basedir:
    #         speak("searching")
    #         for r, d, f in os.walk(s_dir):
    #             # speak("searching")
    #             for files in f:
    #                 # speak("searching")
    #                 if files.__contains__('.mp3'):
    #                     songs_dir.append(os.path.join(r, files))
    #         if Event().is_set():
    #             break
    #
    # search_music()
    # action_thread = Thread(target=search_music)
    # action_thread.start()
    # action_thread.join(timeout=3)
    # Event().set()
    # speak("Done")
    #
    # songs = list(filter(lambda s: ("AppData" not in s), songs_dir))
    #
    # s_num = random.randint(0, len(songs)-1)
    # print(songs)
    # # playsound(songs_dir[s_num])
    #
    # pressed = True
    # while pressed:
    #     if keyboard.is_pressed("space"):
    #         pressed = False
    #     playsound(songs[s_num])




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
                    speak('Thank God')
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
        speak('You did not talk. No problem')


def capabilities(begin):
    while begin:

        command = str(take_command()).lower()
        # print(command)

        if "go away" in command or "offline" in command or "exit" in command:
            opt = ["Ok, I'm quitting now", "have a nice day, bye bye", "See you soon boss", "Nice being at your service, bye"]
            speak(opt[random.randint(0, len(opt)-1)])
            quit()

        elif ("your" in command and "capabilities" in command) or "can you do" in command:
            message = """What I can do for now is
                            search on wikipedia, tell the current date and time"""
            speak(message)

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

        elif "send email" in command or "send mail" in command or "send an email" in command or "send a mail" in command:
            speak("To who? Please type for me...")
            receiver = str(input("Enter receiver's email: "))
            speak("Gotten. Please what should I send")
            msg = take_command()
            print(msg)
            send_mail(receiver, msg)

        elif "play songs" in command or "play song" in command or "play music" in command:
            speak("ok. relax let me search for where the song is")
            play_music()

        elif command.__contains__("") or command.__contains__(" "):
            speak(" ")
        else:
            speak("this is above my capabilities to answer or do")



if __name__ == '__main__':
    welcome_address()
    ask_of_health()

    speak("how may I help you?")
    start = True
    capabilities(start)


    take_command()



