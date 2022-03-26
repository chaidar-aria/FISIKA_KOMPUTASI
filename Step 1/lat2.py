#Program untuk mendeteksi bilangan prima


bilangan = int(input('Masukkan bilangan: '))

pembagi = 2
while bilangan % pembagi != 0:
    pembagi = pembagi + 1

if pembagi == bilangan:
    print('bilangan', bilangan,'adalah bilangan primer')
else:
    print('bilangan', bilangan, 'bukan bilangan primer')

