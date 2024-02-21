import firebase_admin
from firebase_admin import credentials, firestore

# Intilialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Function to add data to a collection (Table) in the FireStore 
def add_data_to_firestore(collection_name : str, data):
    doc_ref = db.collection(collection_name).add(data)
    print("Adding document to collection " + collection_name)
    
    
# Function to get data from a collection (Table) in the FireStore
def get_data_to_firestore(collection_name : str):
     docs = db.collection(collection_name).get()
     # Loop through documents in the firestore
     for doc in docs:
          print(f"Document ID: {doc.id}, Data: {doc.to_dict()}")




