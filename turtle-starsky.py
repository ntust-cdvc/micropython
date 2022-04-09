# Write your code here :-)
from turtle import *
from random import randint

# 指定畫布的尺寸(寬 x 高)及起始位置(startx, starty)
setup(width=810, height=610, startx=0, starty=0)
# 更改畫布(視窗)標題
title("我的畫布")

# 更改背景顏色
bgcolor("midnight blue")
# 將畫筆改成黃色，填滿顏色改成綠色
color('yellow', 'green')

# 筆被拿起，不會畫
up()
# 移動海龜到座標x=-400, y=-200的位置
goto(-400, -200)
# 筆被放下，開始畫
down()
# 準備畫草皮
begin_fill() # 開始填滿顏色到海龜畫過的圖形
forward(800)
right(90)
forward(100)
right(90)
forward(800)
right(90)
forward(100)
end_fill() # 結束填滿
# 筆被拿起，不會畫
up()

# 將畫筆改成黑色，填滿顏色改成黃色
color('black', 'yellow')
# 移動海龜到座標x=-350, y=-250的位置
goto(-350, 250)
# 筆被放下，開始畫
down()
# 準備畫月亮
begin_fill() # 開始填滿顏色到海龜畫過的圖形
# 畫一個半徑為30的圓形
circle(30)
end_fill() # 結束填滿
# 筆被拿起，不會畫
up()
# 隱藏海龜
hideturtle()

# 星星的各種顏色，使用串列設定顏色種類
star = ["white", "white smoke", "mint cream", "ivory", "yellow", "gold"]
# 星群，用來儲存星星位置
stargroup = []

while True:
    # 準備畫星星
    x = randint(-400, 400)
    y = randint(-100, 300)
    color = star[randint(0, len(star)-1)]
    goto(x, y)
    pensize(1)
    pencolor(color)
    dot()
    # 將目前星星的位置紀錄到星群
    stargroup.append([x, y])
    # 模擬星星一閃一閃的動作
    while len(stargroup) >= 20:
        first = stargroup[0]
        goto(first[0], first[1])
        pencolor("midnight blue")
        dot()
        del stargroup[0]
