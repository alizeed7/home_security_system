import pyrebase
from datetime import datetime


config = { 
  "apiKey": "AIzaSyA38xl73beUZ1PJkbJvrBq9pJlobgEhEig", 
  "authDomain": "piguardian-bdb7e.firebaseapp.com", 
  "databaseURL": "https://piguardian-bdb7e-default-rtdb.firebaseio.com/", 
  "storageBucket": "piguardian-bdb7e.appspot.com" 
} 

# Connect using your configuration 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 


def add_event(event_type: str, details: dict):
  '''
  Function that add events to the firebase
  
  Paramaters:
    event_type: String that describes the type of event. 
    details: Additional details about the event in question 
  
  Returns: 
    None

  '''
  
  now = datetime.now()
  

  # Format as a string, if desired
  timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
  
 
  event_data = {
    'event_type' : event_type,
    'time':timestamp_str,
    'details':details
   
  }
  new_event = db.child('Events').push(event_data)
  


