from tkinter import *


root = Tk()

root.title("Calculator")

root.iconbitmap(
    r"D:\calculator on python\Guillendesign-Variations-1-Calculator-3.ico")

# fun when we press any ky

text_lable = ""
text_num = ""
num1 = 0
num2 = 0
Switch = False
oper = ""


# show the number,operation and the reselt on screen
def on_screen():
    """just any any thing"""
    label.config(text=text_lable)


# when the user press any number
def on_click(num):
    """just any any thing"""
    global text_lable, text_num
    if not Switch:
        text_lable += str(num)
        on_screen()
    else:
        text_num += str(num)
        text_lable += str(num)
        on_screen()

# when the user choose the operations


def operation(op):
    """just any any thing"""
    global num1, text_lable, oper, Switch
    try:
        oper = op
        num1 = int(text_lable)
        text_lable += str(op)
        Switch = True
        on_screen()
    except ValueError:
        oper = op
        index_dot = text_lable.index(".")
        num_decimals = len(text_lable[index_dot + 1:])
        decimals = 1
        for i in range(num_decimals):
            decimals *= 10
        num1 = int(text_lable[:index_dot]) + \
            (int(text_lable[index_dot + 1:]) / decimals)
        text_lable += str(op)
        Switch = True
        on_screen()

# when we press the equ operation


def equ():
    """just any any thing"""

    global oper, num1, num2, text_lable, text_num, Switch

    try:
        num2 = int(text_num)

    except ValueError:
        index_dot = text_num.index(".")
        num_decimals = len(text_num[index_dot + 1:])
        decimals = 1
        for i in range(num_decimals):
            decimals *= 10
        num2 = int(text_num[:index_dot]) + \
            (int(text_num[index_dot + 1:]) / decimals)

    reselt = 0

    if oper == "x":
        reselt = num1*num2
    elif oper == "/":
        reselt = num1/num2
    elif oper == "+":
        reselt = num1+num2
    elif oper == "-":
        reselt = num1-num2

    text_lable += f" = {reselt}"
    on_screen()

    # claer the var after show the reselt
    text_lable = ""
    text_num = ""
    num1 = 0
    num2 = 0
    Switch = False
    oper = ""


# where the ruselt should apperd
label = Label(root, width=35, height=5, border=12,
              borderwidth=12, font=("", 8, "bold"))
label.grid(row=0, column=0, columnspan=4)


# the number from 0 to 2
bu0 = Button(root, text="0", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(0))
bu0.grid(row=1, column=0)

bu1 = Button(root, text="1", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(1))
bu1.grid(row=1, column=1)

bu2 = Button(root, text="2", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(2))
bu2.grid(row=1, column=2)


# the number from 3 to 5
bu3 = Button(root, text="3", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(3))
bu3.grid(row=2, column=0)

bu4 = Button(root, text="4", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(4))
bu4.grid(row=2, column=1)

bu5 = Button(root, text="5", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(5))
bu5.grid(row=2, column=2)


# the number from 6 to 8
bu6 = Button(root, text="6", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(6))
bu6.grid(row=3, column=0)

bu7 = Button(root, text="7", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(7))
bu7.grid(row=3, column=1)

bu8 = Button(root, text="8", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(8))
bu8.grid(row=3, column=2)


# the number 9
bu9 = Button(root, text="9", padx=20, pady=15, font=(
    "", 10, "bold"), command=lambda: on_click(9))
bu9.grid(row=4, column=1)

# the operations
bu_dot = Button(root, text=".", padx=20, pady=15, font=(
    "", 10, "bold"),
    command=lambda: on_click("."))
bu_dot.grid(row=4, column=0)


bu_mul = Button(root, text="x", padx=20, pady=15, font=(
    "", 10, "bold"),
    command=lambda: operation("x"))
bu_mul.grid(row=1, column=3)


bu_div = Button(root, text="÷", padx=20, pady=15, font=(
    "", 10, "bold"),
    command=lambda: operation("/"))
bu_div.grid(row=2, column=3)


bu_plus = Button(root, text="+", padx=20, pady=15, font=(
    "", 10, "bold"),
    command=lambda: operation("+"))
bu_plus.grid(row=3, column=3)


bu_minus = Button(root, text="_", padx=20, pady=15, font=(
    "", 10, "bold"),
    command=lambda: operation("-"))
bu_minus.grid(row=4, column=3)


bueq = Button(root, text="=", padx=20, pady=15, font=(
    "", 10, "bold"), command=equ)
bueq.grid(row=4, column=2)

root.mainloop()
