from database import add_data_to_firestore, get_user_from_firestore, get_user_attribute, add_event
from Notification import send_email
from api import add_user, login
import requests

def main():
    event_data = {
        "event_type": "sample_event",
        "details": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    
    
data = {
    'username': 'hamdiatadiakite',
    'password': 'SYSC3010'  # Replace 'your_password_here' with the actual password
}

URL = 'http://127.0.0.1:5000/login'

# Make a POST request to the login route with the username and password in the body
response = requests.post(URL, json=data)

    


   


    
    
   

    

if __name__ == "__main__":
    main()