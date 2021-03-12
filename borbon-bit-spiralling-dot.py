"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep

pixel = [[0,0],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[4,3],[4,4],[3,4],[2,4],[1,4],[0,4],[0,3],[0,2],[0,1],[1,1],[2,1],[3,1],[3,2],[3,3],[2,3],[1,3],[1,2],[2,2]] # all the coordinates of the micro:bit LED will be stored to a two-dimentional array


while True: # condition that loops infinitely
        for x in range(len(pixel)): # loop that access every index inside the array
                display.set_pixel(pixel[x][0],pixel[x][1],9)# set the  LED in coordinate x in index x to 0 and index x in index 1 and set the brightness of the LED to full brightness which is 9
                sleep(1)#sleep 1 second
                display.clear()# clear the  LED display
