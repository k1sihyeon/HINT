from time import sleep
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone

buzzer = TonalBuzzer(3)

scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

try:
    print("Playing scale on buzzer")
    for note in scale:
        buzzer.play(Tone(note))
        sleep(0.5)
        buzzer.stop()
        sleep(0.1)
        
finally:
    buzzer.detach()