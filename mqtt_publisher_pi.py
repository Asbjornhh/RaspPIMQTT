import Adafruit_DHT
import paho.mqtt.client as mqtt
import time

# DHT11 setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 23

# MQTT setuppip
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "home/sensor/dht11"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        payload = f"Temperature: {temperature}C, Humidity: {humidity}%"
        client.publish(MQTT_TOPIC, payload)
        time.sleep(3)
    else:
        print("Failed to retrieve data from sensor")
