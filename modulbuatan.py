#Import Modul
import numpy as np

#Persamaan Wavelet Ricker


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

def getRicker(f,t):
    assert len(f) == 1, 'Ricker wavelet needs 1 frequency as input'
    f = f[0]
    pift = pi*f*t
    wav = (1 - 2*pift**2)*np.exp(-pift**2)
    return wav