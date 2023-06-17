def keliling_lingkaran(pi, r):
    hasil = 2 * pi * r
    return hasil

def luas_lingkaran(pi, r):
    hasil = pi * r * r
    return hasil

def tampilkan_hasil(keliling, luas):
    print("Keliling Lingkaran : {}".format(keliling))
    print("Luas Lingkaran : {}".format(luas))

pi = 3.14
r = float(input("Masukkan jari-jari : "))

keliling = keliling_lingkaran(pi, r)
luas = luas_lingkaran(pi, r)
tampilkan_hasil(keliling, luas)
