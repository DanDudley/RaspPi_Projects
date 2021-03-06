import RPi.GPIO as GPIO
import time
wait=0.1
timestoblink=10
#blinking function
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(wait)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(wait)
	return

#to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
# blink GPIO17 50 times
for i in range(0,timestoblink):
	blink(11)
	blink(13)
	print i
GPIO.cleanup()

