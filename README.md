[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/5bxZGXM7)
### README
### PiGuardian Project (SYSC 3010)
### Group number: L2-G6
### Students: Bisher Abou-Alwan, Hamdiata Diakite, Alizée Drolet, Yousef Hammad
### TA: Oly Papillon
___
**About**

   This project is about ....

**Directory Map**
   - Demo: 
   - FaceRecognition:
     - This directory represents the facial recognition component needed to detect, scan, and encode a face.
     - It also handles the local database by calling local_database.py function implcitly from facial_recognition.py to update DB
     - The directory also includes the doorbell.py code to handle doorbell requests to scan a face
     - This contains a unit_test sub directory that provides a thorough functonal test to each method
   - Notification:
   - WeeklyUpdates:
     - This directory includes weekly individual reports from week 3 to week 12 of the course.
   - api:
   - database:
   - person_detection
     - This directory handles the person_detection, proximity sensing, and lighting control of the project.
     - Includes test code for end to end testing, person detection testing, and lighting control testing.
   - yousef-test

**Installation Instructions**
   - Please install the following libraries and dependencies:
     - To install Pyrebase: 'pip3 install pyrebase'
     - To install OpenCV: 'pip3 install opencv-python'
     - To install Facial Recognition: 'pip3 install facial_recognition-python'
     - To install Numpy: 'pip3 install numpy'
     - To install SQLite3: 'sudo apt-get install sqlite3'

**How to run**
   - meow

**Validate Installation**
   - To validate installations, please follow 2 stages. Stage 1 represents the unit tests, please run each node's unit test and verify that all tests pass. Stage 2    represents real-time functionality where we exercise the system, please register a user on the GUI, register a face, verify the door lock status, test the doorbell by scanning an unregistered face to verify status remains locked, test the doorbell by scanning an registered face to verify status becomes unlocked , provide motion in front of the proximity sensors and verify motion detection videos are uploaded on the GUI, and lastly provide darkness above the light sensory to verify the LED turns on upon detecting darkness.
   
