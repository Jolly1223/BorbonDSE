"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
from time import sleep


# clue_data = clue.simple_text_display(title="Message Streamer", title_scale=2, title_color= (255,0,0))


clue_data = clue.simple_text_display(
    title="Message Streamer", 
    title_color= (255,0,0),
    text_scale= 2)

while True:

    clue_data[1].text= "This message moves from right to left"
    clue_data[1].color = clue.YELLOW

    clue_data[3].text= "This message moves from left to right"
    clue_data[3].color = clue.WHITE

    clue_data[5].text= "This message blinks"
    clue_data[5].color = clue.SKY
    sleep(1)
    clue_data[5].color = (0,0,0)

    

    clue_data.show()
