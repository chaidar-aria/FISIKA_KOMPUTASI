'''
TUGAS FISIKA KOMPUTASI KE-2
KELAS FISIKA E 2021
KELOMPOK 4 :
ISHTAR DIDA         21030224006
AISYAH SALSABILA    21030224026
PRATIWI             21030224038
ERFINA NUR RAHAYU   21030224051
'''
#MENGELOMPOKAN ANGKA GANJIL DAN GENAP

awal = int(input('masukan angka awal: '))
akhir = int(input('masukan angka akhir: '))
a = []

for i in range(awal, akhir+1) :
    if i%2 == 0:
        a.append(i)
print("angka genap: ",a)
print("Finish")


'''
TUGAS FISIKA KOMPUTASI KE-2
KELAS FISIKA E 2021
KELOMPOK 4 :
ISHTAR DIDA         21030224006
AISYAH SALSABILA    21030224026
PRATIWI             21030224038
ERFINA NUR RAHAYU   21030224051
'''

#MENYEBUTKAN ANGKA GANJIL DAN GENAP

a = float(input("masukkan angka: "))
if (a % 2) == 0:
    print ("Bilangan Genap")
else :
    print("Bilangan Ganjil")
print("Finish")


'''
TUGAS FISIKA KOMPUTASI KE-2
KELAS FISIKA E 2021
KELOMPOK 4 :
ISHTAR DIDA         21030224006
AISYAH SALSABILA    21030224026
PRATIWI             21030224038
ERFINA NUR RAHAYU   21030224051
'''
#Menentukan Bilangan Prima

num = int(input("Masukkan bilangan: "))
# bilangan prima harus lebih besar dari 1
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "bukan bilangan prima")
            print(i, "kali", num//i, "=", num)
            break
    else:
        print(num,"adalah bilangan prima")
# bila bilangan kurang atau sama dengan satu
else:
    print(num, "bukan bilangan prima")
print("finish")


'''
TUGAS FISIKA KOMPUTASI KE-2
KELAS FISIKA E 2021
KELOMPOK 4 :
ISHTAR DIDA         21030224006
AISYAH SALSABILA    21030224026
PRATIWI             21030224038
ERFINA NUR RAHAYU   21030224051
'''
#BILANGAN ANTARA 100 DAN 1000 HABIS DIBAGI 5 BUKAN KELIPATAN 3
print('Bilangan Antara 100 dan 1000 yang habis dibagi 5 tapi bukan kelipatan 3')

a = 100
while  a < 1000:
    a += 5

    if (a % 3) == 0:
        continue
    
    print(f"{a} adalah angka habis dibagi 5 bukan kelipatan 3")

print("Finish!")


'''
TUGAS FISIKA KOMPUTASI KE-2
KELAS FISIKA E 2021
KELOMPOK 4 :
ISHTAR DIDA         21030224006
AISYAH SALSABILA    21030224026
PRATIWI             21030224038
ERFINA NUR RAHAYU   21030224051
'''

#PROGRAM MENGHITUNG RENTANG NILAI SISWA
print('HASIL KELULUSAN NILAI AKHIR')
Nama = input ("Masukan Nama: " )
Kelas = input ("Masukan Kelas: ")
nilai= int(input("Masukan Nilai Ujianmu:"))

if (nilai >= 80) and (nilai <=100) :
    grade = "LULUS AKREDITAS A"
elif (nilai >= 70) and (nilai <=79) :
   grade = "LULUS AKREDITAS B"
elif (nilai >=60) and (nilai <=69) :
     grade = "LULUS AKREDITAS C -DISARANKAN MENGULANG-"
elif (nilai >=50) and (nilai <=59) :
     grade = "TIDAK LULUS AKREDITAS D"
else :
    grade = "TIDAK LULUS AKREDITAS E"
     
print('--------------------------------')
print('HASIL KELULUSAN')
print('Nama Siswa: ', Nama)
print('Kelas:', Kelas)
print('HASIL KELULUSAN NILAI AKHIR', "adalah =" ,grade)

