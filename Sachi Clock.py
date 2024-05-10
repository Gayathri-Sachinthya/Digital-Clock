from tkinter import*
from tkinter.ttk import*

from time import strftime

root=Tk()
root.title("Sachi Digital Clock")

def time():
    string=strftime('%H:%M:%S %p %a')
    label.config(text=string)
    label.after(1000,time)

label= Label(root, font=("DS-digital",40),
            background="WHITE",
            foreground="#2209C9")
label.pack(anchor='center')
time()
mainloop()
