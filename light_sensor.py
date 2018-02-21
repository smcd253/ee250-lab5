import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN)

def Main():
	while True:
		if GPIO.input(23):
			data = GPIO.input(23)
		else
			print("no data")
		time.sleep(0.1)

	GPIO.cleanup()

if __name__ == '__main__':
	Main()
