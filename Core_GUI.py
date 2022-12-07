#Import Modul
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.figure import Figure
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

def kont(f,length, dt):
    data = pd.read_csv("data.csv")
    df = data 
    df.head()
    
    y = -(data['TWT'] )
    def plot(x,y,nm):
        root = tk.Tk()
        root.geometry("500x500")
        root.title(str(nm))
        matplotlib.use('TkAgg')
        figure = Figure(figsize=(5, 5), dpi=100)
        axes = figure.add_subplot(111)
        axes.plot(x,y)
        canvas = FigureCanvasTkAgg(figure, root)
        canvas.get_tk_widget().grid(row=0, column=0)


    
    def Rc(df): #impedansi akustik
        Imp = df['AI_Log'].values
        Rc=[]
        for i in range(len(Imp)-1):
            Rc.append((Imp[i+1]-Imp[i])/(Imp[i]+Imp[i+1]))
    # to adjust vector size copy the last element to the tail
        Rc.append(Rc[-1])
    # Let's add Rc into dataframe as new column
        df['Rc'] = pd.Series(Rc, index=df.index)
        return df,Rc
    def getRicker(f,length,t): #ricker wavelet
        t = np.arange(-length/2, (length-dt)/2,dt)
        pift = np.pi*f*t
        wav = (1 - 2*pift**2)*np.exp(-pift**2)
        return wav,t
    def konvolusi(Rc,w): #Konvolusi 
        n_conv=len(Rc)-len(w)+1
        rev_w=w[::-1].copy()
        result=np.zeros(n_conv)
        for i_conv in range(n_conv):
            result[i_conv]=np.dot(Rc[i_conv:i_conv+len(w)],rev_w)
        return result

    Rc(df)
    tm, w = getRicker(f,length, dt)
    sinyalsintetik=konvolusi(df['Rc'],w)
    t = np.arange(0,len(sinyalsintetik),1)

    #Plotting Grafik
    plot(data["AI_Log"], y,"AI_Log")
    plot(tm,w,'Ricker wevlet')
    plot(sinyalsintetik,t, 'Hasil Konvolusi')
    