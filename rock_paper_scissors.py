""" Rock-Paper-Scissors: A game implemented using computer vision with open cv and custom trained yolo model."""
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
import random
import time
from ultralytics import YOLO
import cv2
from voice_engine import speak

# Initialize the game engine
print("Initializing Game Engine")
speak("Initializing Game Engine")
labels = ["Rock", "Paper", "Scissors"]
model = YOLO("Models/best.pt", verbose=False)

# Define the function to start the game
def start_game(no_of_plays):
    print("Starting Rock; Paper; Scissors Game")
    speak("Starting Rock; Paper; Scissors Game")
    player_score = 0
    computer_score = 0
    threshold = 0.55
    img = None

    # Loop through the specified number of plays
    for i in range(0, no_of_plays):
        cap = cv2.VideoCapture(0)
        computer_choice = labels[random.randint(0, 2)]
        print("Turn " + str(i + 1) + ". Say Rock; Paper; Scissors.")
        speak("Turn " + str(i + 1) + ". Say Rock; Paper; Scissors.")
        ret, frame = cap.read()
        player_choice_list = []

        # Capture multiple frames for robust object detection
        for _ in range(0, 15):
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            results = model(frame, verbose=False)[0]

            # Iterate over detected objects and choose the label with the highest count
            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = result
                if score > threshold:
                    player_choice_list.append(labels[int(class_id)])
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                    cv2.putText(frame, labels[int(class_id)], (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 3, cv2.LINE_AA)  # Display label
                    break

        # Determine the player's choice based on the label count
        rock_no = player_choice_list.count("Rock")
        paper_no = player_choice_list.count("Paper")
        scissors_no = player_choice_list.count("Scissors")
        max_no = max(rock_no, paper_no, scissors_no)
        if max_no == rock_no:
            player_choice = "Rock"
        elif max_no == paper_no:
            player_choice = "Paper"
        else:
            player_choice = "Scissors"

        # Display choices and determine the winner
        print("I chose " + computer_choice)
        speak("I chose " + computer_choice)
        print("You chose " + player_choice)
        speak("You chose " + player_choice)
        if player_choice == computer_choice:
            print("Draw")
            speak("Draw")

        # Evaluate and announce the winner for each turn
        match player_choice:
            case "Rock":
                if computer_choice == "Paper":
                    computer_score += 1
                    print("I win")
                    speak("I win")
                if computer_choice == "Scissors":
                    player_score += 1
                    print("You win")
                    speak("You win")

            case "Paper":
                if computer_choice == "Rock":
                    player_score += 1
                    print("You win")
                    speak("You win")
                if computer_choice == "Scissors":
                    computer_score += 1
                    print("I win")
                    speak("I win")

            case "Scissors":
                if computer_choice == "Rock":
                    computer_score += 1
                    print("I win")
                    speak("I win")
                if computer_choice == "Paper":
                    player_score += 1
                    print("You win")
                    speak("You win")

            case _:
                print("Did you even make a move ?")
                speak("Did you even make a move ?")

        # Release video capture and close windows
        cap.release()
        cv2.destroyAllWindows()

    # Announce the final results of the game
    if player_score > computer_score:
        print("Congratulations, you won.")
        speak("Congratulations, you won.")
    elif computer_score > player_score:
        print("Too bad, better luck next time.")
        speak("Too bad, better luck next time.")
    else:
        print("That is a draw. We both make good rivals.")
        speak("That is a draw. We both make good rivals.")
