import RPi.GPIO as GPIO
import time
wait=input('Enter Blink speed:')
timestoblink=input('Enter desired number of blinks:')
proceed=input('Proceed? (1=start or 0=stop)')

#blinking function
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(wait)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(wait)
	return
if proceed==0:
	GPIO.cleanup()
else:

#to use Raspberry Pi board pin numbers
	GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
	GPIO.setup(11,GPIO.OUT)
# blink GPIO17 50 times
	for i in range(0,timestoblink):
		blink(11)
		print i

	GPIO.cleanup()
	print 'Allison is beautiful!'
