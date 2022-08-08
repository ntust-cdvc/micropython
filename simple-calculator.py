from tkinter import *

expression = ""

# 計算函式
def evaluate():
    try:
        global expression
        result = ""
        if expression != equation.get():
            result = str(eval(equation.get()))
        else:
            result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("error!")
        expression = ""

def press(num):
    global expression

    expression += str(num)
    equation.set(expression)

def clear():
    global expression

    expression = ""
    equation.set(expression)

# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
    gui.title('Python計算機')
    gui.geometry('260x250')

    equation = StringVar()
    field = Entry(gui, textvariable=equation, font=('Arial',20), relief='solid',
            justify='right', width=16)
    field.place(x=5, y=10)

    btn_7 = Button(gui, text='7', font=('Arial',20), width=2, command=lambda: press(7))
    btn_7.place(x=5, y=50)
    btn_8 = Button(gui, text='8', font=('Arial',20), width=2, command=lambda: press(8))
    btn_8.place(x=65, y=50)
    btn_9 = Button(gui, text='9', font=('Arial',20), width=2, command=lambda: press(9))
    btn_9.place(x=125, y=50)
    btn_plus = Button(gui, text='+', font=('Arial',20), width=2, command=lambda: press('+'))
    btn_plus.place(x=185, y=50)

    btn_4 = Button(gui, text='4', font=('Arial',20), width=2, command=lambda: press(4))
    btn_4.place(x=5, y=100)
    btn_5 = Button(gui, text='5', font=('Arial',20), width=2, command=lambda: press(5))
    btn_5.place(x=65, y=100)
    btn_6 = Button(gui, text='6', font=('Arial',20), width=2, command=lambda: press(6))
    btn_6.place(x=125, y=100)
    btn_minus = Button(gui, text='-', font=('Arial',20), width=2, command=lambda: press('-'))
    btn_minus.place(x=185, y=100)

    btn_3 = Button(gui, text='3', font=('Arial',20), width=2, command=lambda: press(3))
    btn_3.place(x=5, y=150)
    btn_2 = Button(gui, text='2', font=('Arial',20), width=2, command=lambda: press(2))
    btn_2.place(x=65, y=150)
    btn_1 = Button(gui, text='1', font=('Arial',20), width=2, command=lambda: press(1))
    btn_1.place(x=125, y=150)
    btn_multiply = Button(gui, text='x', font=('Arial',20), width=2, command=lambda: press('*'))
    btn_multiply.place(x=185, y=150)

    btn_clear = Button(gui, text='AC', font=('Arial',20), width=2, command=clear)
    btn_clear.place(x=5, y=200)
    btn_0 = Button(gui, text='0', font=('Arial',20), width=2, command=lambda: press(0))
    btn_0.place(x=65, y=200)
    btn_equal = Button(gui, text='=', font=('Arial',20), width=2, command=evaluate)
    btn_equal.place(x=125, y=200)
    btn_div = Button(gui, text='/', font=('Arial',20), width=2, command=lambda: press('/'))
    btn_div.place(x=185, y=200)

    gui.mainloop()
