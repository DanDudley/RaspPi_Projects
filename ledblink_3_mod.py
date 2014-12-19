import RPi.GPIO as GPIO
import time
wait=0.1
timestoblink=10

#channel setup
def channelset(chan):
	GPIO.setup(chan,GPIO.OUT)
	return

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
channelset(11)
channelset(13)
channelset(15)

# blink GPIO17 50 times
for i in range(0,timestoblink):
	blink(11)
	blink(13)
	blink(15)
	print i
GPIO.cleanup()

