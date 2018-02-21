import RPi.GPIO as GPIO
import time

#set LED port for output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def Main():
	# loop with delay of 0.5s
	count = 0
	while (count < 5):
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.5)
		count = count + 1

	GPIO.cleanup()

	# p = GPIO.PWM(11, 2)
	# p.start(1)
	# input('Press return to stop:')
	# p.stop
	# GPIO.clenup()

if __name__ == '__main__':
	Main()