import RPi.GPIO as GPIO
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)
logging.info("GPIO mode set to BCM numbering")

# Set GPIO17 as an output
GPIO.setup(17, GPIO.OUT)
logging.info("GPIO17 set as an output")

# Turn on GPIO17
GPIO.output(17, GPIO.HIGH)
logging.info("GPIO17 turned on")
time.sleep(1)  # Wait for 1 second

# Turn off GPIO17
GPIO.output(17, GPIO.LOW)
logging.info("GPIO17 turned off")

# Clean up GPIO settings
GPIO.cleanup()
logging.info("GPIO cleaned up")
