# Write your code here :-)
from microbit import *
import matrix7219

max7219led = matrix7219.Matrix8x8(spi, pin16)
max7219led.brightness(15)

while True:
    display.show(Image.HAPPY)

    max7219led.fill(False)

    max7219led.pixel(2, 2, True)
    max7219led.show()
    sleep(1000)

    max7219led.fill(False)
    max7219led.show()

    display.clear()
    sleep(1000)
