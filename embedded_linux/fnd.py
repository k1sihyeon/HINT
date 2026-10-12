from time import sleep
from gpiozero import LEDCharDisplay
from gpiozero.pins.lgpio import LGPIOFactory

factory = LGPIOFactory(chip=0)

# BCM GPIO 순서: a, b, c, d, e, f, g, dp
display = LEDCharDisplay(
    17, 18, 27, 22, 23, 24, 25, dp=5,
    active_high=True, pin_factory=factory
)

try:
    while True:
        for number in "0123456789A":
            display.value = number
            sleep(1)
            
except KeyboardInterrupt:
    pass

finally:
    display.off()
    display.close()
    factory.close()