from database import add_data_to_firestore, get_user_from_firestore, get_user_attribute, add_event
from Notification import send_email
from api import add_user, login
import requests
import time

def main():
    event_data = {
        "event_type": "Proximity Sensor triggered",
        "details":{
                "key1": "value1"
                "key2": "value2"            
            }     
        
        }

url_POST = 'http://127.0.0.1:5000/add_event'

print("Making POST request")
time.sleep(1)
response = requests.post(url_POST, json=event_data)
if response.status_code == 200:
       print("POST request sucessful, user added to database")
    
else:
    print(response.status_code)
    
    time.sleep(1)