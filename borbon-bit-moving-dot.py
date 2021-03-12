"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""
from microbit import *
from time import sleep
while True: #condition that loops the program infinitely
    for y in range(5): #it will execute the loop five times
        for x in range (5): # will execute the loop five times
            display.set_pixel(x,y,9) # this will set the LED x and y to a brightness of 9
            sleep(1) #sleep in 1 second
            display.clear() #this is to clear the LED display