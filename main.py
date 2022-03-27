'''
TUGAS FISIKA KOMPUTASI KE-2
KELAS FISIKA E 2021
KELOMPOK 4 :
ISHTAR DIDA         21030224006
PRATIWI             21030224038
ERFINA NUR RAHAYU   21030224051
'''
#MENGELOMPOKAN ANGKA GANJIL DAN GENAP

awal = int(input('masukan angka awal: '))
akhir = int(input('masukan angka akhir: '))
a = []
b = []
for i in range(awal, akhir+1) :
    if i%2 == 0:
        a.append(i)
    if i%2 == 1:
        b.append(i)
print("angka genap: ",a)
print("angka ganjil: ",b)
