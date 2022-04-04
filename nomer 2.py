awal = int(input("masukkan angka awal: "))
akhir = int(input("masukkan angka akhir: "))
x = []
for i in range(awal, akhir+1):
    if i%2 == 0:
        x.append(i)
print("angka genap: ", x)