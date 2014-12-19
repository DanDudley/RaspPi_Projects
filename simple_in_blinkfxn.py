import RPi.GPIO as GPIO
import time
wait=0.2
timestoblink=10

#channel setup
##output
def channelout(chan):
	GPIO.setup(chan,GPIO.OUT)
	return
##input
def channelin(chan):
        GPIO.setup(chan,GPIO.IN,GPIO.PUD_UP)
        return

#blinking functions
##simple
def blink(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(wait)
	GPIO,output(pin,GPIO.LOW)
	time.sleep(wait)
	return

##advanced
def blink_adv(pin,blinkcount,changetime):
        for i in range (0,blinkcount):
                GPIO.output(pin,GPIO.HIGH)
                time.sleep(changetime)
                GPIO.output(pin,GPIO.LOW)
                time.sleep(changetime)
                print(i)
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
			blink_adv(11,5,.2)
			blink_adv(13,10,.10)
			blink_adv(15,15,.05)
			print('Button Pressed')
			time.sleep(wait)
except KeyboardInterrupt:  
	print('Keyboard Interrupted Me!')

except: 
	print('Other Error Occured!')

finally:
	GPIO.cleanup()	




