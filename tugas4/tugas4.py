# %% [markdown]
# # TUGAS 4 FISIKA KOMPUTASI
# ## KELOMPOK 2
# NAMA ANGGOTA:
# 1. Febbrya Eka Dewi W  (21030224012)
# 2. Renita Fitriani     (21030224047)
# 3. Chaidar Aria Bayu P (21030224052)
# 4. Dilla Amalia        (21030224053)

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
maxIter = 500

lenX = lenY = 20
delta = 1

Ttop = 100
Tbottom = 0
Tleft = 0
Tright = 0

Tguess = 30

# %%
colorinterpolation = 50
colourMap = plt.cm.jet

X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))


# %%
T = np.empty((lenX, lenY))
T.fill(Tguess)

T[(lenY-1):, :] = Ttop
T[:1, :] = Tbottom
T[:, (lenX-1):] = Tright
T[:, :1] = Tleft


# %%
print("Mohon Tunggu. . . . .")
for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            T[i, j] = 0.25 * (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])

print("Iterasi Selesai")


# %%
# Konfigurasi
plt.title("Kontur Suhur")
plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)
plt.colorbar()
plt.show()

print("")


# %%
