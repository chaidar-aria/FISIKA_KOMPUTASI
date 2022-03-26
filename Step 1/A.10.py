print('Tugas ICT Fisika Matematika 1')
print('Kelas : Fisika 2021 E')
print('Bab   : Deret Tak Hingga')

print('Nama  : Riana Oktafianti')
print('NIM   : 21030224040')

print('Penyelesaian Tugas ICT FISMAT Bagian A No.10')

from mpmath import*
#Pendekatan jumlahan deret tak hingga
print('jumlahan deret')
mp.dps = 15
mp.pretty = True
y=lambda n:n/((n**2)+1)**2
sum=nsum(y,[1,inf])
print('sum=',sum)


 
