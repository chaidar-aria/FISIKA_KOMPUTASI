#Tugas Fisika Komputasi No 2
#Program untuk menentukan nilai genap pada range tertentu dari yang terkecil

x = int(input('bilangan'))
nilai_awal = int(input('Masukkan nilai awal: '))
nilai_akhir = int(input('Masukkan nilai akhir: '))

for x in range (nilai_awal, nilai_akhir):
    if x % 2 == 0:
        print(x)