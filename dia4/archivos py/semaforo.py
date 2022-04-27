import RPi.GPIO as GPIO 
import time

LED_Azul = 16
LED_Rojo = 20
LED_Verde = 21

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_Azul , GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_Rojo , GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(LED_Verde, GPIO.OUT, initial=GPIO.LOW) 
    
while True:
    GPIO.output(LED_Rojo, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_Rojo, GPIO.LOW) 
    time.sleep(1)
    
    GPIO.output(LED_Rojo, GPIO.HIGH)
    GPIO.output(LED_Verde, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(LED_Rojo, GPIO.LOW)
    GPIO.output(LED_Verde, GPIO.LOW)
    
    time.sleep(1)
    GPIO.output(LED_Verde, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_Verde, GPIO.LOW) 
    time.sleep(1)