from tkinter import *

root = Tk()
root.title("Arithmetic Calculator")

# Entry widget to display input and output
input = Entry(root, width=50)
input.grid(row=0, column=0, columnspan=3, padx=15, pady=15)

# Global variables to store the first number and the math operation
fnum = None
math = None

# Button click function
def click(num):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(num))

# Function to perform addition
def add():
    global fnum, math
    fnum = float(input.get())
    math = "addition"
    input.delete(0, END)

# Function to perform subtraction
def sub():
    global fnum, math
    fnum = float(input.get())
    math = "subtraction"
    input.delete(0, END)

# Function to perform multiplication
def mul():
    global fnum, math
    fnum = float(input.get())
    math = "multiplication"
    input.delete(0, END)

# Function to perform division
def div():
    global fnum, math
    fnum = float(input.get())
    math = "division"
    input.delete(0, END)

# Function to clear the input
def clear():
    input.delete(0, END)

# Function to calculate the result
def equal():
    snum = float(input.get())
    input.delete(0, END)
    if fnum is not None:
        result = None
        if math == "addition":
            result = fnum + snum
        elif math == "subtraction":
            result = fnum - snum
        elif math == "multiplication":
            result = fnum * snum
        elif math == "division":
            if snum != 0:
                result = fnum / snum
            else:
                result = "Error: Division by zero"
        input.insert(0, result)

# Button creation and placement
button_1 = Button(root, text="1", padx=50, pady=25, command=lambda: click(1), bg="black", fg="white")
button_2 = Button(root, text="2", padx=50, pady=25, command=lambda: click(2), bg="black", fg="white")
button_3 = Button(root, text="3", padx=50, pady=25, command=lambda: click(3), bg="black", fg="white")
button_4 = Button(root, text="4", padx=50, pady=25, command=lambda: click(4), bg="black", fg="white")
button_5 = Button(root, text="5", padx=50, pady=25, command=lambda: click(5), bg="black", fg="white")
button_6 = Button(root, text="6", padx=50, pady=25, command=lambda: click(6), bg="black", fg="white")
button_7 = Button(root, text="7", padx=50, pady=25, command=lambda: click(7), bg="black", fg="white")
button_8 = Button(root, text="8", padx=50, pady=25, command=lambda: click(8), bg="black", fg="white")
button_9 = Button(root, text="9", padx=50, pady=25, command=lambda: click(9), bg="black", fg="white")
button_0 = Button(root, text="0", padx=50, pady=25, command=lambda: click(0), bg="black", fg="white")
button_add = Button(root, text="+", padx=50, pady=25, command=add, bg="blue", fg="white")
button_sub = Button(root, text="-", padx=50, pady=25, command=sub, bg="blue", fg="white")
button_mul = Button(root, text="x", padx=50, pady=25, command=mul, bg="blue", fg="white")
button_div = Button(root, text="/", padx=50, pady=25, command=div, bg="blue", fg="white")
button_clear = Button(root, text="AC", padx=100, pady=25, command=clear, bg="grey", fg="white")
button_equal = Button(root, text="=", padx=105, pady=25, command=equal, bg="green", fg="white")

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_mul.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_div.grid(row=6, column=0)
button_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
