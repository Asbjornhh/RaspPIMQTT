import serial
import paho.mqtt.client as mqtt

# Serial port configuration
SERIAL_PORT = 'COM4'  # Change this to your Arduino's serial port
BAUD_RATE = 115200

# MQTT configuration
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "home/sensor/dht11"


# Callback when the message is published
def on_publish(client, userdata, mid):
    print("Message Published...")


# Initialize MQTT client
client = mqtt.Client()
client.on_publish = on_publish
client.connect(BROKER, PORT)
client.loop_start()

# Open the serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()

        # Publish the line to the MQTT broker
        client.publish(TOPIC, line)

except KeyboardInterrupt:
    ser.close()
    client.loop_stop()
    client.disconnect()
