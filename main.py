from Firebases import add_data_to_firestore, get_data_to_firestore

def main():
    # Adding Hamdiata Diakite as a user in the user collection.
    data_to_add = {
        'name': 'Hamdiata Diakite',
        'username': 'hamdiatadiakite',
        'email': 'hamdiatadiakite@cmail.carleton.ca',
        'phone number' : '819-213-6364',
        'password' : 'SYSC3011'
    }
    
    
    add_data_to_firestore('Users',data_to_add)
    get_data_to_firestore('Users')
    
    
    
if __name__ == "__main__":
    main()
    
    