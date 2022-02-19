# Program
# Menghitung jarak antara 2 titik koordinat

# Kamus
# a, b, c, d, e, f  : int
# koordinatAkhir    : int

# Algoritma
print('Petunjuk: Masukkan angka koordinat 3D dengan separasi koma dan spasi \n format: <int>, <int>, <int> \n contoh: 9, 3, 2')
x1, y1, z1 = [int(x) for x in input("Masukkan koordinat awal: ").split(", ")] # input koordinat awal
x2, y2, z2 = [int(x) for x in input("Masukkan koordinat akhir: ").split(", ")] # input koordinat akhir

jarak = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5     # menghitung jarak dengan rumus matematika
                                                        # ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

print("%.2f" % jarak) # mengeluarkan output jarak dengan maksimal 2 digit desimal
