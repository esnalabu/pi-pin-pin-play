#!/bin/python3
# Author: Anders Myren
# This is a small script for playing audio when a pin is pulled high.

import RPi.GPIO as GPIO
import pygame
from time import sleep

# Setup input pin
inputpin = 18	# Pin used for triggering
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define functions

def play_audio():
    print("Playing audio file...")
    pygame.mixer.init()
    pygame.mixer.music.load("myFile.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Done playing audio file!")

# Start listening for events
GPIO.add_event_detect(inputpin, GPIO.RISING)

# Run, check for new status 
if __name__ == "__main__":
    while True:
        if GPIO.input(inputpin):
            print('Input was HIGH')
            play_audio()
        else:
            print('Input was LOW')
        sleep(1)
