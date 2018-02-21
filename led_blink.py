import RPi.GPIO as GPIO
import time

#set LED port for output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(0, GPIO.OUT)

def Main():
	# loop with delay of 0.5s
	# while True:
	# 	GPIO.output(17, GPIO.HIGH)
	# 	time.sleep(0.5)
	# 	GPIO.output(17, GPIO.LOW)
	# 	time.sleep(0.5)

	# GPIO.cleanup()

	p = GPIO.PWM(0, 0.125)
	p.start(1)
	input('Press return to stop:')
	p.stop
	GPIO.clenup()

if __name__ == '__main__':
	Main()