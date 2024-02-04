""" Physical Engine: Script for initializing and sending data to arduino bot."""

import serial
import time
from voice_engine import speak

COM_PORT = 'com6'  # Change after checking to which port arduino is connected


def send_data(cmd, l):
    """
    Send data to Arduino using serial communication.

    Args:
        cmd (str): Command to send to Arduino.
        l (int): Number of times to send the command.

    Note:
        Assumes the Arduino is connected to the 'com6' port and uses a baud rate of 9600.
    """
    try:
        # Establish a serial connection to Arduino
        arduino_data = serial.Serial(COM_PORT, 9600, timeout=1)
        time.sleep(2)

        # Reset input and output buffers
        arduino_data.reset_input_buffer()
        arduino_data.reset_output_buffer()

        # Check if the serial connection is established
        if arduino_data is not None:
            # Send the command 'l' times to Arduino
            for i in range(0, l):
                cmd = cmd + '\r'
                arduino_data.write(cmd.encode('utf-8'))

            # Send a termination signal ('a') to Arduino
            arduino_data.write('a'.encode('utf-8'))

            # Close the serial connection
            arduino_data.close()

    except Exception as e:
        print(e)
        speak("No hardware detected. Check connections.")
