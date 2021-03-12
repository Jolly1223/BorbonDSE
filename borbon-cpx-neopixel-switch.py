# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
 
"""This example prints the status of the slide switch. Try moving the switch back and forth to see
what's printed to the serial console!"""
from time import sleep
from adafruit_circuitplayground import cp
import time
 

a = 9 #declare variable
while True: #condition that loops the program endlessly

   if cp.switch == False:        #by default the switch is false then it will execute the code
        cp.pixels[a] = (255,0,0) #the pixels will light up
        sleep(.5)                #sleep
        cp.pixels[a] = (0,0,0)   
        a-=1                     #it will decrement
        if a == -1:              #if a is equal to -1 the value of a will set back to 9 or to index 9pP
          a = 9                  
   elif cp.switch == True:       #then if the switch becomes true it will execute the following code
        cp.pixels[a] = (255,0,0) #the pixels will light up
        sleep(.5)                #sleep
        cp.pixels[a] = (0,0,0)   
        a+=1                     #increment
        if a == 9:               #if a is equal to 9 then the value of a will set back to -1 or to index 0
          a = -1                 
        


         
