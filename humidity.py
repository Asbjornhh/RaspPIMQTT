import Adafruit_DHT
import time  # <-- import the time module

# Sensor type
DHT_SENSOR = Adafruit_DHT.DHT11
# GPIO pin number (not the physical pin number)
DHT_PIN = 23

while True:  # <-- start an infinite loop
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from the sensor")

    time.sleep(2)  # <-- delay for 2 seconds before the next read
