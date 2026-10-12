from gpiozero import LED

led = LED(18) # GPIO pin 18

while True:
    number_input = input("Enter a number (0 to turn off, 1 to turn on): ")
    
    if number_input == '1':
        led.on()
        print("LED is ON")
        
    if number_input == '0':
        led.off()
        print("LED is OFF")