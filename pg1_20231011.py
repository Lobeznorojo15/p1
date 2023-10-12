from gpiozero import LED
from time import sleep

led0 = LED(14)
led1 = LED(15)
led2 = LED(16)

while true:
    led0.on()
    led1.on()
    led2.on()
    sleep(1)
    led0.off()
    led1.off()
    led2.off()
    sleep(2)

