#program penyelesaian soal A metode persamaan

from math import *

#mendefinisikan nilai besaran gravitasi
g = 9.8

#meminta input dari pengguna
m1 = eval(input('masukkan nilai massa benda 1: ')) #10
m2 = eval(input('masukkan nilai massa benda 2: ')) #7
m3 = eval(input('masukkan nilai massa benda 3: ')) #5
(teta) = eval(input('masukkan nilai sudut bidang miring: ')) #45
(ns) = eval(input('masukkan nilai koefisien gesek statis: ')) #0.4

#mendefinisikan penyederhanaan rumus
phi = 3.1428
rad = teta*phi/180
y = sin(rad)
x = cos(rad)

#menentukan nilai massa 4
m4 = (m1+m2+m3)*(y-(x*(ns)))

#menentukan nilai tegangan 1, 2, 3, 4
T1 = m1*g*(y-(x*(ns)))
T2 = (m1+m2)*g*(y-(x*(ns)))
T3 = (m1+m2+m3)*g*(y-(x*(ns)))
T4 = T3

#menampilkan hasil perhitungan kepada pengguna
print('Nilai massa 4 adalah = ',m4)
print('Nilai Tegangan 1 adalah = ',T1)
print('Nilai Tegangan 2 adalah = ',T2)
print('Nilai Tegangan 3 adalah = ',T3)
print('Nilai Tegangan 4 adalah = ',T4)