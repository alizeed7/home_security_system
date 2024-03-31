import requests
import time
from datetime import datetime
#import os
import subprocess

import sys
sys.path.insert(1, '/home/alizeedrolet/sysc3010-project-l2-g6/database')
from firebase import upload_file_to_storage
#import base64
#import pyrebase


def main():
    #os.system("python3 main_rpi.py --object")
    #wait until main_rpi.py finishes running
    subprocess.Popen(['python3', 'person_detection.py']).wait()
    
    # Read video file content
    
    with open("test.mp4", "rb") as video_file:
        video_content = video_file.read()
    
    # Base64 encode the video content
    #video_content_base64 = base64.b64encode(video_content).decode('utf-8')
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    filename = timestamp + '.mp4'
    upload_file_to_storage('/home/alizeedrolet/sysc3010-project-l2-g6/person_detection/test.mp4', filename)
    
    '''
    event_data = {
        "event_type": "Proximity Sensor triggered",
        "details":{
                "test": "hello"          
            }     
        
        }
    print('data is ok')
    #close file
    #event_data["details"]["test.mp4"].close()

    url_POST = 'http://172.17.82.143:5000/add_event'

    print("Making POST request")
    time.sleep(1)
    response = requests.post(url_POST, json=event_data)
    
    # Check response status
    if response.status_code == 200:
       print("POST request sucessful, user added to database")
    
    else:
        print(response.status_code)
        
        time.sleep(1)
    '''
        
if __name__ == "__main__":
    main()
