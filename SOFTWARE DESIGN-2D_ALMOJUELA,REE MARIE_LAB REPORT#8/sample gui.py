from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root, padding=80)
frm.grid()

ttk.Label(frm, text="Mabait ba si SIr Jay-Ar?").grid(column=100, row=10)

ttk.Button(frm, text="Oo", command=root.destroy).grid(column=100, row=20)

root.mainloop()