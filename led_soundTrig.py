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
threshold = 600
ledOn = False

# Main program loop.
while count < end:
	# read light level from pin
	soundVal = mcp.read_adc(soundChannel)
	print("soundVal = " + str(soundVal))

	if (soundVal > threshold):
		ledOn = True

	if ledOn:
		GPIO.output(11, GPIO.HIGH)
		ledOn = False
	else:
		GPIO.output(11, GPIO.LOW)

	time.sleep(0.1)
	count = count + 1

