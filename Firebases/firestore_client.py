import firebase_admin
from firebase_admin import credentials, firestore

# Intilialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
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
    Function to get user data based on usernmae
    
    Paramaters:
    Username: username of the user
    
    Returns:
    Error if username is not found, user data if it is found
    '''
    
    try:
        user_reference = db.collection('Users').document(username)
        return user_reference.get().to_dict()
    except Exception as error:
        print("Error getting user")
        return None
        
        
        
    
    

def get_data_to_firestore(collection_name : str):
    '''
    Function to print data from firestore collection
    
    Parameters:
     collection_name: Name of the firestore collection where the data is to be retreived
    
    '''
    docs = db.collection(collection_name).get()
     # Loop through documents in the firestore
    for doc in docs:
        print(f"Document ID: {doc.id}, Data: {doc.to_dict()}")




