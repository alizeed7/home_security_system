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

