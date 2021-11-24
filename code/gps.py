#$GPGGA,164045.000,6008.8305,N,02458.5444,E,1,8,0.95,-52.2,M,19.5,M,,*45


import os
import serial
import pynmea2

port = "/dev/ttyUSB0"

serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
    s = serialPort.readline().decode('utf-8')
    if '$GPGGA' in s:
     #print(s)
     s=s.replace('\n','').split(',')
     lon=f'{float(s[2])/100:0.4f} {s[3]}'
     lat=f'{float(s[4])/100:0.4f} {s[5]}'
     above_sea=f'{float(s[9]):0.1f} {s[10]}'
     os.system('clear')
     print('Longitude: ',lon)
     print('Latitude:  ',lat)
     print('Above mean sea level: ',above_sea)
