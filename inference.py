from flask import Flask, render_template, jsonify
import numpy as np
import cv2
import mediapipe as mp
from keras.models import load_model

app = Flask(_name_)

# Load the pre-trained emotion detection model and labels
model = load_model("model.h5")
label = np.load("labels.npy")

# Initialize mediapipe for face and hand landmark detection
holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

# Example dictionary of book recommendations
book_recommendations = {
    "Happy": [
        {"title": "Pride and Prejudice", "genre": "Classic Novel"},
        {"title": "The Hobbit", "genre": "Fantasy"}
    ],
    "Sad": [
        {"title": "The Power of Now", "genre": "Self Help"},
        {"title": "The Hitchhiker's Guide to the Galaxy", "genre": "Comedy"}
    ],
    "Angry": [
        {"title": "The Bhagavad Gita", "genre": "Spiritual"},
        {"title": "Atomic Habits", "genre": "Motivation"}
    ],
    "Surprised": [
        {"title": "The Catcher in the Rye", "genre": "Classic Novel"},
        {"title": "The Curious Incident of the Dog in the Night-Time", "genre": "Mystery"}
    ]
}

# Global variable to store detected emotion
emotion = "Neutral"

# Function to capture emotion once and detect it using the pre-trained model
def capture_emotion_once():
    global emotion
    cap = cv2.VideoCapture(0)

    while True:
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        # Process the frame for emotion detection
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        if res.face_landmarks:
            lst = []
            for i in res.face_landmarks.landmark:
                lst.append(i.x - res.face_landmarks.landmark[1].x)
                lst.append(i.y - res.face_landmarks.landmark[1].y)

            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)

            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)

            lst = np.array(lst).reshape(1, -1)
            pred = label[np.argmax(model.predict(lst))]

            emotion = pred
            print("Detected emotion:", emotion)
            break

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture_emotion', methods=['POST'])
def capture_emotion():
    global emotion
    capture_emotion_once()  # Capture emotion once when requested

    # Get book recommendations based on detected emotion
    recommended_books = book_recommendations.get(emotion, [])

    # Create a list of book titles to send to the frontend
    books = [{"title": book["title"], "genre": book["genre"]} for book in recommended_books]

    # Return emotion and recommended books as a JSON response
    return jsonify({"emotion": emotion, "recommended_books": books})

if _name_ == "_main_":
    app.run(debug=True)