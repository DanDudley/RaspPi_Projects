import RPi.GPIO as GPIO
import time
wait=0.2
timestoblink=10

#channel setup
#output
def channelout(chan):
	GPIO.setup(chan,GPIO.OUT)
	return

#input
def channelin(chan):
	GPIO.setup(chan,GPIO.IN,GPIO.PUD_UP)
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
channelin(16)
channelout(11)
channelout(13)
channelout(15)


#inputtest
try:
	while True:
		input_state=GPIO.input(16)
		if input_state==False:
			blink(11)
			blink(13)
			blink(15)
			print('Button Pressed')
			time.sleep(wait)
except KeyboardInterrupt:  
	print('Keyboard Interrupt')

except: 
	print('Other Error Occured!')

finally:
	GPIO.cleanup()	
# blink GPIO17 50 times
#for i in range(0,timestoblink):
#	blink(11)
#	blink(13)
#	blink(15)
#	print i

