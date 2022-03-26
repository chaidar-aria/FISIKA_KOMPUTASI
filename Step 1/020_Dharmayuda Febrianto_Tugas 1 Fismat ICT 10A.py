"""
TUGAS ICT FISMAT 1 BAGIAN A NO. 10
NAMA : Dharmayuda Febrianto
Kelas : FRE21
NIM : 21030224020
"""

from mpmath import *
#Pendekatan jumlahan deret tak hingga
print('jumlahan deret')
mp.dps = 15
mp.pretty = True
y=lambda n:n/(n**2+1)**2
sum=nsum(y,[1,inf])
print('Jumlah Deret=',sum)