#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Set GPIO17 as control pin
relayPin2 = 27
relayPin1 = 17

# Define a setup function for some setup
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set relayPin's mode to output,
    # and initial level to High(3.3v)
    GPIO.setup(relayPin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(relayPin2, GPIO.OUT, initial=GPIO.LOW)

# Define a main function for main process
def main():
    
    counter = 0
    max_count = 3
    
    while counter < max_count:
        
        print ('Relay1 open...')
        # Tick
        GPIO.output(relayPin1, GPIO.HIGH)
        time.sleep(2)
        print ('...Relay1 close')
        # Tock
        GPIO.output(relayPin1, GPIO.LOW)
        time.sleep(0.5)

        
        print ('Relay2 open...')
        # Tick
        GPIO.output(relayPin2, GPIO.HIGH)
        time.sleep(2)
        print ('...Relay2 close')
        # Tock
        GPIO.output(relayPin2, GPIO.LOW)
        time.sleep(0.5)
        
        counter += 1
# Define a destroy function for clean up everything after
# the script finished
def destroy():
    # Turn off LED
    GPIO.output(relayPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()                    

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
