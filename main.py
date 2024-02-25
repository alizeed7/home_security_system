from Firebases import add_data_to_firestore, get_data_to_firestore,get_user_from_firestore
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
    
    print(login('hamdiata','SYSC3011'))
    
    
   
    
    
    
if __name__ == "__main__":
    main()
    
     