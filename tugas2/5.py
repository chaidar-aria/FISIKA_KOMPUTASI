'''
TUGAS 2 FISIKA KOMPUTASI
KELOMPOK 2
ANGGOTA KELOMPOK:
Febbrya Eka Dewi W  (21030224012)
Renita Fitriani     (21030224047)
Chaidar Aria Bayu P (21030224052)
Dilla Amalia        (21030224053)
'''
print("program untuk rentang nilai dari A sampai E")
print("-"*20)
nama = input("Nama:")
nilai = float(input("Nilai:"))

if nilai >= 80:
    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Dinyatakan LULUS, dengan predikat A")
elif nilai < 80 and nilai >=70:
    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Dinyatakan LULUS, dengan predikat B")
elif nilai < 70 and nilai >=60:
    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Dinyatakan LULUS (Disarankan untuk mengulang), dengan predikat C")
elif nilai < 60 and nilai >=50:
    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Dinyatakan TIDAK LULUS, dengan predikat D")
elif nilai < 50:
    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Dinyatakan TIDAK LULUS, dengan predikat E")
else:
    print("Data tidak valid")