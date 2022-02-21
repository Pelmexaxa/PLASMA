from gpiozero import LED
from time import sleep

outLED = LED(17)

while True:
    outLED.on()
    sleep(1)
    outLED.off()
    sleep(1)