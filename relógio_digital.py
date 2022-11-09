from tkinter import *
from tkinter.ttk import *

from time import strftime

rot = Tk()
rot.title('Relógio criado com python')

def time():
    str = strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000, time)

label = Label(rot, font=('ds-digital', 80), background='black', foreground='grey')
label.pack(anchor='center')
time()

mainloop()