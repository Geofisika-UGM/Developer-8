#Import Modul
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Data
data = pd.read_csv("data.csv")
df = data 
df.head()

#Plotting Grafik AI
y = -(data['TWT'] )

plt.figure(figsize=(16,8) )
plt.subplot(1,7,7)
plt.plot(data["AI_Log"], y, 'red')
plt.title("AI_Log")
plt.yticks([])

#Def 
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

f=20            #wavelet frequency
length=0.512    #Wavelet vector length
dt=0.001         # Sampling prefer to use smiliar to resampled AI
t, w = getRicker(f,length, dt)

#Plotting Grafik Sinyal Wavelet
t, w = getRicker(20,0.512, 0.001)
plt.plot(w,t)
plt.title('Wavelet')
plt.grid()

#Plotting Grafik Sinyal Konvolusi
sinyalsintetik=konvolusi(df['Rc'],w)
t = np.arange(0,len(sinyalsintetik),1)
plt.plot(sinyalsintetik,t)
plt.title('Hasil Konvolusi')
plt.grid()