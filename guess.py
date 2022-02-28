# Write your code here :-)
from random import randint

played = True

while played:
    print("===== 歡迎來到剪刀石頭布遊戲 =====")
    user = int(input("請輸入剪刀(0)、石頭(1)、布(2)："))
    guess = randint(0, 2)

    if guess == 0:
        print("電腦出的是剪刀")
    elif guess == 1:
        print("電腦出的是石頭")
    elif guess == 2:
        print("電腦出的是布")
    else:
        print("電腦亂出！")

    if user == guess:
        print("結果是平手！")
    elif (
        (user == 0 and guess == 1)
        or (user == 1 and guess == 2)
        or (user == 2 and guess == 0)
    ):
        print("你輸了QQ")
    elif (
        (user == 0 and guess == 2)
        or (user == 1 and guess == 0)
        or (user == 2 and guess == 1)
    ):
        print("你贏了！^_^")
    else:
        print("是不是你亂出？！")
    user_input = input("要繼續玩嗎 (y/n)?")
    played = (False, True)[user_input == "y"]
