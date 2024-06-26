from machine import Pin
from machine import sleep
import dht

sensor = dht.DHT11(Pin(14))

while True:
    try:
        sleep(2)
        sensor.measure()
        temperatura = sensor.temperature()
        humidity = sensor.humidity()
        temperatura_f = temperatura * (9/5) + 32.0
        print("UPDATE:")
        print("Temperature: %3.1f C" %temperatura)
        print("Temperature: %3.1f F" %temperatura_f)
        print("Humidity: %3.1f %%" %humidity)
    except OSError as e:
        pass