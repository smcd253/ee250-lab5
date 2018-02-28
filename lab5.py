# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import RPi.GPIO as GPIO

#set LED port for output
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

count = 0
end = 50
lightChannel = 0
soundChannel = 1
soundThresh = 600
lightThresh = 500
ledOn = False

# Main program loop.
while True:
	#p1
	print("Part1: blink led 5 times every 500ms")
	count = 0
	while (count < 5):
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.5)
		count = count + 1
	
	#p2
	print("Part2: read light sensor every 100ms")
	count = 0
	while count < end:
		# read light level from pin
		lightVal = mcp.read_adc(lightChannel)

		if (lightVal < lightThresh):
			print("DARK")
		else:
			print("LIGHT")
		count = count + 1
		time.sleep(0.1) # sleep 100ms

	#p3
	count = 0
	print("Part3: blink led 4 times every 200ms")
	while (count < 4):
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.2) # hold on for 200ms
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.2) # hold off for 200ms
		count = count + 1

	#p4
	count = 0
	print("Part4: control led with sound sensor for 5 seconds (100ms intervals)")
	while count < end:
		# read light level from pin
		soundVal = mcp.read_adc(soundChannel)
		print("soundVal = " + str(soundVal))

		if (soundVal > soundThresh):
			ledOn = True

		if ledOn:
			GPIO.output(11, GPIO.HIGH)
		else:
			GPIO.output(11, GPIO.LOW)

		count = count + 1
		ledOn = False
		time.sleep(0.1) # sleep 100ms	

	
	#p5
	count = 0
	print("Part5: blink led 4 times every 200ms")
	while (count < 4):
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.2) # hold on for 200ms
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.2) # hold off for 200ms
		count = count + 1

