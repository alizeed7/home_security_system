import pyrebase

config = { 
  "apiKey": "AIzaSyA38xl73beUZ1PJkbJvrBq9pJlobgEhEig", 
  "authDomain": "piguardian-bdb7e.firebaseapp.com", 
  "databaseURL": "https://piguardian-bdb7e-default-rtdb.firebaseio.com/", 
  "storageBucket": "piguardian-bdb7e.appspot.com" 
} 

# Connect using your configuration 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 


def add_event(event_type: str, time: str, details: dict):
  '''
  Function that add events to the firebase
  
  Paramaters:
    event_type: String that describes the type of event. 
    time: Time the event happended
    details: Additional details about the event in question 
  
  Returns: 
    None

  '''
  
 
  event_data = {
    'event_type' : event_type,
    'time':time,
    'details':details
   
  }
  new_event = db.child('Events').push(event_data)
  


