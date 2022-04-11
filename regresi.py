# %% [markdown]
# # Regresi Linear
#
# Regresi Linier atau Linear Regression adalah suatu model statistik yang umum dan paling sederhana yang digunakan untuk Machine Learning untuk melakukan prediksi dengan cara supervised learning.
# Regresi Linier hanya bisa digunakan untuk data yang bersifat interval dan ratio yang biasanya bersifat diskrit dan kontinu, dan merupakan analisis bivariate dan multivariate, simplenya kita bahas bivariate terlebih dahulu, diharapkan juga sudah membaca tentang analisa bivariate terlebih dahulu dimana dijelaskan tentang korelasi antara 2 variabel yang sudah dibahas di Statistika Dasar (Lanjutan).
# Regresi Linier melibatkan 2 variabel dimana salah satunya adalah variabel independen (x) dan satu lagi adalah variabel dependen (y).
# Independen berarti variabel ini sebagai variabel utama yang mungkin akan mempengaruhi nilai variabel kedua (dependen).
# Dependen berarti nilai variabel ini akan tergantung dari nilai variabel independennya, jika korelasi tinggi maka dependensi juga tinggi.
# Mari kita mulai dengan contoh paling sederhana :
# Terdapat data sample yang didapat dari 10 orang sebagai berikut :
# ```sh
# Data Tinggi Badan(cm) : 151,174,138,186,128,136,179,163,152,131
# Data Berat Badan (Kg) : 63, 81, 56, 91, 47, 57, 76, 72, 62, 48
# ```
# Disini tinggi badan merupakan variabel independen (x), dan berat badan merupakan variabel dependen (y).
# Data x dan y ini dapat kita sebarkan ke dalam sumbu x dan y seperti berikut :
#
# ![Contoh Regresi Linear](https://miro.medium.com/max/1400/0*sqlVaod2URmmy2oG.png)
#
# Jika memang x dan y memiliki korelasi tinggi maka titik-titik akan cenderung menurun atau naik, dengan data diatas seharusnya naik. Regresi Linear adalah proses mencari garis linear yang menujukkan korelasi antara kedua variabel tersebut, garis linear itu akan didapat dengan sebuah persamaan :
# ```sh
# y = ax + b atau y = w1x + w0
# dimana
# a atau w1 adalah slope / gradient / coefficient
# b atau w0 adalah intercept / bias
# ```
#
# Sebelum menggunakan Regresi Linier, hitung terlebih dahulu korelasinya menggunakan rumus Pearson Correlation (r), jika belum paham ini, disarankan membaca tentang Statistika Dasar Lanjutan untuk analisis bivariate :
#
# Correlation Coefficient $$  r = \frac{\sum (x_i - \bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i - \bar{x})^2(y_i-\bar{y})^2}} $$
#
# ```sh
# mean x = (151+174+138+186+128+136+179+163+152+131)/10 = 153.8
# mean y = (63+81+56+91+47+57+76+72+62+48)/10 = 65.3
# r = (((151-153.8)*(63-65.3)) + ... + ((131-153.8)*(48-65.3))) /   √(((151-153.3)² + ... + (131-153.8)²)*((63-65.3)² + ... + (48-65,3)²))
#   = 0.9771295961897941
# Catatan : korelasi 0.97 adalah nilai yang sangat tinggi, artinya nilai y benar-benar sangat dipengaruhi oleh nilai x, karena korelasi tinggi maka algoritma Regresi Linier ini cocok digunakan untuk data tersebut.
# ```
#
# Setelah ditemukan korelasi tinggi selanjutnya adalah mencari persamaan garis dengan mencari terlebih dahulu nilai a dan b, dengan menggunakan rumus Least Square, rumus yang digunakan adalah sebagai berikut :
#
# $$Slope \;\;\;\;\; a = \frac{\sum(x_i - \bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2}$$
# $$intercept \;\;\;\; = b=\bar{y}-a\bar{x}$$
# Slope adalah tingkat kemiringan garis, intercept adalah jarak titik y pada garis dari titik 0
# ```sh
# mean x = (151+174+138+186+128+136+179+163+152+131)/10 = 153.8
# mean y = (63+81+56+91+47+57+76+72+62+48)/10 = 65.3
# a = (((151-153.8)*(63-65.3)) + ... + ((131-153.8)*(48-65.3))) / ((151-153.3) + ... + (131-153.8))²
#   = 0.67461045
# b = 65.3 - 0.67461045 * 153.8
#   = -38.45508707607701
# maka persamaan garis :
# y = 0.67461045 x - 38.45508707607701
# Catatan :
# Jadi persamaan garis diatas dapat digunakan untuk melakukan prediksi apabila kita memiliki data tinggi badan yang baru, berat badan dapat diperkirakan dengan rumus tersebut, masukkan nilai tinggi baru ke x, maka perkiraan nilai y (berat badan) akan didapat.
# ```
# ## Tentang algoritma Regresi Linier
# Digunakan untuk Prediksi dengan mencari pola garis terbaik antara variable independent dan dependen
# ### Pros:
# - Mudah diimplementasikan
# - Digunakan untuk memprediksi nilai numerik/ continous /data jenis interval dan ratio
# ### Cons :
# - Cenderung mudah Overfitting
# - Tidak dapat digunakan bila relasi antara variabel independen dan dependen tidak linier atau korelasi variabel rendah
#
#
# ## Pengukuran Akurasi
# Model tipe Regresi Linier tingkat akurasinya dapat dihitung dengan beberapa metode, yang paling umum adalah :
# - R-squared (r²) atau biasa disebut juga Coefficient of Determination, yaitu nilai dari r dikuaratkan, nilai r sudah dibahas diatas.
# - Adjusted R-squared (r²) biasanya digunakan apabila sample kecil dari populasi yang sangat besar.
#
# $$R_{adj}^2 = 1-\left [ \frac{(1-R^2)(n-1)}{n-k-1} \right ]$$
#
# - Multiple R-squared (r²) biasanya digunakan untuk multiple correlation multivariate.
#
# $$R=\sqrt{\frac{r_{yx1}^2+r_{yx2}^2+-2r_{yx1}\cdot r_{yx2}\cdot r_{x1x2}}{1-r^2_{x1x2}}}$$
#
# ## Pengukur Error
# Semakin tinggi nilai error, semakin besar errornya.
# - Redisual (y actual — y predicted)
# - Standard Error (SE)
# - Root Mean Square Error (RMSE)
# - Mean Absolute Error (MAE), absolute berarti nilai negatif dipositifkan
# - Root Relative Squared Error (RRSE)
# - Relative Absolute Error (RAE), absolute berarti nilai negatif dipositifkan
#
# $$SE_{\bar{x}} = \frac{s}{\sqrt{n}}$$
# $$RMSE = \sqrt{\sum \frac{(y_{pred}-y_{ref})^2}{N}}$$
# Mean Absolute Error (MAE)
# $$MAE = \frac{1}{n}\sum\left | y_{predicted} - y_{actual} \right |$$
# Root Relative Squared Error (RRSE)
# $$RRSE = \sqrt{\frac{\sum\left ( y_{predicted} - y_{actual} \right )^2}{\sum\left ( \bar{y}_{predicted} - \bar{y}_{actual} \right )^2}}$$
# Relative Absolute Error (RAE)
# $$RAE = \frac{\sum\left | y_{predicted} - y_{actual} \right |}{\sum\left | \bar{y}_{predicted} - \bar{y}_{actual} \right |}$$
#

# %% [markdown]
# ### Contoh Kasus
#
# A student hangs masses on a spring and measures the spring’s extension as a function of the applied force in order to find the spring constant k. Her measurements are :
#
# Mass (kg) 200 300 400 500 600 700 800 900
#
# Extension (cm) 5.1 5.5 5.9 6.8 7.4 7.5 8.6 9.4
#
# . For a perfect spring, the extension ΔL of the spring will be related to the applied force by the relation k. ΔL = F, where F = mg and Δ L = L – L0, and L is 34 the unstretched length of the spring. Use these data and the method of least squares to fing the spring constant k, and the unstretched length of the spring L0
#

# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# %%
df = pd.DataFrame([[200, 5.1], [300, 5.5], [400, 5.9], [500, 6.8], [600, 7.4], [
                  700, 7.5], [800, 8.6], [900, 9.4]])
df.columns = ['x', 'y']


# %%
x_train = df['x'].values[:, np.newaxis]
y_train = df['y'].values


# %%
lm = LinearRegression()
lm.fit(x_train, y_train)  # fase training
print('Coefficient: ' + str(lm.coef_))
print('Intercept: ' + str(lm.intercept_))


# %%
x_test = [[170], [171]]  # data yang akan diprediksi


# %%
p = lm.predict(x_test)  # fase prediksi
print(p)  # hasil prediksi

# %%
# prepare plot
pb = lm.predict(x_train)
dfc = pd.DataFrame({'x': df['x'], 'y': pb})
plt.scatter(df['x'], df['y'])
plt.plot(dfc['x'], dfc['y'], color='red', linewidth=1)
plt.xlabel('Mass (Kg)')
plt.ylabel('Extension (cm)')
plt.show()
