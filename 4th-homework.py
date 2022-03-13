# Write your code here :-)
from microbit import *
from random import randint

水果 = ["banana", "apple", "cherry", "grape", "lemon", "papaya", "coconut"]
while True:
    隨機取水果 = randint(0, 6)
    display.scroll(水果[隨機取水果])
    sleep(5000)
