from gpiozero import LED, Button
from signal import pause

led = LED(18) # GPIO pin 18
button = Button(16) # GPIO pin 16

def turn_on_led():
    led.on()
    
def turn_off_led():
    led.off()
    
button.when_pressed = turn_on_led
button.when_released = turn_off_led

print("Waiting for button events. Press Ctrl+C to exit.")

pause()