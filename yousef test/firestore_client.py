import firebase_admin
from firebase_admin import credentials, firestore

# Intilialize Firebase
#cred = credentials.Certificate("/Users/hamdiatadiakite/Desktop/Winter 2024/SYSC 3010/sysc3010-project-l2-g6/serviceAccountKey.json")
#cred = credentials.Certificate("/Users/youse/Desktop/Sysc 3010 GUI/serviceAccountKey.json")
cred = credentials.Certificate("/home/yousef/Downloads/Sysc 3010 GUI/serviceAccountKey.json")



firebase_admin.initialize_app(cred)
db = firestore.client()


def add_data_to_firestore(collection_name: str, data: dict, doc_id: str):
    '''
    Function to add data to firestore
    
    Paramaters: 
        collection_name: Name of the firestore collection where the data is to be added
        data: Data to be added 
        Doc_ID: Unique ID of the document 
    

    '''
    try:
        doc_ref = db.collection(collection_name).document(doc_id)
        doc_ref.set(data)
    except Exception as error:
        print("Error adding data to firestore")
    
    
    
    
def get_user_from_firestore(username: str):
    '''
    Function to get user data based on usernmae.The username serves as the document id in the Users collection
    
    Paramaters:
        Username: username of the user
    
    Returns:
        Error if username is not found, returns user data if it is found
    '''
    
    try:
        user_reference = db.collection('Users').document(username)
        return user_reference.get().to_dict()
    except Exception as error:
        print("Error getting user")
        return None
            
        
def get_user_attribute(username: str,attribute: str) ->str:
    '''
    Function returns user attribute based on the username. The username serves as the document id in the Users collection
    Parameters:
        username: Username of the user
        attribute: Attribute to be returned. Options are name, username, email, phone number, password
    
    Returns: 
        Attribute value of the user sotred in the firetore. None if the user not found or a eception is raised 
    
    '''
        
    try:
        user_reference = db.collection('Users').document(username)
        user_data = user_reference.get()
        if user_data.exists:
            user_dict = user_data.to_dict()
            return user_dict.get(attribute)
        else:
            return None
    except Exception as error:
        print("Error getting user")
        return None
    


def get_user_names(username: str):
    try:
        # user_reference = db.collection('Users').document(username)
        # user_data = user_reference.get()
        # if user_data.exists:
        #     user_dict = user_data.to_dict()
        #     return user_dict.get(attribute)
        # else:
        #     return None
        return db.collection('Users').document(username).get().to_dict()
    except Exception as error:
        print("Error getting user")
        return None


    

        
            
    




