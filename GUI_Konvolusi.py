from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import pandas as pd
import numpy as np    

root = Tk()
root.title("Grafik Trigonometri")
root.resizable(width=False,height=False)

WIDTH = 1000
HEIGHT = 600
canvas = Canvas(root, width=WIDTH,height=HEIGHT, bg='green')
canvas.pack()

data = pd.read_csv("data.csv")
df = data

log_start = 1517               # Depth of logging starts(m) from header
kb = 15                        # Kelly Bushing elevation(m) from header

gap_int = log_start - kb
repl_vel = 2632                # this is from VSP data knowledge (m/s)
log_start_time = 2.0 * gap_int / repl_vel        # 2 for twt

dt = 0.01
dt_iterval = np.nan_to_num(dt) * 0.1524 / 1e6
t_cum =  np.cumsum(dt_iterval) * 2
TWT = t_cum + log_start_time
df['TWT'] = pd.Series(TWT, index=TWT)

Imp = df['AI_Log'].values
Rc=[]
for i in range(len(Imp)-1):
    Rc.append((Imp[i+1]-Imp[i])/(Imp[i]+Imp[i+1]))

# to adjust vector size copy the last element to the tail
Rc.append(Rc[-1])

df['Rc'] = pd.Series(Rc, index=df.index)

dt = 0.001   #sampleing interval
t_max = 3.0   # max time to create time vector
t = np.arange(0, t_max, dt)
AI_tdom = np.interp(x=t, xp = df.TWT, fp = df.AI_Log)    #resampling
y = -(data['TWT'] )


def Rc(df): #impedansi akustik
    Imp = df['AI_Log'].values
    Rc=[]
    for i in range(len(Imp)-1):
        Rc.append((Imp[i+1]-Imp[i])/(Imp[i]+Imp[i+1]))
    # to adjust vector size copy the last element to the tail
    Rc.append(Rc[-1])
    # Let's add Rc into dataframe as new column
    df['Rc'] = pd.Series(Rc, index=df.index)
    return df,
    
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


def grafik():
    f = float(input("frekuensi:"))
    length = float(input("panjang data:"))
    dt = float(input("dt:"))
    t, w = getRicker(f,length, dt)
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    
    plot1 = fig.add_subplot(111)
    plot1.plot(t, w)
    canvas = FigureCanvasTkAgg(fig,
                               master = root)  
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas,
                                        root)
    toolbar.update()
        
    canvas.get_tk_widget().pack()

def resetgrafik():
    global ax

    ax.clear()
    ax.set_title('Grafik Trigonometri')
    ax.set_xlabel('x (phi)')
    ax.set_ylabel('y')
    ax.grid(True)

    canvas.draw()
  
