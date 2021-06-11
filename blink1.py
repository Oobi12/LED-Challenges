import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

for i in range(0,5): 
    GPIO.output(12,True)
    sleep(0.25)
    GPIO.output(12,False)
    sleep(0.25)