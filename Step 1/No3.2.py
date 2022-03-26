bilangan = int(input('Masukkan bilangan: '))

if bilangan > 1:
    for i in range (2,bilangan):
        print(bilangan, 'bukan merupakan bilangan prima')
    else:
        print(bilangan, 'merupakan bilangan prima')
else:
    print(bilangan, 'merupakan bilangan prima')
