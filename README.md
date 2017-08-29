## pi-pin-play.py Play audio on pin high
This is a small script for playing audio when a pin is pulled high. 

### Dependencies
* Python 3
* pygame
* RPi-GPIO


### Notes:
* Your user needs acces to GPIO and audio output. Root might not have access to audio.
* Pinning is configured in the pi-pin-play.py file.
* Make sure the audio levels are turned up, you might want to use alsamixer for this.
