import tkinter as tk
from tkinter import ttk

root= tk.Tk()

def seleccionar(opcion):
    print(opcion)

ttk.Button(root,text="Python",command=lambda:seleccionar("Python")).pack()
ttk.Button(root,text="Java",command=lambda:seleccionar("Java")).pack()
ttk.Button(root,text="Javascript",command=lambda:seleccionar("Javascript")).pack()

root.mainloop()