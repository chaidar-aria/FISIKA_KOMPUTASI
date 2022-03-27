'''
Nama : Erfina Nur Rahayu
Kelas : FRE 21
NIM : 21030224051
TUGAS ICT FISMAT 1 BAGIAN A NO.1
'''

# jumlah deret tak hingga
from mpmath import*

print('jumlahan deret')
mp.dps = 15
mp.pretty = True
y=lambda n:n/(n+4)
sum=nsum(y,[1,inf])
print('sum=',sum)

