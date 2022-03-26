'''
TUGAS 2 FISIKA KOMPUTASI
KELOMPOK 2
ANGGOTA KELOMPOK:
Febbrya Eka Dewi W  (21030224012)
Renita Fitriani     (21030224047)
Chaidar Aria Bayu P (21030224052)
Dilla Amalia        (21030224053)
'''
print("Buatlah program menampilkan angka genap dari yang terkecil sampai pada angka yang kita pilih!")
print("-"*20)
i = 1
x = int(input("Masukkan angka:"))
while i <= x :
    if i %2 ==0:
        print(i)
    i += 1