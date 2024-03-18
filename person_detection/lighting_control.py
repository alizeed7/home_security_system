from gpiozero import LED
import RPi.GPIO as GPIO
import time

light = LED(24)

photoresistor = 18 #pin 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(photoresistor, GPIO.IN)

while(True):
    if GPIO.input(photoresistor):
        #light
        print("GPIO pin %d is ON" % photoresistor)
        light.off()
    else:
        #dark
        print("it is dark outside")
        light.on() #until specified time (database)
        time.sleep(3)
        light.off()
        time.sleep(5) #so that it wont turn on right after it turned off based on specified time
        
    
