from flask import Flask, request, jsonify
from .controller import add_user, login
from flask_cors import CORS
from database import get_user_attribute, add_event


app = Flask(__name__)
CORS(app)

@app.route('/register_user', methods=['POST'])
def add_user_route():
    data = request.json

    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    phone_number = data.get('phone_number')
    password = data.get('password')

    # Attempt to add user and print result for debugging
    try:
        add_user(name, username, email, phone_number, password)
        print("User added successfully.")
        return jsonify({'message': 'User added successfully'})
    except Exception as e:
        print("Error adding user:", e)
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/get_user_attributes', methods=['GET'])
def get_user_attributes_route():
    username = request.args.get('username')
    attribute = request.args.get('attribute')
    # Check if username and attribute are provided
    if not username or not attribute:
        return jsonify({'error': 'Username and attribute must be provided'}), 400

    user_attribute = get_user_attribute(username, attribute)
   

    if user_attribute is None:
        return jsonify({'error': 'User not found or attribute does not exist'}), 404

    # Return the user attribute
    return jsonify({attribute: user_attribute})

@app.route('/add_event', methods=['POST'])
def add_event_route():
    data = request.json
    
    event_type = data.get('event_type')
    details = data.get('details')
    
    # Check if all required fields are provided
    if not event_type or not details:
        return jsonify({'error': 'Missing required field(s)'}), 400
    
    # Call the add_event function from firebase.py
    try:
        add_event(event_type,details)
        return jsonify({'message': 'Event added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.route('/login', methods=['POST'])
def login_route():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    

    # Check if both username and password are provided
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Attempt to log in with username and password
    if login(username, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

if __name__ == "__main__":
    app.run(debug=True)    

    
