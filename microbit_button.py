# Write your code here :-)

from microbit import *
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ASLEEP)
    elif button_a.is_pressed():
        display.show("A")
    elif button_b.is_pressed():
        display.show("B")
    sleep(100)
