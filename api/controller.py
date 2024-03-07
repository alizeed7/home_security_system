from database import add_data_to_firestore, get_user_from_firestore,get_user_attribute
    
def add_user(name: str, username: str, email: str, phone_number: str, password: str):
    '''
    Function to add user to the 'Users' collection in the firestore. 
    Parameters: 
        name: Name of the user to be added 
        username: Username of the user to be added 
        email: email if the user to be added
        phone: Phone number of rhe user to be added 
        password: Password of the email to be added
    '''
    user_info = {
        'name': name,
        'username': username,
        'email': email,
        'phone_number': phone_number,
        'password': password
    }
    
    # Call function from Firebases to add user with username as doc id
    add_data_to_firestore('Users',user_info,username)
    
def login(username: str, password: str) -> bool:
        
    user_data = get_user_from_firestore(username)
    
    if user_data is not None:
        #Get password stored in firebase
        user_password = get_user_attribute(username,'password')
        # Check to see if stored password and password enters match
        if user_password == password:
            return True
        
        else:
            return False
    else:
        return False
        
        
        
        
        