import time
import board
import adafruit_vl53l1x as af

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