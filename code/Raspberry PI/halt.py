#Step 0: Preamble
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#Program Title  : easy_stepper.py 
#Code Written by: Salty Scott
#Current Project: www.rowboboat.com
#This code is a very basic example of using python to control a spark fun
# easy driver.  The spark fun easy driver that I am using in this example
# is connected to a 42HS4013A4 stepper motor and my raspberry pi.  Pin 23
# is the direction control and pin 24 is the step control.  I am using
# these components in the www.rowboboat.com project version 2.0 and I
# hope someone finds this a useful and simple example.
# This program expects two arguments: direction and steps
# Example usage: sudo python easy_stepper.py left 1600
# The above example would turn a 200 step motor one full revolution as by
# default the easy driver 4.4 is in 1/8 microstep mode. However the stepper driver 
# selected by gtaagii will default to one full step per step pulse, microstepping can
# be selected if desired.
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
#Step 1: Import necessary libraries 
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
#Step 2: Read arguements https://www.youtube.com/watch?v=kQFKtI6gn9Y
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#read the direction and number of steps; if steps are 0 exit  
#print which direction and how many steps 
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 3: Setup the raspberry pi's GPIOs
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#use the broadcom layout for the gpio
gpio.setmode(gpio.BCM)
#GPIO23 = Direction
#GPIO24 = Step
gpio.setup(14, gpio.OUT) #E1
gpio.setup(15, gpio.OUT) #S1
gpio.setup(18, gpio.OUT) #D1
gpio.setup(23, gpio.OUT) #E2
gpio.setup(24, gpio.OUT) #S2
gpio.setup(25, gpio.OUT) #D2
gpio.setup(8, gpio.OUT)  #E3
gpio.setup(7, gpio.OUT)  #S3
gpio.setup(12, gpio.OUT) #D3
#------------------------------------------------------------------------
#------------------------------------------------------------------------


 
#Step 4: Set direction of rotation
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#set the output to true for left and false for right
#if direction == 'left':
gpio.output(25, True)
#    gpio.output(18, False)
#    gpio.output(12, False)
#elif direction == 'right':
    #gpio.output(25, False)
gpio.output(18, True)
gpio.output(12, True)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
# disable all
gpio.output(14, True)
gpio.output(23, True)
gpio.output(8, True)
 
#Step 5: Setup step counter and speed control variables
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#track the numebr of steps taken
StepCounter = 0
 
#waittime controls speed
WaitTime = 0.008
#------------------------------------------------------------------------
#------------------------------------------------------------------------
gpio.output(24,False)
gpio.output(15,False)
gpio.output(7, False) 
#Step 6: Let the magic happen
#------------------------------------------------------------------------
#------------------------------------------------------------------------
# Start main loop
while True:
    time.sleep(1)
    #turning the gpio on and off tells the easy driver to take one step
    #gpio.output(24, True)
    #gpio.output(15, True)
    
    #gpio.output(24, False)
    #gpio.output(15, Fal
    #Wait before taking the next step...this controls rotation speed
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 7: Clear the GPIOs so that some other program might enjoy them
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#relase the GPIO
gpio.cleanup()
#------------------------------------------------------------------------
#------------------------------------------------------------------------