import requests
import time
#import os
import subprocess
#import base64
#import pyrebase


def main():
    #os.system("python3 main_rpi.py --object")
    #wait until main_rpi.py finishes running
    subprocess.Popen(['python3', 'main_rpi.py', '--object']).wait()
    
    # Read video file content
    '''
    with open("test.mp4", "rb") as video_file:
        video_content = video_file.read()
    
    # Base64 encode the video content
    video_content_base64 = base64.b64encode(video_content).decode('utf-8')
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
        
if __name__ == "__main__":
    main()
