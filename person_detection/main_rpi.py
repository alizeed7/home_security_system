import person_detection as pd
import threading
import time
import argparse

def main(object_detected=False):
    person_detect_thread = threading.Thread(target=pd.main)
    print(object_detected)
    
    if(object_detected == True):
        print('hello')
        person_detect_thread.start()
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--object', action="store_true", help='Specify if object is detected')
    
    args = parser.parse_args()
    
    main(args.object)
