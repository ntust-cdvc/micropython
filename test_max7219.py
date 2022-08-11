# 匯入microbit 函式庫
from microbit import *
# 匯入matrix7219 函式庫
import matrix7219

# 初始化設定，不用更改
max7219led = matrix7219.Matrix8x8(spi, pin16)
# 設定LED矩陣明亮度
max7219led.brightness(15)

while True:
    # microbit內建顯示模組
    display.show(Image.HAPPY)
    sleep(1000)
    display.clear()
    
    # 設定矩陣內容全為False，代表不亮
    max7219led.fill(False)
    # 設定特定座標(2,2)內容為True，代表點亮
    max7219led.pixel(2, 2, True)
    # 顯示矩陣內容到畫面
    max7219led.show()
    sleep(1000)

    max7219led.fill(False)
    max7219led.show()
    # 設定矩陣內容全為True，代表點亮
    max7219led.fill(True)
    # 顯示矩陣內容到畫面
    max7219led.show()
    sleep(1000)
