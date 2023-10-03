from gpiozero import Button
from signal import pause

def pressed():
    print("Button pressed!")

button = Button(27)
button.when_pressed = pressed

pause()