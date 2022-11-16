#Persamaan Wavelet
import math as mt
import numpy as np

def wavelet(f,t):
    pift = mt.pi*f*t
    hasilwavelet = []
    wav = (1 - 2*pift**2)*mt.exp(-pift**2)
    hasilwavelet.append(wav)
    return wav

#Koefisien Seismik Refleksi

def impedansi(rho,v):
    rho, v = np.array(rho, dtype=float), np.array(v, dtype=float)
    return rho*v

def koefisien_refleksi(rho,v):
    rho, v = np.array(rho, dtype=float), np.array(v, dtype=float)
    Z   = rho*v       # acoustic impedance
    dZ  = (Z[1:] - Z[:-1])
    sZ  = (Z[:-1] + Z[1:])
    R   = dZ/sZ #reflection coefficients
    return R

