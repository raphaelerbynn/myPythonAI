# import getpass
# pw = getpass.getpass("enter hidden word: ")
# print(type(pw))

# import smtplib

# to = "rerbynn@stu.ucc.edu.gh"
# send = "erbynn1234@gmail.com"
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.ehlo()
# server.starttls()
# server.login(send, "mountain500000")
# server.sendmail(send, to, "Message from personal AI")

import os
import time
from threading import Thread, Event

basedir = ['C:\\']
songs_dir = []


def action():
    i = 0
    while True:
        i += 1
        print(i)
        time.sleep(1)
        for dir in basedir:
            # speak("searching")
            for r,d,f in os.walk(dir):
                # speak("searching")
                for files in f:
                    # speak("searching")
                    if files.__contains__('.mp3'):
                        songs_dir.append(os.path.join(r, files))
        if Event().is_set():
            break
    print(songs_dir)
                    
action_thread = Thread(target=action)   
action_thread.start()
action_thread.join(timeout=10)
Event().set()
print("Done")
print(songs_dir)
      
# print(songs_dir)
# os.startfile(songs_dir[0])


# print os.path.abspath("something.exe")
# print(basedir)
