""" Timer Engine: A script for setting timer and locking the system if required."""

from voice_engine import speak
import time
from pygame import mixer
from listner_engine import get_audio
import ctypes
from visual_engine import show_my_face
import subprocess
from physical_engine import send_data

mixer.init()


def check_locked():
    """
    Checks if the Windows screen is locked.
    Returns:
        str: "Locked" if locked, "Unlocked" otherwise.
    """
    time.sleep(2)
    process_name = 'LogonUI.exe'
    callall = 'TASKLIST'
    outputall = subprocess.check_output(callall)
    outputstringall = str(outputall)

    if process_name in outputstringall:
        return "Locked"
    else:
        return "Unlocked"


def timer_set(time_min, message):
    """
    Sets a timer and plays music until the timer ends.
    Args:
        time_min (int): Timer duration in minutes.
        message (str): Message to be spoken before setting the timer.
    """
    time.sleep(2)
    speak("Idling the engines until the timer ends.")
    print(message)
    speak(message)
    speak(str(time_min) + " minutes timer set")
    time.sleep(time_min * 60)
    mixer.music.load('music_and_tones/tropical-summer-music-112842.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()
    done = "no"
    while done != "stop":
        done = get_audio(1)
        time.sleep(1)
    mixer.music.stop()
    speak("Timer stopped")


def lock_windows(my_face_val, flag):
    """
    Locks Windows screen based on face detection.
    Args:
        my_face_val (any): Face detection value.
        flag (int): Flag indicating whether face detection is enabled.
    Returns:
        int: 1 if Windows is locked, 0 otherwise.
    """
    if my_face_val is None and flag == 0:
        time.sleep(2)
        print("No person detected")
        speak("No person detected. Windows will lock in 10 seconds")
        time.sleep(10)
        if show_my_face(1) is None:
            send_data("logo", 1)
            ctypes.windll.user32.LockWorkStation()  # Lock the windows
            return 1
        else:
            print("Person came back")
            speak("Oh you are back. Aborting lock down.")
            return 0
    else:
        if check_locked() == "Locked":
            return 1
        else:
            return 0
