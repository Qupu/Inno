import time
import board
import busio
import adafruit_adxl34x

i2c = board.I2C()
accelerometer = adafruit_adxl34x.ADXL345(i2c,0x1d)


accelerometer.enable_freefall_detection(threshold=10, time=25)
accelerometer.enable_motion_detection(threshold=18)
accelerometer.enable_tap_detection(tap_count=2, threshold=30, duration=50)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    print("Dropped: %s"%accelerometer.events["freefall"])
    print("Tapped: %s"%accelerometer.events['tap'])
    print("Motion detected: %s"%accelerometer.events['motion'])
    time.sleep(0.5)
