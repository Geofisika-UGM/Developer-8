#Import Modul
import numpy as np
import functools
import itertools
import operator
import sys
import warnings
import numbers
import numpy.core.multiarray

#Persamaan Wavelet Ricker
def wavelet(f,t):
    '''Frekuensi (f) adalah banyak gelombang dalam satu detik, satuannya Hertz (Hz)
    waktu (t) satuannya sekon (s) '''
    pift = np.pi*f*t
    hasilwavelet = []
    wav = (1 - 2*pift**2)*np.exp(-pift**2)
    hasilwavelet.append(wav)
    return wav

#Impedansi akustik
def impedansi(rho,v):
    '''Rho atau massa jenis(ρ) adalah pengukuran massa setiap satuan volume benda
     kecepatan (v) adalah jarak perpindahan suatu objek dalam waktu tertentu'''
    rho, v = np.array(rho, dtype=float), np.array(v, dtype=float)
    return rho*v

#Koefisien Seismik Refleksi
def koefisien_refleksi(rho,v):
    rho, v = np.array(rho, dtype=float), np.array(v, dtype=float)
    Z   = rho*v #Impedansi akustik
    dZ  = (Z[1:] - Z[:-1])
    sZ  = (Z[:-1] + Z[1:])
    R   = dZ/sZ #Koefisien refleksi
    return R

#KONVOLUSI
def konvolusi(a, v, mode='full'):
    a, v = np.array(a, copy=False, ndmin=1), np.array(v, copy=False, ndmin=1)
    if (len(v) > len(a)):
        a, v = v, a
    if len(a) == 0:
        raise ValueError('a cannot be empty')
    if len(v) == 0:
        raise ValueError('v cannot be empty')
    return multiarray.correlate(a, v[::-1], mode)
