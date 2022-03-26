'''
TUGAS 2 FISIKA KOMPUTASI
KELOMPOK 2
ANGGOTA KELOMPOK:
Febbrya Eka Dewi W  (21030224012)
Renita Fitriani     (21030224047)
Chaidar Aria Bayu P (21030224052)
Dilla Amalia        (21030224053)
'''
print("program untuk menampilkan semua bilangan antara 100 dan 1000 yang habis dibagi 5 tetapi bukan kelipatan 3")
print("-"*20)
for a in range (100, 1001, 5):
    if a % 3 != 0:
        print(a)