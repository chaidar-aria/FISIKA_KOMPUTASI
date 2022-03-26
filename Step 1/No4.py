#Tugas Fisika Komputasi No 4
#Program untuk menampilkan semua bilangan diantara 100 dan 1000 yang habis dibagi 5 tetapi bukan kelipatan 3

for x in range (100,1000):
        if x % 5 == 0 and x % 3 != 0:
            print(x)
