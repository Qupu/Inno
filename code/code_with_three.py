import os
import serial
import pynmea2
import threading
import time
import board
import busio
import adafruit_adxl34x
import Adafruit_DHT

def printter():
    while True:
     time.sleep(5)
     
     tlon=lon
     tlat=lat
     tabove_sea=above_sea
     taccel=accel
     tmoti=moti
     ttem=tem
     thum=hum
     ttapp=tapp

     os.system('clear')
     print(f'\n-----------------------------------------\n\nLongitude: {tlon}\nLatitude:  {tlat}\nAbove mean sea level: {tabove_sea}\n\n-----------------------------------------\n\n{taccel}\nMotion detected: {tmoti}\nHit detected:    {ttapp}\n\n-----------------------------------------\n\nTemarature: {ttem}C\nHumidity: {thum}%\n\n-----------------------------------------')


     with open("log.txt", 'a') as file:
         file.write(f'{tlon};{tlat};{tabove_sea};{taccel};{tmoti};{ttapp};{ttem};{thum}\n')




def gps():
    global lon
    global lat
    global above_sea
    port = "/dev/ttyUSB0"
    serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)

    while True:
        s = serialPort.readline().decode('utf-8')
        if '$GPGGA' in s:
         s=s.replace('\n','').split(',')
         if s[4]:
            lon=f'{float(s[2])/100:0.4f} {s[3]}'
            lat=f'{float(s[4])/100:0.4f} {s[5]}'
            above_sea=f'{float(s[9]):0.1f} {s[10]}'
         else:
            lon='No FIX'
            lat='No FIX'
            above_sea='No FIX'

def acc():
    global accel
    global moti
    global tapp

    i2c = board.I2C()
    acce = adafruit_adxl34x.ADXL345(i2c,0x1d)
    acce.enable_freefall_detection(threshold=10, time=25)
    acce.enable_motion_detection(threshold=18)
    acce.enable_tap_detection(tap_count=1, threshold=10, duration=500)
    
    while True:
        accel=acce.acceleration
        moti=acce.events['motion']
        tapp=acce.events['tap']

def temp():
    global hum
    global tem

    sensor=Adafruit_DHT.DHT11
    gpio=4

    while True:
     hum, tem = Adafruit_DHT.read_retry(sensor,gpio)


lon=""
lat=""
above_sea=""
accel=None
tem=None
hum=None
moti=False


with open("log.txt", 'a') as file:
         file.write(f'lon;lat;above_sea;accel;moti;tapp;tem;hum\n')

t1 = threading.Thread(target=printter)
t2 = threading.Thread(target=gps)
t3 = threading.Thread(target=acc)
t4 = threading.Thread(target=temp)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()




