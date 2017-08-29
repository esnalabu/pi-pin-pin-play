#!/bin/python3
# Author: Anders Myren
# This script is for controlling a Venset TV-lift using power from an USB-port as trigger. Add a pulldown resistor between inputpin and common/ground/0V.

import RPi.GPIO as GPIO
import pygame
from time import sleep

# Set input and output pins
inputpin = 18	# Pin used for triggering lift
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define functions raising and lowering TV-lift

def my_callback(pin):
    print 'Movment! '

def play_audio():
    print("Playing audio file ", raiseduration, "s..."  )
    pygame.mixer.init()
    pygame.mixer.music.load("myFile.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Done playing audio file!"  )

# Setting up
GPIO.add_event_detect(inputpin, GPIO.RISING)

# Run, check for new status, raise/lower on change, sleep for stability
if __name__ == "__main__":
    while(True):
        if GPIO.event_detected(inputpin):
            print 'Detect!'
