import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.IN)

def Main():
	while True:
		if GPIO.input(21):
			data = GPIO.input(21)
		else:
			print("no data")
		time.sleep(0.1)

	GPIO.cleanup()

if __name__ == '__main__':
	Main()
