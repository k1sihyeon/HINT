from gpiozero import Button
from signal import pause

button = Button(16)

def button_pressed():
    print("Button pressed")
    
def button_released():
    print("Button released")
    
    
button.when_pressed = button_pressed
button.when_released = button_released

print("Waiting for button events. Press Ctrl+C to exit.")

pause()