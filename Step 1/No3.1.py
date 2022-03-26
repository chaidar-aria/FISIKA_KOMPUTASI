bilangan = int(input("Masukkan bilangan: "))

if bilangan > 1:
    for i in range(2,bilangan):
        if (bilangan % i) == 0:
            print(bilangan, "bukan merupupakan bilangan prima")
    else:
        print(bilangan,"merupakan bilangan prima")
else:
    print(bilangan, "bukan merupakan bilangan prima")