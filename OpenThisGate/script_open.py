#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

def open():
	output_pin = 7

	GPIO.setboard(GPIO.ZERO)    # Orange Pi PC board
	GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
	GPIO.setup(output_pin, GPIO.OUT)         # set BCM7 (pin 26) as an output (LED)

	GPIO.output(output_pin, 1)       # set port/pin value to 1/HIGH/True
	sleep(3)
	GPIO.output(output_pin, 0)       # set port/pin value to 0/LOW/False
	GPIO.cleanup()              # Clean GPIO
