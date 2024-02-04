""" Voice Engine: A Script for text to speech using Windows Voices."""

import pyttsx3


def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init('sapi5')

    # Set the voice (using the third voice in this case)
    engine.setProperty('voice', engine.getProperty('voices')[1].id) # change the id if you are facing any problem.

    # Set the volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)

    # Set the speech rate (words per minute)
    engine.setProperty('rate', 175)

    # Speak the provided text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
