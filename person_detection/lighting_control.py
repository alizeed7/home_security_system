from gpiozero import LED
import RPi.GPIO as GPIO

light = LED(24)

photoresistor = 18 #pin 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(photoresistor, GPIO.IN)

while(True):
    if GPIO.input(photoresistor):
        print("GPIO pin %d is ON" % photoresistor)
        light.off()
    else:
        print("its off")
        light.on()
        
    
