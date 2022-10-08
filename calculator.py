from tkinter import * 

root = Tk() 
root.title('calculator') 

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=20, pady=10)

operator = []

def button_click(number):
    current = e.get() 
    e.delete(0,END)
    e.insert(0, str(current) + str(number)) 

def button_add():
    global num
    num = float(e.get())
    e.delete(0,END)
    operator.append('+')

def button_substract():
    global num
    num = float(e.get())
    e.delete(0,END)
    operator.append('-')

def button_multiply():
    global num 
    num = float(e.get())
    e.delete(0,END)
    operator.append('*')

def button_divide():
    global num 
    num = float(e.get())
    e.delete(0,END)
    operator.append('/')

def button_clear():
    e.delete(0,END)

def button_back_space():
    e.delete(len(e.get())-1,END)

def button_equal():
    global num
    num2 = float(e.get())
    e.delete(0,END)
    if operator[-1:] == ['+']:
        answer = num + num2 
    elif operator[-1:] == ['-']:
        answer = num - num2 
    elif operator[-1:] == ['*']:
        answer = num * num2 
    elif operator[-1:] == ['/']:
        answer = num / num2
    e.insert(0,answer)

def button_add_signs():
    num = e.get()
    e.delete(0,END)
    e.insert(0,'-' + str(num))

def button_add_decimal_point():
    num = e.get()
    e.delete(0,END)
    e.insert(0,str(num) + '.')

button1 = Button(root, text='1', padx=20, pady=10, borderwidth=5, command=lambda: button_click(1))
button2 = Button(root, text='2', padx=20, pady=10, borderwidth=5, command=lambda: button_click(2))
button3 = Button(root, text='3', padx=20, pady=10, borderwidth=5, command=lambda: button_click(3))
button4 = Button(root, text='4', padx=20, pady=10, borderwidth=5, command=lambda: button_click(4))
button5 = Button(root, text='5', padx=20, pady=10, borderwidth=5, command=lambda: button_click(5))
button6 = Button(root, text='6', padx=20, pady=10, borderwidth=5, command=lambda: button_click(6))
button7 = Button(root, text='7', padx=20, pady=10, borderwidth=5, command=lambda: button_click(7))
button8 = Button(root, text='8', padx=20, pady=10, borderwidth=5, command=lambda: button_click(8))
button9 = Button(root, text='9', padx=20, pady=10, borderwidth=5, command=lambda: button_click(9))
button0 = Button(root, text='0', padx=52, pady=10, borderwidth=5, command=lambda: button_click(0))
buttonDot = Button(root, text='.', padx=20, pady=10, borderwidth=5, command=button_add_decimal_point)
buttonAdd = Button(root, text='+', padx=20, pady=10, borderwidth=5, command=button_add)
buttonbackspace = Button(root, text='<--', padx=20, pady=10, borderwidth=5, command=button_back_space)
buttonEqual = Button(root, text='=', padx=20, pady=10, borderwidth=5, command=button_equal)
buttonClear = Button(root, text='C', padx=20, pady=10, borderwidth=5, bg='#FF0000', command=button_clear)
buttonDivide = Button(root, text='/', padx=20, pady=10, borderwidth=5, command=button_divide)
buttonMultiply = Button(root, text='*', padx=20, pady=10, borderwidth=5, command=button_multiply)
buttonSubstract = Button(root, text='-', padx=20, pady=10, borderwidth=5, command=button_substract)
buttonInvertSigns = Button(root, text='+-', padx=20, pady=10, borderwidth=5, command=button_add_signs)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0, columnspan=2)
buttonDot.grid(row=4, column=2)
buttonAdd.grid(row=4, column=3)

buttonEqual.grid(row=4, column=4)
buttonDivide.grid(row=1, column=3)
buttonMultiply.grid(row=2, column=3)

buttonSubstract.grid(row=3, column=3)
buttonClear.grid(row=1, column=4)
buttonInvertSigns.grid(row=2, column=4)

buttonbackspace.grid(row=3,column=4)
root.mainloop()

