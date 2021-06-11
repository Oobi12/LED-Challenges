import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)

while True:
    GPIO.output(17,True)
    sleep(0.25)
    GPIO.output(17,False)
    sleep(0.25)
    GPIO.output(18,True)
    sleep(0.25)
    GPIO.output(18,False)
    sleep(0.25)
    GPIO.output(13,True)
    sleep(0.25)
    GPIO.output(13,False)
    sleep(0.25)
    
   