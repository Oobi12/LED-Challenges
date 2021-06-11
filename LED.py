import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)

while True:
    GPIO.output(18,True)
    sleep(0.25)
    GPIO.output(18,False)
    sleep(0.25)