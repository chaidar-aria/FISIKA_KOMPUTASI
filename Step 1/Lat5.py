#Program untuk rentanf nilai A sampai E

nilai = int(input('Masukkan nilai:'))

if nilai >= 80:
    print('Predikat A')
    print('Lulus')
elif 79 >= nilai >= 70:
    print('Predikat B')
    print('Lulus')
elif 69 >= nilai >= 60:
    print('Predikat C')
    print('Lulus tapi disarankan mengulang')
elif 59 >= nilai >= 50:
    print('Predikat D')
    print('Tidak Lulus')
else: 
    print('Predikat E')
    print('Tidak Lulus')