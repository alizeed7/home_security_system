import threading
import time
from datetime import datetime
import argparse
import board
import adafruit_vl53l1x as af
import person_detection as pd
import lighting_control as lc
import sys
sys.path.insert(1, '/home/alizeedrolet/sysc3010-project-l2-g6/database')
from firebase import upload_file_to_storage

def main(object_detected):
    
    light_control_thread = threading.Thread(target=lc.main)
    light_control_thread.start()
    
    while(True):
        #object_detected = prox_sensor()
        #object detected so start thread to capture video
        if(object_detected == True):
            person_detect_thread = threading.Thread(target=pd.main)
            person_detect_thread.start()
            
            #send video to db
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            filename = timestamp + '.mp4'
            upload_file_to_storage('/home/alizeedrolet/sysc3010-project-l2-g6/person_detection/test.mp4', filename)
    
            person_detect_thread.join()


def prox_sensor():
    i2c = board.I2C()
    vl53 = af.VL53L1X(i2c)
    vl53.distance_mode = 2 #long mode (1 for short mode)
    vl53.timing_budget = 100

    vl53.start_ranging()

    while True:
        if vl53.data_ready:
            print("Distance: {} cm".format(vl53.distance))
            vl53.clear_interrupt()
            time.sleep(1.0)
            
            if(vl53.distance < 300):
                return True
            
            
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--object', action="store_true", help='Specify if object is detected')
    
    args = parser.parse_args()
    
    main(args.object)
   
    #main()
