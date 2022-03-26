#Tugas Fisika Komputasi No 1
#Program untuk membedakan bilangan genap dan ganjil


bilangan = int(input('Masukkan bilangan: '))
if bilangan % 2 == 0:
    print('%i merupakan bilangan genap' % bilangan)
else:
    print('%i merupakan bilangan ganjil' % bilangan)