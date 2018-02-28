# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

count = 0
end = 50
lightChannel = 0
threshold = 500
# Main program loop.
while count < end:
	# read light level from pin
	lightVal = mcp.read_adc(lightChannel)

	if (lightVal < threshold):
		print("DARK")
	else:
		print("LIGHT")
	time.sleep(0.1)

