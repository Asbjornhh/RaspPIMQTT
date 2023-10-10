import paho.mqtt.client as mqtt
from RPi import GPIO
from time import sleep
from ssl import SSLContext, PROTOCOL_TLS_CLIENT, CERT_REQUIRED

# Azure IoT Hub Configuration
IOT_HUB_NAME = "myldriothub.azure-devices.net"
IOT_HUB_DEVICE_ID = "rotaryencoder"
IOT_HUB_SAS_TOKEN = "SharedAccessKey=ZBy99v4PLRM6k+rsEb39gZqmisipMZTS8AIoTFekOeQ="

# Rotary Encoder Configuration
clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

# Callbacks
def on_connect(mqtt_client, obj, flags, rc):
    print("Connected with result code: " + str(rc))

def on_publish(mqtt_client, obj, mid):
    print("Message Published: " + str(mid))

mqtt_client = mqtt.Client(client_id=IOT_HUB_DEVICE_ID, protocol=mqtt.MQTTv311)
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

mqtt_client.username_pw_set(username=IOT_HUB_NAME + ".azure-devices.net/" + IOT_HUB_DEVICE_ID + "/?api-version=2021-04-12",
                            password=IOT_HUB_SAS_TOKEN)

ssl_context = SSLContext(protocol=PROTOCOL_TLS_CLIENT)
ssl_context.load_default_certs()
ssl_context.verify_mode = CERT_REQUIRED
ssl_context.check_hostname = True
mqtt_client.tls_set_context(context=ssl_context)

mqtt_client.connect(host=IOT_HUB_NAME + ".azure-devices.net", port=8883, keepalive=120)
mqtt_client.loop_start()

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter += 1
            print(counter)
            # Publish the counter value to the Azure IoT Hub
            mqtt_client.publish("devices/" + IOT_HUB_DEVICE_ID + "/messages/events/", payload=str(counter), qos=1)
        clkLastState = clkState
        sleep(0.01)
finally:
    GPIO.cleanup()
    mqtt_client.disconnect()
