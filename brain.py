""" Brain: Main Script For Handling the various engines and processes of Cyclops."""

import os
import time
import datetime

import pygame

from llm_engine import LLM_answer, llama_message_init
from image_engine import scrape_images
import cv2 as cv
import numpy as np
from listner_engine import get_audio
from voice_engine import speak
from news_engine import get_news_science, get_news_world
from music_engine import play_music, play_youtube_video
from pygame import mixer
from visual_engine import show_my_face, emotion_identity
from timer_engine import timer_set, lock_windows
from physical_engine import send_data
from scheduler_engine import add_schedule, check_schedule
from note_engine import start_noting, read_prev_note
from rock_paper_scissors import start_game
from hangman import HangmanGame


# Defining some constants

LOOP_ARD = 1  # Tells how many times data has to be sent to the arduino
IDLE_TIME_LIMIT = 1800  # Indicates in seconds the amount of time after which idleness reminder has to be played.
EMOTION_TIME_LIMIT = 7200  # Indicates in seconds the amount of time after which emotion detection has to be carried out.
LOG_OUT_TIME_LIMIT = 120  # Indicates in seconds after how many minutes the user present in front of computer has to be checked.

MONTH_LIST = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november",
              "december"]  # For mapping months in number to words

USER_DETAILS = ""  # For storing and passing user details to llm
LOOP_CONTROLLER = True  # Controls the main loop
LOCK_FLAG = 0  # For checking the lock status of the windows
CONTROL_TYPE = 1  # By default, 0 is for speech control 1 for type control
AFTER_KEYWORD = 2  # Specifies how many times input should be taken after keyword recognition.


def first_load():
    """
       Function to gather user information during the first load.
       It prompts the user for details like name, music preference, age, and profession.
       Saves the user's details to a file.
    """

    send_data("on", LOOP_ARD)
    mixer.music.load('music_and_tones/deep-ambient-version-60s-9889.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()
    time.sleep(1)

    print("Hello I am Cyclops your personal desktop assistant.")
    speak("Hello I am Cyclops your personal desktop assistant.")

    print("What should I call you friend ?")
    speak("What should I call you friend ?")
    user_name = input()

    print("Oh what a wonderful name. Help me know you better so that I can assist you.")
    speak("Oh what a wonderful name. Help me know you better so that I can assist you.")

    print("Tell me your favourite music " + user_name)
    speak("Tell me your favourite music " + user_name)
    user_music = input()

    print("What is your age ?")
    speak("What is your age ?")
    user_age = input()

    print("Where do you work or are you a student ?")
    speak("Where do you work or are you a student ?")
    user_profession = input()

    with open("user_pref.txt", "a") as f:
        deets = "Name: " + user_name + '\n' + "Music: " + user_music + '\n' + "Age: " + user_age + '\n' + "Job: " + user_profession + '\n' + "Last Boot: " + str(
            datetime.datetime.now().day) + '\n'
        f.write(deets)

    with open("working_deets.txt", "w") as f:
        f.write("Previous_Note_path: \n")

    return deets


def llm_interpreter(func, res):
    """
       Function to interpret the LLM response and execute corresponding actions.
    """

    brack_start = func.find("(")
    brack_end = func.find(")")
    f_name = func[0:brack_start]
    match f_name:
        case "show_image":
            send_data("#" + response, LOOP_ARD)
            image_name = func[brack_start + 1:brack_end]
            if len(image_name) < 1:
                image_name = res.split()[-2]
            scrape_images(image_name)
            pics = os.listdir("images_temp")
            img_list = []
            img = np.zeros([255, 255])
            for path in range(0, len(pics)):
                if image_name in pics[path]:
                    img = cv.imread("images_temp/" + pics[path])
                    img = cv.resize(img, (500, 350))
                    os.remove("images_temp/" + pics[path])
                    img_list.append(img)
            img_collage = np.concatenate((np.concatenate((img_list[0], img_list[1]), axis=1),
                                          np.concatenate((img_list[2], img_list[3]), axis=1)), axis=0)
            cv.imshow(image_name, img_collage)
            cv.waitKey(0)
            cv.destroyAllWindows()

        case "play_youtube":
            send_data("sine", LOOP_ARD)
            yt_search = func[brack_start + 1:brack_end]
            play_youtube_video(yt_search)

        case "schedule":
            send_data("#Scheduler", LOOP_ARD)
            first_comma = func.find(",")
            second_comma = func.find(",", first_comma + 1)
            third_comma = func.find(",", second_comma + 1)
            day = func[brack_start + 1:first_comma].strip()
            month = func[first_comma + 1:second_comma].strip()
            year = func[second_comma + 1:third_comma].strip()
            note = func[third_comma + 1:brack_end].strip()
            print("Should I set the schedule on " + day + " of " + month + " year " + year)
            speak("Should I set the schedule on " + day + " of " + month + " year " + year)
            if CONTROL_TYPE == 0:  # To use audio input
                inp = get_audio()
            elif CONTROL_TYPE == 1:  # To use typing input
                inp = input("::> ")
            else:
                inp = " "
            inp = inp.lower()
            if 'yes' in inp or 'yeah' in inp or 'sure' in inp or 'go ahead' in inp:
                add_schedule(day, month, year, note)
                print("Default schedule added")
                speak("Default schedule added")
            else:
                print("Tell me the day")
                speak("Tell me the day")
                day = get_audio() if CONTROL_TYPE == 0 else input("::> ")
                print("Tell me the month")
                speak("Tell me the month")
                month = get_audio() if CONTROL_TYPE == 0 else input("::> ")
                print("Tell me the year")
                speak("Tell me the year")
                year = get_audio() if CONTROL_TYPE == 0 else input("::> ")
                print("Tell me the note")
                speak("Tell me the note")
                note = get_audio() if CONTROL_TYPE == 0 else input("::> ")
                add_schedule(day, month, year, note)
                print("New schedule added")
                speak("New schedule added")

        case "timer":
            send_data('clock', LOOP_ARD)
            time_to_set = 0
            if "minutes" in func:
                time_to_set = int(func[brack_start + 1:func.find("minutes")].strip())
                message_timer = func[func.find(","):brack_end]
            elif "seconds" in func:
                time_to_set = int(func[brack_start + 1:func.find("seconds")].strip())
                message_timer = func[func.find(","):brack_end]
            else:
                time_to_set = 1
                message_timer = 'default one minute timer done because sometimes llm are dumb'

            timer_set(time_to_set, message_timer)

        case _:
            print("No Function")


def first_boot_today():
    """
       Function to be executed on the first boot of the day.
       It checks for major headlines, schedules, and performs necessary actions.
    """

    send_data("logo", LOOP_ARD)
    print("Welcome " + user_name + ". Hope you are doing great.")
    speak("Welcome " + user_name + ". Hope you are doing great.")
    print("Should I go over some major headlines today?")
    speak("Should I go over some major headlines today?")
    ans = get_audio()
    print(ans)

    if 'yes' in ans or 'yeah' in ans or 'ok' in ans or 'sure' in ans:
        send_data("#News Today", LOOP_ARD)
        get_news_world()
        get_news_science()

    else:
        print("Ok got it")
        speak("Ok got it")

    print("Checking Schedules for you.")
    speak("Checking Schedules for you.")
    today_schedule = check_schedule()
    send_data("#" + today_schedule, LOOP_ARD)
    print(today_schedule)
    speak(today_schedule)


def noting_begin():
    """
        Function to handle note-related actions.
        It prompts the user to add a new note or read previous notes.
    """

    print("Should I add a new Note or read previous note ?")
    speak("Should I add a new Note or read previous note ?")
    note_flag = get_audio() if CONTROL_TYPE == 0 else input("note:>")
    if "new" in note_flag:
        print("What is the title of note ?")
        speak("What is the title of note ?")
        title = get_audio() if CONTROL_TYPE == 0 else input("note:>")
        start_noting(title, datetime.date.today().day, CONTROL_TYPE)
    elif "prev" in note_flag or "previous" in note_flag:
        read_prev_note()
    else:
        print("Sorry your command is not understandable.")
        speak("Sorry your command is not understandable.")


if __name__ == '__main__':
    pygame.init()
    # Initialize pygame mixer for music
    mixer.init()
    if os.path.exists("user_pref.txt"):  # outer if start
        message, llama_model = llama_message_init(USER_DETAILS)  # loading the llm

        with open('user_pref.txt', 'r') as f:
            b = f.readline().strip()[-1]
            f.seek(0)
            data = f.readlines()

        user_name = data[1][data[1].find(":") + 1:].strip()

        if int(b) == 0:  # checking if the boot is the first one
            first_boot_today()
            data[0] = "Boot: 1\n"
            data[-1] = "Last Boot: " + str(datetime.datetime.now().day) + '\n'

            with open('user_pref.txt', 'w') as f:
                f.writelines(data)

        else:
            with open('user_pref.txt', 'r') as f:
                data = f.readlines()

            if int((data[-1].strip()[-2:]).strip()) != datetime.datetime.now().day:
                data[0] = "Boot: 1\n"
                data[-1] = "Last Boot: " + str(datetime.datetime.now().day) + '\n'
                first_boot_today()
            else:
                send_data("#Welcome", LOOP_ARD)
                print("Welcome again. Time to be productive.")
                speak("Welcome again. Time to be productive.")

            with open('user_pref.txt', 'w') as f:
                f.writelines(data)

        time_master = time.time()  # keeps track of the time of idleness
        emotion_time_master = time.time()  # keeps track of when to check for person's emotions
        logout_time_master = time.time()  # keeps track of when to check for user's presence

        while LOOP_CONTROLLER:

            response = ""
            function = ""

            if time.time() - logout_time_master > LOG_OUT_TIME_LIMIT:
                send_data("#Checking for you", 1)
                my_face = show_my_face(1)  # takes a picture of face
                LOCK_FLAG = lock_windows(my_face, LOCK_FLAG)  # checks for if the person is in front of screen or not

                if LOCK_FLAG == 1:  # if windows is locked the program is suspended
                    continue
                logout_time_master = time.time()

            if time.time() - time_master > IDLE_TIME_LIMIT:  # For Idleness
                my_face = show_my_face(1)
                if my_face is not None:
                    send_data("exercise", LOOP_ARD)
                    print("Time to stretch for 2 minutes")
                    speak("Time to stretch for 2 minutes. I will also oil my engines.")
                    time.sleep(120)
                    speak("Let's get back on track")
                time_master = time.time()

            if time.time() - emotion_time_master > EMOTION_TIME_LIMIT:  # For Emotion recognition
                send_data("#Analyzing Emotions", 1)
                my_face = show_my_face(1)
                if my_face is not None:
                    print("Analyzing Emotions")
                    owner_emotion, eye_status = emotion_identity(15)

                    if owner_emotion == 'happy' and eye_status == 'open':
                        send_data("happy", LOOP_ARD)
                        speak("You look Happy let me elevate that feeling")
                        response, function, message = LLM_answer("I am feeling happy cyclopes join my happiness",
                                                                 message,
                                                                 llama_model)

                    elif owner_emotion == 'sad' and eye_status == 'open':
                        send_data("sad", LOOP_ARD)
                        speak("You look sad let me think of how to cheer you up")
                        response, function, message = LLM_answer("I am feeling sad cyclopes cheer me up", message,
                                                                 llama_model)

                    elif eye_status == 'closed':
                        send_data("#Zzzz Zzzzz", LOOP_ARD)
                        print("You are drowsy. Please do some stretching or take a power nap.")
                        speak("You are drowsy. Please do some stretching or take a power nap.")
                        time.sleep(1)
                        print("Should I set a powernap timer for 25 minutes ?")
                        speak("Should I set a powernap timer for 25 minutes ?")
                        power_nap = get_audio() if CONTROL_TYPE == 0 else input("power_nap:> ")
                        power_nap = power_nap.strip()

                        if 'yes' in power_nap or 'yeah' in power_nap or 'sure' in power_nap:
                            send_data("clock", LOOP_ARD)
                            timer_set(25, "Power nap")
                        else:
                            print(
                                "Ok then, I am not setting a timer. But please remember body requires some maintenance "
                                "to keep going.")
                            speak(
                                "Ok then, I am not setting a timer. But please remember body requires some maintenance "
                                "to keep going.")

                    print(response)
                    send_data('rotate1', 1)
                    speak(response)
                    print(function)
                    llm_interpreter(function, response)
                    response = ""
                    function = ""
                    emotion_time_master = time.time()
                    continue

            # Handle user input based on control type (audio or typing)
            if CONTROL_TYPE == 0:  # To use audio input
                audio_inp = get_audio(1)

            elif CONTROL_TYPE == 1:  # To use typing input
                audio_inp = input("::> ")

            else:
                continue

            audio_inp = audio_inp.lower().strip()

            if len(audio_inp) <= 1:
                continue

            print(audio_inp)

            if 'cyclops' in audio_inp or 'cyclones' in audio_inp:  # detecting word cyclops
                send_data("led_blink", 1)

                print("Yes I am here.")
                speak("Yes I am here.")

                for i in range(0,
                               AFTER_KEYWORD):  # After cyclops keyword recognition, it runs for specified number of times
                    if i > 0:
                        print("You want to say anything else")
                        speak("You want to say anything else")

                    audio_inp = get_audio() if CONTROL_TYPE == 0 else input("::> ")
                    audio_inp = audio_inp.strip()

                    print(audio_inp)

                    if ("what" in audio_inp or "whats" in audio_inp or "what's" in audio_inp) and "time" in audio_inp:
                        send_data('rotate2', 1)
                        current_time = datetime.datetime.now()
                        speak(
                            "Current time is " + str(current_time.hour) + " hours " + str(
                                current_time.minute) + " minutes")

                    elif ("what" in audio_inp or "whats" in audio_inp or "what's" in audio_inp) and "date" in audio_inp:
                        send_data('rotate2', 1)
                        current_date = datetime.datetime.now()
                        speak("Current date is " + str(current_date.day) + " of " + MONTH_LIST[current_date.month - 1])

                    elif "play" in audio_inp and "music" in audio_inp:
                        send_data("sine", LOOP_ARD)
                        if "classical" in audio_inp:
                            play_music("classical")
                        elif "pop" in audio_inp:
                            play_music("pop")
                        elif "techno" in audio_inp:
                            play_music("techno")
                        elif "rock" in audio_inp:
                            play_music("rock")
                        else:
                            play_music("techno")

                    elif "play" in audio_inp and ("games" in audio_inp or "game" in audio_inp):
                        send_data("game", LOOP_ARD)
                        print("What game you want to play ? 1.Hangman 2.Rock Paper Scissors")
                        speak("What game you want to play ? Hangman or Rock, Paper, Scissors")
                        game = get_audio() if CONTROL_TYPE == 0 else input("game:> ")

                        if "rock" in game or "paper" in game or "scissors" in game:
                            start_game(5)
                        elif "hangman" in game or "Hangman" in game:
                            hangman_game=HangmanGame()
                            hangman_game.start_hangman()
                            pygame.quit()

                    elif "how do I look" in audio_inp or "i" and "look" in audio_inp:
                        send_data('camera', LOOP_ARD)
                        show_my_face()

                    elif "note engine" in audio_inp or "noting engine" in audio_inp:
                        send_data("#Note Engine....", LOOP_ARD)
                        noting_begin()

                    elif "click a picture" in audio_inp or "take a picture" in audio_inp:
                        send_data("camera", LOOP_ARD)
                        show_my_face(0, 1)

                    elif (
                            "what" in audio_inp or "whats" in audio_inp or "what's" in audio_inp) and "temperature" in audio_inp and "room" in audio_inp:
                        send_data("temph", LOOP_ARD)
                        print("Check the screen on my body")
                        speak("Check the screen on my body")

                    elif "shut down" in audio_inp or "shutdown" in audio_inp:
                        send_data('rotate1', 1)
                        mixer.init()
                        mixer.music.load(
                            'music_and_tones/short-warm-piano-prelude-intro-ending-for-film-and-video-182969.mp3')
                        mixer.music.set_volume(0.3)
                        mixer.music.play()
                        send_data("angry", LOOP_ARD)
                        print("Turning down the engines. Good bye")
                        speak("Turning down the engines. Good bye")
                        time.sleep(2)
                        send_data("off", LOOP_ARD)
                        LOOP_CONTROLLER = False
                        break

                    elif "type mode" in audio_inp or "typing mode" in audio_inp:
                        send_data("#Type Mode", LOOP_ARD)
                        CONTROL_TYPE = 1

                    elif "audio mode" in audio_inp:
                        send_data("#Audio Mode", LOOP_ARD)
                        CONTROL_TYPE = 0

                    else:
                        speak("Let me think")
                        send_data("#LLM Thinking     Please Wait", LOOP_ARD)
                        response, function, message = LLM_answer(audio_inp, message, llama_model)
                        print(response)
                        send_data('rotate2', 1)
                        speak(response)
                        print(function)
                        llm_interpreter(function, response)

                send_data("logo", 1)

    # outer if ends
    else:
        with open("user_pref.txt", "a") as fil:
            fil.write("Boot: " + "0" + '\n')

        USER_DETAILS = first_load()
