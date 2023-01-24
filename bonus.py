from tkinter import *
from tkinter import ttk

parent = Tk()
parent.title("Padou")
parent.geometry("1000x1000")
parent.resizable(False, False)
parent.configure(background='#f5f5f5')
ttk.Button(parent, text="Quit", command=parent.destroy).grid(column=5, row=2)
parent.mainloop()  