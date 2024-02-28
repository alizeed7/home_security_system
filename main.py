from Firebases import add_data_to_firestore,get_user_from_firestore,get_user_attribute,add_event
from Notification import send_email
from api import add_user,login
def main():
    # Adding Hamdiata Diak`ite as a user in the user collection.
    username = 'hamdiatadiakite'
    data_to_add = {
        'name': 'Hamdiata Diakite',
        'username': username,
        'email': 'hamdiatadiakite@cmail.carleton.ca',
        'phone number' : '819-213-6364',
        'password' : 'SYSC3011'
    }
    
    print(get_user_attribute(username,'email'))
    print(login(username,'SYSC3011'))
    
    event_type = "door_unlocked"
    timestamp = "2024-02-20T12:30:45Z"
    details = {
    "user_id": "user_id_123",
    "door_id": "door_id_456"
    }

    add_event(event_type, timestamp, details)
    
    
   
    
    
    
   
    
    
    
if __name__ == "__main__":
    main()
    
     