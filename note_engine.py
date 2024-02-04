""" Note Engine: Script for creating, adding and reading previous notes."""

import datetime
from voice_engine import speak
from listner_engine import get_audio


def create_note(title, number):
    """
    Create a new note file with a given title and number.

    Args:
        title (str): Title of the note.
        number (int): Number associated with the note.

    Returns:
        str: Path of the created note file.
    """
    path = "notes/" + title + "_" + str(number) + ".txt"
    with open(path, "w") as f:
        f.write(title + " : " + str(datetime.datetime.now()) + "\n")
    return path


def write_note(path, content):
    """
    Append content to an existing note file.

    Args:
        path (str): Path of the note file.
        content (str): Content to be appended to the note.
    """
    with open(path, "a") as f:
        f.write(content + "\n")
    f.close()


def start_noting(title, number, control_type):
    """
    Start the process of creating a new note.

    Args:
        title (str): Title of the note.
        number (int): Number associated with the note.
        control_type (int): Control type (0 for voice control, 1 for manual input).
    """
    path = create_note(title, number)
    to_write = ['Previous_Note_path: \n', path]

    with open("working_deets.txt", "w") as f:
        f.writelines(to_write)

    print("What should I note down ?")
    speak("What should I note down ?")
    note = get_audio() if control_type == 0 else input("note:> ")
    while note != 'no':
        print(note)
        write_note(path, note)
        print("Anything else to add")
        speak("Anything else to add")
        note = get_audio() if control_type == 0 else input("note:> ")


def read_prev_note():
    """
    Read the contents of the previously created note.

    This function reads the path from 'working_deets.txt' and reads the corresponding note file.
    """
    print("Let me check the files")
    print("------------")
    speak("Let me check the files")

    with open("working_deets.txt", "r") as f:
        read_lines = f.readlines()

    prev_path = read_lines[1]

    try:
        with open(prev_path, "r") as f:
            prev_read = f.readlines()

        print("Reading Note title " + prev_path[prev_path.find("s") + 2:])
        speak("Reading Note title " + prev_path[prev_path.find("s") + 2:])

        for i in prev_read[1:]:
            i = i.strip()
            if len(i) < 1:
                continue
            print(i)
            speak(i)

        print("------------")
        print("That was all.")
        speak("That was all. Closing Note.")

    except Exception as e:
        print("Sorry no such previous records.")
        speak("Sorry no such previous records.")
