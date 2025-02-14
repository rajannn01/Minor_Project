import os   
import numpy as np  
import cv2  
from tensorflow.keras.utils import to_categorical 
from keras.layers import Input, Dense  
from keras.models import Model 
 
# Initialize flags and variables 
is_init = False 
size = -1 
 
label = [] 
dictionary = {} 
c = 0 
 
# Load the data from .npy files 
for i in os.listdir(): 
    if i.split(".")[-1] == "npy" and not(i.split(".")[0] == "labels"):   
        if not(is_init): 
            is_init = True  
            X = np.load(i) 
            size = X.shape[0] 
            y = np.array([i.split('.')[0]]*size).reshape(-1, 1) 
        else: 
            X = np.concatenate((X, np.load(i))) 
            y = np.concatenate((y, np.array([i.split('.')[0]]*size).reshape(-1, 1))) 
 
        label.append(i.split('.')[0]) 
        dictionary[i.split('.')[0]] = c   
        c += 1 
 
# Convert labels to integers using dictionary 
for i in range(y.shape[0]): 
    y[i, 0] = dictionary[y[i, 0]] 
y = np.array(y, dtype="int32") 
 
# Convert labels to categorical (one-hot encoding) 
y = to_categorical(y) 
 
# Shuffle the data 
X_new = X.copy() 
y_new = y.copy() 
cnt = np.arange(X.shape[0]) 
np.random.shuffle(cnt) 
 
for counter, i in enumerate(cnt):  
    X_new[counter] = X[i] 
    y_new[counter] = y[i] 
 
# Define the input shape for the model 
ip = Input(shape=(X.shape[1],))  # Make sure the input shape is a tuple 
# Build the model 
m = Dense(512, activation="relu")(ip) 
m = Dense(256, activation="relu")(m) 
op = Dense(y.shape[1], activation="softmax")(m) 
# Create the model 
model = Model(inputs=ip, outputs=op) 
# Compile the model 
model.compile(optimizer='rmsprop', loss="categorical_crossentropy", metrics=['acc']) 
# Train the model 
model.fit(X_new, y_new, validation_split=0.2, epochs=50) 
# Save the model and labels 
model.save("model.h5") 
np.save("labels.npy", np.array(label))