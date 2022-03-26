'''
TUGAS 2 FISIKA KOMPUTASI
KELOMPOK 2
ANGGOTA KELOMPOK:
Febbrya Eka Dewi W  (21030224012)
Renita Fitriani     (21030224047)
Chaidar Aria Bayu P (21030224052)
Dilla Amalia        (21030224053)
'''
print("program yang bisa mendeteksi apakah itu bilang prima atau tidak")
print("-"*20)
x = int(input("Masukkan angka:"))
y = 2
if x >1 :
    while x % y!=0:
        y = y+1
    if y ==x:
        print(x, ":Prima")
    else:
        print(x, ":Bukan Prima")
else:
    print("Angka anda adalah %d \n Pastikan angka lebih dari 1" %x)