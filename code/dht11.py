import Adafruit_DHT

sensor=Adafruit_DHT.DHT11
gpio=4

while True:
    hum, tem = Adafruit_DHT.read_retry(sensor,gpio)
    print(tem)
    print(hum)
    print('----')
