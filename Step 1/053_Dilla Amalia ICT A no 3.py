'''
Nama : Dilla Amalia
NIM : 21030224053
Kelas : FRE 2021

TUGAS FISIKA MATEMATIKA 1
Bagian A nomor 3
'''
#penjumlahan deret
from mpmath import*

print('jumlahan deret')
mp.dps = 15
mp.pretty = True
y=lambda n:(n**0.5)/(n+2)
sum=nsum(y,[1,inf])
print('sum=',sum)
