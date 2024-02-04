""" Visual Engine: A Script for camera, emotion recognition and drowsiness detection."""

import datetime
import cv2
import numpy as np
from silence_tensorflow import silence_tensorflow

silence_tensorflow()
import tensorflow as tf
from pygame import mixer
from voice_engine import speak

mixer.init()

print("Initializing Visual Engine")
speak("Initializing Visual Engine")

try:  # Loading all models
    emotion_model = tf.keras.saving.load_model("Models/model_emo (1).h5")
    eye_blink_model = tf.keras.saving.load_model("Models/eye_blink_model.h5")
    detector = cv2.FaceDetectorYN.create(
        "Models/face_detection_yunet_2023mar.onnx", "", (1024, 720), 0.9, 0.3, 5000)
except Exception as e:
    pass


def visualize(inp, faces, fps, thickness=1):
    coords = None
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            coords = face[:-1].astype(np.int32)
            cv2.rectangle(inp, (coords[0], coords[1]), (coords[0] + coords[2], coords[1] + coords[3]), (255, 255, 0),
                          thickness)
            # cv2.rectangle(input, (coords[4] - 30, coords[5] - 20), (coords[4] + 30, coords[5] + 20), (255, 255, 0),
            #               thickness)
            # cv2.rectangle(input, (coords[6] - 30, coords[7] - 10), (coords[6] + 30, coords[7] + 10), (0, 255, 0),
            #               thickness) # For bounding boxes of eyes
    cv2.putText(inp, "Press Q Key to exit. Press A for photo.", (1, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                2)
    return coords


# Function for camera
def show_my_face(get_face=0, click_pic=0):
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (1024, 720))
        im_sh = img.copy()
        if img is not None:
            faces = detector.detect(img)
            coords = visualize(img, faces, 60)

            if get_face == 1:
                return coords
            print("You Look Great Today")
            speak("You Look Great Today")
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('a') or click_pic == 1:
                print("Clicking Picture")
                cv2.imwrite("photos taken/face_img_" + str(datetime.date.today().day) + "_" + str(
                    datetime.datetime.now().minute) + ".png", im_sh)

                mixer.music.load('music_and_tones/camera-shutter-6305.mp3')
                mixer.music.set_volume(0.8)
                mixer.music.play()

                if click_pic == 1:
                    click_pic = 0
                    break

            cv2.imshow("CamView", img)

    cap.release()
    cv2.destroyAllWindows()


# Function for emotion and drowsiness detection
def emotion_identity(no_of_frames=10):
    emotion_list = ['happy', 'sad', 'neutral']
    eye_list = ['closed', 'open']
    emotions = []
    eyes = []
    cap = cv2.VideoCapture(0)
    while no_of_frames > 0:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (1024, 720))
        if img is not None:
            faces = detector.detect(img)
            coords = visualize(img, faces, 60)
            if coords is None:
                break
            face = img[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]
            eye = img[coords[5] - 20:coords[5] + 20, coords[4] - 30:coords[4] + 30]
            det = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            det = cv2.resize(det, (48, 48))
            det = det / 255.0
            det_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
            det_eye = cv2.resize(det_eye, (48, 48))
            det_eye = det_eye / 255.0
            emotions.append(
                emotion_list[np.argmax(emotion_model.predict(det.reshape((-1, 48, 48, 1)), verbose=False)[0])])
            eyes.append(
                eye_list[np.argmax(eye_blink_model.predict(det_eye.reshape((-1, 48, 48, 1)), verbose=False)[0])])

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        no_of_frames -= 1
    happy = emotions.count("happy")
    sad = emotions.count("sad")
    closed_eye = eyes.count("closed")
    open_eye = eyes.count("open")
    to_send = ["emotion", "eye"]
    if happy >= 4 or sad >= 4:
        if happy > sad:
            to_send[0] = "happy"
        elif happy <= sad:
            to_send[0] = "happy"
    else:
        to_send[0] = "neutral"

    if closed_eye > open_eye:
        to_send[1] = "closed"
    else:
        to_send[1] = "open"

    return to_send
