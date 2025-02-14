from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import bcrypt
from pymongo import MongoClient
from keras.models import load_model
import numpy as np
import cv2
import mediapipe as mp
import random  # Importing the random module
from bson import ObjectId

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["book_recommendation"]
users_collection = db["users"]
user_moods_collection = db["user_moods"]
user_ratings_collection = db["user_ratings"]
previous_recommendations_collection = db["previous_recommendations"]

# Load the pre-trained emotion detection model and labels
model = load_model("model.h5")
label = np.load("labels.npy")

# Initialize mediapipe for face and hand landmark detection
holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

# Global variable to store detected emotion
emotion = "Neutral"

# Global variable to store previously recommended books in the current session
previously_recommended_books = []

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

            emotion = pred.lower()
            print("Detected emotion:", emotion)
            break

    cap.release()

def get_books_from_db(emotion, exclude_books=None):
    collection = db[emotion]
    books = list(collection.find({}, {"_id": 0}))

    if exclude_books:
        filtered_books = [book for book in books if book['title'] not in exclude_books]
    else:
        filtered_books = books

    # Select 2 random books from the list
    if len(filtered_books) > 2:
        return random.sample(filtered_books, 2)  # Get 2 random books
    elif len(filtered_books) > 0:
        return filtered_books  # If there are less than 2 books, return all of them
    else:
        return None  # Return None if no books are available

@app.route('/')
def index():
    global previously_recommended_books
    previously_recommended_books = []  # Reset previously recommended books on new session
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({"username": username})

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials, please try again.", "error")  # Flash an error message

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if users_collection.find_one({"username": username}):
            flash("Username already exists, please choose a different one.", "error")  # Flash an error message
            return render_template('register.html')  # Return to the same page

        users_collection.insert_one({"username": username, "password": hashed_pw})
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/capture_emotion', methods=['POST'])
def capture_emotion():
    global previously_recommended_books
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    capture_emotion_once()  # Capture emotion once when requested

    # Save user's mood into the database
    user_moods_collection.insert_one({"username": username, "emotion": emotion})

    # Get book recommendations from MongoDB based on detected emotion
    recommended_books = get_books_from_db(emotion)

    # Save previous recommendations
    previous_recommendations_collection.insert_one({
        "username": username,
        "mood": emotion,
        "books": recommended_books
    })

    previously_recommended_books.extend([book['title'] for book in recommended_books])

    # Return emotion and recommended books as a JSON response
    return jsonify({"emotion": emotion.capitalize(), "recommended_books": recommended_books})

@app.route('/re_recommend', methods=['POST'])
def re_recommend():
    global previously_recommended_books
    if 'username' not in session:
        return redirect(url_for('login'))

    # Use the global variable 'emotion' that was set during emotion capture
    recommended_books = get_books_from_db(emotion, exclude_books=previously_recommended_books)

    if recommended_books is None:
        return jsonify({"error": "Sorry, we are out of recommendations."})

    # Save the new recommendations in the previous_recommendations collection
    previous_recommendations_collection.insert_one({
        "username": session['username'],
        "mood": emotion,
        "books": recommended_books
    })

    previously_recommended_books.extend([book['title'] for book in recommended_books])

    # Return the new recommendations as a JSON response
    return jsonify({"recommended_books": recommended_books})

@app.route('/submit_rating', methods=['POST'])
def submit_rating():
    if 'username' not in session:
        return redirect(url_for('login'))

    data = request.get_json()
    title = data['title']
    rating = data['rating']

    # Fetch the document
    doc = previous_recommendations_collection.find_one({"username": session['username'], "books.title": title})

    if doc:
        # Update the rating for the specific book
        for book in doc['books']:
            if book['title'] == title:
                book['rating'] = rating
                break

        # Save the updated document
        previous_recommendations_collection.update_one({"_id": doc["_id"]}, {"$set": doc})

    return jsonify({"message": "Rating submitted successfully"})

@app.route('/previous_moods')
def previous_moods():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    previous_recommendations = list(previous_recommendations_collection.find({"username": username}, {"_id": 1}))
    previous_recommendations_with_details = []

    for item in previous_recommendations:
        details = previous_recommendations_collection.find_one({"_id": item["_id"]})
        details["_id"] = str(details["_id"])
        previous_recommendations_with_details.append(details)

    return render_template('previous_moods.html', previous_recommendations=previous_recommendations_with_details)

if __name__ == "__main__":
    app.run(debug=True)
