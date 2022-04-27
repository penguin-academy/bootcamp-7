#
"""
    https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api
    https://roboticadiy.com/how-to-blink-led-with-raspberry-pi-4/
"""
import RPi.GPIO as GPIO 
import time

LED_PIN = 2 #BCM
# LED_PIN = 3 #BOARD


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
# GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW) 


while True:
    GPIO.output(LED_PIN, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_PIN, GPIO.LOW) 
    time.sleep(1)