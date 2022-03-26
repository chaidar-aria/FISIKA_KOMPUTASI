'''
TUGAS 2 FISIKA KOMPUTASI
KELOMPOK 2
ANGGOTA KELOMPOK:
Febbrya Eka Dewi W  (21030224012)
Renita Fitriani     (21030224047)
Chaidar Aria Bayu P (21030224052)
Dilla Amalia        (21030224053)
'''

print("kode yang menyatakan dapat membedakan antar angka ganjil dan genap!")
print("-"*20)
bilangan = int(input("Masukkan angka:"))
if bilangan % 2 == 0:
    print("angka %d adalah angka genap" %bilangan)
else:
    print("angka %d adalah angka ganjil" %bilangan)
