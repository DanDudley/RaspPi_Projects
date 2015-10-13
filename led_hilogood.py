import RPi.GPIO as GPIO
import time


#to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
# blink GPIO17 50 times
for i in range(0,timestoblink):
	blink(11)
	blink(13)
	blink(15)
	print i
GPIO.cleanup()

