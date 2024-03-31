#!/usr/bin/python3
import time
import cv2
import face_recognition
from picamera2 import MappedArray, Picamera2, Preview
import numpy as np
import os
import pyrebase
from gpiozero import Button
import local_database


doorbell = Button(6)


def draw_faces(request):
    global capture_needed
    with MappedArray(request, "main") as m:
        for f in faces:
            (x, y, w, h) = [c * n // d for c, n, d in zip(f, (w0, h0) * 2, (w1, h1) * 2)]
            cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 255, 0, 0))
            capture_needed = True

def retrieve_known_names():
    global known_face_names
    
    # Retrieve face encodings and names from Firebase
    face_encodings_data = db.child(username).child(dataset_encodings).get()

    # Check if the retrieval was successful
    if face_encodings_data.each() is not None:
        for item in face_encodings_data.each():
            name = item.key()  # The name of the individual
            known_face_names.append(name)
            
            
def retrieve_known_encodings():
    global known_face_encodings
    
    # Retrieve face encodings and names from Firebase
    face_encodings_data = db.child(username).child(dataset_encodings).get()

    # Check if the retrieval was successful
    if face_encodings_data.each() is not None:
        for item in face_encodings_data.each():
            encoding = np.array(item.val())  # Convert the list back into a NumPy array
            known_face_encodings.append(encoding)
            
def compare():
    global capture_needed
    global known_face_encodings
    global known_face_names   
    
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    
    while True:
        buffer = picam2.capture_buffer("lores")
        grey = buffer[:s1 * h1].reshape((h1, s1))
        faces = face_detector.detectMultiScale(grey, 1.1, 3)
        if capture_needed:
            print("Face successfully detected, please stay still for 3 seconds!")
            time.sleep(3)
            picam2.capture_file("unknown_person.jpg")
            print("Face was detected, thanks!")
            capture_needed = False  # Reset flag after capturing
            picam2.stop_preview()
            break
    
    unknown_face_encoding = encode_unknown_face()
    if unknown_face_encoding is not None:
        distances = face_recognition.face_distance(known_face_encodings, unknown_face_encoding)
        best_match_index = np.argmin(distances)
        if distances[best_match_index] < 0.6:  # Threshold for "closeness"
            print(f"Match found: {known_face_names[best_match_index]}")
            local_database.store_attempt("Successful match") #Stores attempt in local DB
            return True
        
    print("No matching face found.")
    local_database.store_attempt("Unsuccessful match") #Stores attempt in local DB
    return False
    
def encode_unknown_face():
    unknown_image_path = "unknown_person.jpg"
    unknown_image = face_recognition.load_image_file(unknown_image_path)
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)
    if unknown_face_encoding:
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        return unknown_face_encoding
    else:
        return None
        
def encode_known_face(known_face_path):
    global known_face_names
    global name
    
    face_image = face_recognition.load_image_file(known_face_path) #Loads image as numpy array
    face_encoding = face_recognition.face_encodings(face_image)
    if face_encoding:
        face_encoding = face_recognition.face_encodings(face_image)[0]

        
        list_known_face_encodings = face_encoding.tolist()
        db.child(username).child(dataset_encodings).child(name).set(list_known_face_encodings) #Stores encoding and name in cloud DB
        local_database.store_encoding(list_known_face_encodings) #Stores encoding in local DB
        local_database.store_name(name) #Stores name in local DB
        
        print("Face recognition successful for " + name + "!")
    else:
        print("Face recognition failed for " + name + "!" + " Please retry with your full face in the picture.")


###################################################################################################################

                                    #############FIREBASE INFO####################
config = { 
  "apiKey": "AIzaSyCPJYIY1FpwZ9aytnzeMCTuBUkVo_KqJQc", 
  "authDomain": "sysc3010-lab3-15f70.firebaseapp.com", 
  "databaseURL": "https://sysc3010-lab3-15f70-default-rtdb.firebaseio.com/", 
  "storageBucket": "sysc3010-lab3-15f70.appspot.com" 
}

# Connect using the configuration 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 
dataset_encodings = "Known Face Encodings"
dataset_names = "Known Faces Names"
username = "Facial Recognition Camera"

###################################################################################################################


face_detector = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")


capture_needed = False  # Flag to indicate when a photo capture is needed

known_face_encodings = []
known_face_names = []

picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)}, lores={"size": (320, 240), "format": "YUV420"})
picam2.configure(config)


(w0, h0) = picam2.stream_configuration("main")["size"]
(w1, h1) = picam2.stream_configuration("lores")["size"]
s1 = picam2.stream_configuration("lores")["stride"]

faces = []
picam2.post_callback = draw_faces


known_faces_dir = "/home/bisher/facial_recognition/known_faces"
known_face_encodings = []
known_face_names = []

name = str(input("What is your name? "))
picam2.start_preview(Preview.QTGL)
picam2.start()

while True:
    
    buffer = picam2.capture_buffer("lores")
    grey = buffer[:s1 * h1].reshape((h1, s1))
    faces = face_detector.detectMultiScale(grey, 1.1, 3)
    if capture_needed:
        print("Face successfully detected, please stay still for 3 seconds!")
        time.sleep(3)
        known_face_path = os.path.join(known_faces_dir, name + ".jpg")
        picam2.capture_file(known_face_path)
        print("Facial Image has been taken, thanks " + name + "!")
        capture_needed = False  # Reset flag after capturing
        picam2.stop_preview()
        encode_known_face(known_face_path)
        again = str(input("Would you like to retry or save a new face (y/n)? "))
        if again.upper() != 'Y':
            break
        name = str(input("What is your name? "))
        picam2.start_preview(Preview.QTGL)
        picam2.start()

#Here we'll set up mode of operations
while True:

    if doorbell.is_pressed:
        retrieve_known_names()
        retrieve_known_encodings() 
        recognized = compare()
        if recognized:
            db.child("doorStatus").set(True)
        time.sleep(0.3)
    
