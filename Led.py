from gpiozero import LED
from time import sleep

led = LED(17)  # Change the number to the GPIO pin you're using

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
