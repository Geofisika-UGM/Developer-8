#Import Modul
from tkinter import *
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from Core_GUI import kont
import pandas as pd
import numpy as np

#Buat Window
root = Tk()
root.geometry("420x200")
root.title('Seismometer Sintetik')

labelfr = LabelFrame(root,text="result",padx=20,pady=20)
labelfr.place(x=60,y=380)

f = Label(root,text = "Masukan Frekuensi")
l = Label(root,text = "Panjang data")
dt=  Label(root,text = "interval sampling")
e1 = Entry(root,width=20)
e2 = Entry(root,width=20)
e3 = Entry(root,width=20)
f.place(x = 20, y = 50)
e1.place(x = 20, y = 70)
l.place(x = 150, y = 50)
e2.place(x = 150, y = 70)
dt.place(x = 280, y = 50)
e3.place(x = 280, y = 70)

def plot():
    x1=float(e1.get())
    x2=float(e2.get())
    x3=float(e3.get())
    kont(x1,x2,x3)

#Buat Tombol
plot_button = Button(master = root, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
plot_button.place(x = 180, y = 100)

root.mainloop()