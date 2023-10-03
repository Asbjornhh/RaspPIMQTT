import RPi.GPIO as GPIO
import time

# Set the GPIO numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the LED is connected
LED_PIN = 17

# Set the LED_PIN as an output pin
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)  # Keep the LED on for 1 second

        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)  # Keep the LED off for 1 second

except KeyboardInterrupt:
    # If the script is interrupted (e.g., pressing Ctrl+C), turn off the LED and cleanup the GPIO
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
