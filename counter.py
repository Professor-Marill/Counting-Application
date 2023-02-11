from tkinter import*
import os 
import keyboard

root = Tk()
root.title("Counting Application")
root.geometry("600x300")

label = Label(root, text = "Counting Application", font = "Comic 25 italic bold")
label.grid(column=0, row=0, columnspan = 8, rowspan = 2,pady = (10, 30))

instructions = Label(root, text="Please Choose Which Files You Would Like To Use")
instructions.grid(column=0, row=1, columnspan = 4, rowspan = 2, sticky=W, padx=(10, 0), pady=(30, 0))

increment = Label(root, text="Input Incremental Value")
increment.grid(column=5, row=1, columnspan=4, rowspan = 1, sticky = E, padx=(0, 30), pady=(30,0))

directory = os.getcwd()
dir_list = os.listdir(directory)

lis = ['1','2','3','4','5','6','7','8','9','10']

clicked = StringVar()
clicked.set(dir_list[0])

clicked2 = StringVar()
clicked2.set(dir_list[0])

clicked3 = StringVar()
clicked3.set(lis[0])

files = OptionMenu(root, clicked, *dir_list)
files.grid(column=0, row=3, sticky=E, padx=(40,0))

files2 = OptionMenu(root, clicked2, *dir_list)
files2.grid(column=1, row=3, sticky=W, padx=(10, 0))

increment_num = OptionMenu(root, clicked3, *lis)
increment_num.grid(column=5, row=3, padx=(37, 0))

f1 = clicked.get()
f2 = clicked2.get()
f3 = clicked3.get()

message = Label(root)
message2 = Label(root)
num = Label(root)
num2 = Label(root)

def tr():
	f1 = clicked.get()
	f2 = clicked2.get()
	c = open(str(f1), "r")
	number = c.readlines()
	count = (number[0])
	d = open(str(f2), "r")
	number2 = d.readlines()
	count2 = (number2[0])
	value = count.strip().isdigit()
	value2 = count2.strip().isdigit()
	if value == True and value2 == True:
		global num
		global num2
		num = Label(root, text = count, font = "Comic 25 bold")
		num2 = Label(root, text=count2, font = "comic 25 bold")
		num.grid(column=0,row=7, columnspan=4, padx=(0, 20), pady=(20,0))
		num2.grid(column=5,row=7, columnspan=4, padx=(15, 0), pady=(20,0))
	else:
		global message
		message = Label(root, text = "One or more of the following files may already have data. \n Please Use a file that has an integer in the first line of the file.")
		message.grid(column=0, row=4, columnspan=8, pady=(15,0), rowspan=(2), padx=(30,0))
	c.close()
	d.close()
	
	
def fal():
	global message2
	message2 = Label(root, text = "Please Select a Number For Your Incremental Value")
	message2.grid(column=0, row=4, columnspan=8, pady=(15,0), padx=(50,0))

def delete():
	message.grid_forget()
	message2.grid_forget()
	num.grid_forget()
	num2.grid_forget()
	

def run():
	delete()
	tr()
	
run = Button(root, text="Run", command = run)
run.grid(column=0, row=6, columnspan=8, pady=(20,0), padx=(70,0))

def addition1(e):
	f1 = clicked.get()
	c = open(str(f1), "r")
	number = c.readlines()
	count = int(number[0])
	add = int(clicked3.get())
	newcount = count + add
	f = open(str(f1), "w")
	f.write(str(newcount))
	f.close()
	c.close()
	delete()
	tr()
	
def addition2(e):
	f1 = clicked2.get()
	c = open(str(f1), "r")
	number = c.readlines()
	count = int(number[0])
	add = int(clicked3.get())
	newcount = count + add
	f = open(str(f1), "w")
	f.write(str(newcount))
	f.close()
	c.close()
	delete()
	tr()
	
def subtraction1(e):
	f1 = clicked.get()
	c = open(str(f1), "r")
	number = c.readlines()
	count = int(number[0])
	add = int(clicked3.get())
	newcount = count - add
	f = open(str(f1), "w")
	f.write(str(newcount))
	f.close()
	c.close()
	delete()
	tr()
	
def subtraction2(e):
	f1 = clicked2.get()
	c = open(str(f1), "r")
	number = c.readlines()
	count = int(number[0])
	add = int(clicked3.get())
	newcount = count - add
	f = open(str(f1), "w")
	f.write(str(newcount))
	f.close()
	c.close()
	delete()
	tr()
	
root.bind("<KP_1>", addition1)
root.bind("<KP_2>", addition2)
root.bind("<KP_3>", subtraction1)
root.bind("<KP_4>", subtraction2)

root.mainloop()
