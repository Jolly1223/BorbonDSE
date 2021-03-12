"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""
import time
from adafruit_circuitplayground import cp
from time import sleep
# value = 320
while True: 
    if(cp.light <= 32): #condition that if cp.light is less than or equal to 32 then it will execute the below code 
       cp.pixels[0] = (cp.light, cp.light, cp.light) # the cp.pixels index 0 will light up and with increasing/decreasing power
       cp.pixels[1] = (0,0,0) # cp.pixels index 1 will not light up
    elif(cp.light <= 64 ): #condition that if cp.light is less than or equal to 64 then it will execute the program below
        cp.pixels[1] = (cp.light-32, cp.light-32, cp.light-32) # the cp.pixels index 1 will light up with increasing/decreasing power
        cp.pixels[2] = (0,0,0)#cp.pixels index 2 will not light up
    elif(cp.light <= 96 ):#condition that if cp.light is less than or equal to 96 then it will execute the below code
        cp.pixels[2] = (cp.light-64, cp.light-64, cp.light-64)#the cp.pixels index 2 will light up with increasing/decreasing power
        cp.pixels[3] = (0,0,0)#cp.pixels index 3 will not light up
    elif(cp.light <= 128 ):#condition that if cp.light is less than or equal to 128 then it will execute the below code
        cp.pixels[3] = (cp.light-96, cp.light-96, cp.light-96)#the cp.pixels index 3 will light up with increasing/decreasing power
        cp.pixels[4] = (0,0,0)#cp.pixels index 4 will not light up
    elif(cp.light <= 160 ):#condition that if cp.light is less than or equal to 160 then it will execute the below code
        cp.pixels[4] = (cp.light-128, cp.light-128, cp.light-128)#the cp.pixels index 4 will light up with increasing/decreasing power
        cp.pixels[5] = (0,0,0)#cp.pixels index 5 will not light up
    elif(cp.light <= 192 ):#condition that if cp.light is less than or equal to 192 then it will execute the below code
        cp.pixels[5] = (cp.light-160, cp.light-160, cp.light-160)#the cp.pixels index 5 will light up with increasing/decreasing power
        cp.pixels[6] = (0,0,0)#cp.pixels index 6 will not light up
    elif(cp.light <= 224 ):#condition that if cp.light is less than or equal to 224 then it will execute the below code
        cp.pixels[6] = (cp.light-192, cp.light-192, cp.light-192)#the cp.pixels index 6 will light up with increasing/decreasing power
        cp.pixels[7] = (0,0,0)#cp.pixels index 7 will not light up
    elif(cp.light <= 256 ):#condition that if cp.light is less than or equal to 256 then it will execute the below code
        cp.pixels[7] = (cp.light-224, cp.light-224, cp.light-224)#the cp.pixels index 7 will light up with increasing/decreasing power
        cp.pixels[8] = (0,0,0)#cp.pixels index 8 will not light up
    elif(cp.light <= 288 ):#condition that if cp.light is less than or equal to 288 then it will execute the below code
        cp.pixels[8] = (cp.light-256,cp.light-256, cp.light-256)#the cp.pixels index 8 will light up with increasing power
        cp.pixels[9] = (0,0,0)#cp.pixels index 9 will not light up
    elif(cp.light <= 320 ):#condition that if cp.light is less than or equal to 320 then it will execute the below code
        cp.pixels[9] = (cp.light-288, cp.light-288, cp.light-288)#the cp.pixels index 9 will light up with increasing/decreasing power

