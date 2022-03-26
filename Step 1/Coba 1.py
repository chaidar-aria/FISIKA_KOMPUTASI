import matplotlib.pyplot as plt

Hambatanjeniskawat = [1,2,3,4,5,6,7]
Hambatanpadarangkaian = [133,267,400,533,667,800,933]

#Membuat grafik pengaruh hambatan jenis kawat terhadap hambatan pada rangkaian
x = range(len(Hambatanjeniskawat))
plt.plot(Hambatanjeniskawat, Hambatanpadarangkaian)
plt.xticks(x, Hambatanjeniskawat)

#Sumbu x dan y
plt.xlabel('Hambatan jenis kawat')
plt.ylabel('Hambatan pada rangkaian')
plt.title('Pengaruh hambatan jenis kawat terhadap hambatan pada rangkaian')
plt.show ()

#Berdasarkan grafik tersebut dapat disimpulkan bahwa hambatan jenis kawat berbanding lurus terhadap hambatan pada rangkaian