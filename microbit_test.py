# Write your code here :-)
from microbit import *

count = 0
display.show(Image.HAPPY)
sleep(200)

while True:
    display.show(count)
    count += 1
    if count > 9:
        count = 0
    sleep(100)
