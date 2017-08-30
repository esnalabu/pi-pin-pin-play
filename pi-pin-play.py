#!/bin/python3
# Author: Anders Myren
# This is a small script for playing audio when a pin is pulled high.

import os
import RPi.GPIO as GPIO
import pygame
from time import sleep

# Set audio file
audiofile = (os.path.dirname(os.path.realpath(__file__)) + "/myFile.wav")

# Setup input pin
inputpin = 18	# Pin used for triggering
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define functions

def play_audio():
    print("Playing audio file...")
    pygame.mixer.init()
    pygame.mixer.music.load(audiofile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        sleep(3)
        if GPIO.wait_for_edge(inputpin, GPIO.FALLING):
            print('Aborting playing audio file!')
            pygame.mixer.music.stop()
        else: 
            continue
    print("Done playing audio file!")
    sleep(5)

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
