from tkinter import Tk, Button, Label, StringVar
from time import sleep


def update(expression: str):
    expression_var.set(expression_var.get() + expression)


def equals():
    try:
        expression_var.set(str(eval(expression_var.get())))

    except (SyntaxError, TypeError):
        expression_var.set("SyntaxError")
        expression_area.update()
        sleep(1)
        clear()

    except ZeroDivisionError:
        expression_var.set("Division by zero error")
        expression_area.update()
        sleep(1)
        clear()


def clear():
    expression_var.set("")


def delete():
    expression_var.set(expression_var.get()[:-1])


master = Tk()

master.geometry("310x310")
master.title("Calculator")
master.resizable(False, False)

expression_var = StringVar(master)
expression_area = Label(master, textvariable=expression_var, borderwidth=2, relief="solid", anchor="w", font=60)

add_button = Button(master, text="+", command=lambda: update("+"), font=(None, 20))
subtract_button = Button(master, text="-", command=lambda: update("-"), font=(None, 20))
multiply_button = Button(master, text="*", command=lambda: update("*"), font=(None, 20))
divide_button = Button(master, text="/", command=lambda: update("/"), font=(None, 20))

ans_button = Button(master, text="=", command=equals, font=(None, 20))
ac_button = Button(master, text="AC", command=clear, font=(None, 10))
del_button = Button(master, text="DEL", command=delete, font=(None, 10))

number_1 = Button(master, text='1', command=lambda: update('1'), font=(None, 20))
number_2 = Button(master, text='2', command=lambda: update('2'), font=(None, 20))
number_3 = Button(master, text='3', command=lambda: update('3'), font=(None, 20))
number_4 = Button(master, text='4', command=lambda: update('4'), font=(None, 20))
number_5 = Button(master, text='5', command=lambda: update('5'), font=(None, 20))
number_6 = Button(master, text='6', command=lambda: update('6'), font=(None, 20))
number_7 = Button(master, text='7', command=lambda: update('7'), font=(None, 20))
number_8 = Button(master, text='8', command=lambda: update('8'), font=(None, 20))
number_9 = Button(master, text='9', command=lambda: update('9'), font=(None, 20))
number_0 = Button(master, text='0', command=lambda: update('0'), font=(None, 20))
bracket_l = Button(master, text='(', command=lambda: update('('), font=(None, 20))
bracket_r = Button(master, text=')', command=lambda: update(')'), font=(None, 20))

expression_area.place(x=10, y=10, width=290, height=50)

# 1st row
number_9.place(x=10, y=70, width=50, height=50)
number_8.place(x=70, y=70, width=50, height=50)
number_7.place(x=130, y=70, width=50, height=50)
subtract_button.place(x=190, y=70, width=50, height=50)
add_button.place(x=250, y=70, width=50, height=50)

# 2nd row
number_6.place(x=10, y=130, width=50, height=50)
number_5.place(x=70, y=130, width=50, height=50)
number_4.place(x=130, y=130, width=50, height=50)
multiply_button.place(x=190, y=130, width=50, height=50)
divide_button.place(x=250, y=130, width=50, height=50)

# 3rd row
number_3.place(x=10, y=190, width=50, height=50)
number_2.place(x=70, y=190, width=50, height=50)
number_1.place(x=130, y=190, width=50, height=50)
ans_button.place(x=190, y=190, width=110, height=50)

# 4th row
bracket_l.place(x=10, y=250, width=50, height=50)
number_0.place(x=70, y=250, width=50, height=50)
bracket_r.place(x=130, y=250, width=50, height=50)
del_button.place(x=190, y=250, width=50, height=50)
ac_button.place(x=250, y=250, width=50, height=50)

master.mainloop()
