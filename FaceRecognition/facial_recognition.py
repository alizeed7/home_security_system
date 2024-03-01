#!/usr/bin/python3
import time
import cv2
import face_recognition
from picamera2 import MappedArray, Picamera2, Preview
import numpy as np
import os
import sys

def draw_faces(request):
    global capture_needed
    with MappedArray(request, "main") as m:
        for f in faces:
            (x, y, w, h) = [c * n // d for c, n, d in zip(f, (w0, h0) * 2, (w1, h1) * 2)]
            cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 255, 0, 0))
            capture_needed = True

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
    
    distances = face_recognition.face_distance(known_face_encodings, unknown_face_encoding)
    best_match_index = np.argmin(distances)
    if distances[best_match_index] < 0.6:  # Threshold for "closeness"
        print(f"Match found: {known_face_names[best_match_index]}")
    else:
        print("No matching face found.")
    
def encode_unknown_face():
    unknown_image_path = "unknown_person.jpg"
    unknown_image = face_recognition.load_image_file(unknown_image_path)
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)
    if unknown_face_encoding:
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    return unknown_face_encoding
        
def encode_known_face(known_face_path):
    global known_face_encodings
    global known_face_names
    global name

    face_image = face_recognition.load_image_file(known_face_path) #Loads image as numpy array
    face_encoding = face_recognition.face_encodings(face_image)
    if face_encoding:
        face_encoding = face_recognition.face_encodings(face_image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(name)  # Remove '.jpg' from filename for name
        print("SUCCESSFULLY ENCODED")
        print("The new saved faces belong to: ")
        print(known_face_names)
    else:
        print("Face Recognition Unsuccessful - Please retry with your full face in the picture.")



face_detector = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")


capture_needed = False  # Flag to indicate when a photo capture is needed


picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)}, lores={"size": (320, 240), "format": "YUV420"})
picam2.configure(config)


(w0, h0) = picam2.stream_configuration("main")["size"]
(w1, h1) = picam2.stream_configuration("lores")["size"]
s1 = picam2.stream_configuration("lores")["stride"]

faces = []
picam2.post_callback = draw_faces


known_faces_dir = "/home/bisher/face_recog_test/known_faces"
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

time.sleep(5)
compare()
