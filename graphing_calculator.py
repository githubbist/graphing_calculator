

#Graphing Calculator
import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import *

def function_input(y_x, interval, step):
	y = lambda x : eval(y_x)
	x = list(np.arange(interval[0], interval[1]+step, step))
	y_list = []
	for i in x:
		y_list.append(y(i))
	
	plt.plot(x, y_list)
	plt.title(str(y_x))
	plt.show()

def get_gui(entry):
	vals = []
	for i in entry:
		vals.append(i.get())
	function_input(vals[0], eval(vals[1]), float(vals[2]))

def gui():
	root = Tk()
	header = Label(root, text = "Graphing Calculator")
	header.grid(column = 0, row = 0, columnspan = 2)
	
	label_1 = Label(root, text = "Function")
	label_1.grid(column = 0, row = 1)
	
	entry_1 = Entry(root)
	entry_1.grid(column = 1, row = 1)
	
	label_2 = Label(root, text = "Domain")
	label_2.grid(column = 0, row = 2)
	entry_2 = Entry(root)
	entry_2.grid(column = 1, row = 2)
	
	label_3 = Label(root, text = "Step")
	label_3.grid(column = 0, row = 3)
	entry_3 = Entry(root)
	entry_3.grid(column = 1, row = 3)
	
	entry = [entry_1, entry_2, entry_3]
	
	run_button = Button(root, text = "Run", command = lambda : get_gui(entry))
	run_button.grid(column = 0, row = 4, columnspan = 2)

	root.mainloop()

gui()
