
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Calculator made by Arsh Ergon")
window.geometry("400x100")
img = tk.PhotoImage(file="C:\\Users\\HP\\Desktop\\pythonProjects\\pythonIcon.png")
window.tk.call('wm', 'iconphoto', window._w, img)

#------Functions------

def ADD():

	num1 = int(Num1_Entry.get())
	num2 = int(Num2_Entry.get())
	Sum = num1 + num2
	take_display = tk.Text(master=window, height=1, width=13)
	take_display.grid(column=2, row=2)
	take_display.insert(tk.END, str(Sum)+' Addition')

def SUB():

	num1 = int(Num1_Entry.get())
	num2 = int(Num2_Entry.get())
	Sum = num1 - num2
	take_display = tk.Text(master=window, height=1, width=13)
	take_display.grid(column=2, row=2)
	take_display.insert(tk.END, str(Sum)+' Subtraction')

def MULTI():

	num1 = int(Num1_Entry.get())
	num2 = int(Num2_Entry.get())
	Sum = num1 * num2
	take_display = tk.Text(master=window, height=1, width=13)
	take_display.grid(column=2, row=2)
	take_display.insert(tk.END, str(Sum)+' Multiply')

def DIV():

	num1 = int(Num1_Entry.get())
	num2 = int(Num2_Entry.get())
	Sum = num1 / num2
	take_display = tk.Text(master=window, height=1, width=13)
	take_display.grid(column=2, row=2)
	take_display.insert(tk.END, str(Sum) +' Divide')

def MODE():

	num1 = int(Num1_Entry.get())
	num2 = int(Num2_Entry.get())
	Sum = num1 % num2
	take_display = tk.Text(master=window, height=1, width=13)
	take_display.grid(column=2, row=2)
	take_display.insert(tk.END, str(Sum)+' MODE')

def about():
	messagebox.showinfo("Version 1.0.0", "This app is made by Arsh Ali\nCation this app is still in development\nif you think you can make this app much better then me then who is stopping YOU!!?\n*See the icon CODE!*")

#-------Labels--------


Num1_Entry = tk.Label(text='Enter Number')
Num1_Entry.grid(row=0, column=0)
Num1_Entry = tk.Entry()
Num1_Entry.grid(column=1, row=0)

Num2_Entry = tk.Label(text='Enter Number')
Num2_Entry.grid(column=0, row=1)
Num2_Entry = tk.Entry()
Num2_Entry.grid(column=1, row=1)


#-----Buttons----

Add_Button = tk.Button(text='Add', command=ADD)
Add_Button.grid(column=2, row=0)

Sub_Button = tk.Button(text='Subtraction', command=SUB)
Sub_Button.grid(column=2, row=1)

Multi_Button = tk.Button(text='Multiply', command=MULTI)
Multi_Button.grid(column=3, row=0)

Div_Button = tk.Button(text='Divide', command=DIV)
Div_Button.grid(column=3, row=1)

Mode_Button = tk.Button(text='Mode', command=MODE)
Mode_Button.grid(column=0, row=3)

About_Button = tk.Button(text='Press About', command=about)
About_Button.grid(column=1, row=3)

Exit_Button = tk.Button(text='Exit', command=window.destroy)
Exit_Button.grid(column=4, row=1)

window.mainloop()
