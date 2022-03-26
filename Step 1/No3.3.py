#Tugas Fisika Komputasi No 3
#Program untuk mendeteksi bilangan prima


bilangan = int(input('Masukkan bilangan: '))

pembagi = 2
if bilangan % pembagi != 0:
    pembagi = pembagi + 1
    if pembagi == bilangan:
        print('Bilangan', bilangan,'merupakan bilangan prima')
    else:
        print('Bilangan', bilangan, 'bukan merupakan bilangan prima')
else:
    print('Bilangan',bilangan, 'bukan merupakan bilangan prima')
