import person_detection as pd
import lighting_control as lc
import threading
import time
import argparse

def main(object_detected=False):

    person_detect_thread = threading.Thread(target=pd.main)
    light_control_thread = threading.Thread(target=lc.main)
    light_control_thread.start()
    
    while(True):
        #object detected so start thread to capture video
        if(object_detected == True):
            person_detect_thread.start()
            person_detect_thread.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--object', action="store_true", help='Specify if object is detected')
    
    args = parser.parse_args()
    
    main(args.object)
