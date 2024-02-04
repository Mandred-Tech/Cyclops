""" Listener Engine: Script for speech to text using Vosk english model."""

from silence_tensorflow import silence_tensorflow
silence_tensorflow()
from pygame import mixer
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio
from voice_engine import speak

# Set log level for Vosk to suppress non-error logs
SetLogLevel(-1)

# Initialize the Pygame mixer for audio playback
mixer.init()

# Print and speak initialization message
print("Initializing Listener Engine")
speak("Initializing Listener Engine")

# Load the Vosk speech recognition model
model = Model("Models/vosk-model-en-us-0.22")

# Initialize the KaldiRecognizer with the model and sample rate
recognizer = KaldiRecognizer(model, 16000)

# Initialize the PyAudio object for working with the microphone
mic = pyaudio.PyAudio()


def get_audio(flag=0):
    # Open the microphone stream
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    data = ""

    # If flag is 0, play a system error notice tone
    if flag == 0:
        print("Start Speaking....")
        mixer.music.load('music_and_tones/system-error-notice-132470.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play()

    try:
        # Start streaming audio data from the microphone
        stream.start_stream()

        # Continue streaming until a valid recognition result is obtained
        while True:
            data = stream.read(4096)

            # Use Vosk to accept the waveform data and get the recognition result
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()
                break

    except Exception as e:
        # Handle exceptions related to microphone errors
        text = "Error in mic"
        print("Error in Mic")

    # Return the recognized text in lowercase
    return text[14:-3].lower()
