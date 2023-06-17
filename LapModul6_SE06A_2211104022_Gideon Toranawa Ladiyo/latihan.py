# NOMOR 1
# def keliling_persegi(sisi):
#     hasil = 4*sisi
#     return hasil

# def luas_persegi(sisi):
#     hasil = sisi*sisi
#     return hasil

# sisi = int(input("Masukkan sisi : "))
# print("Keliling persegi :", keliling_luas_persegi(sisi))
# print("Luas persegi :", luas_persegi(sisi))

# NOMOR 1 bag 2
# def keliling_luas_persegi(sisi):
#     keliling = 4*sisi
#     luas = sisi*sisi
#     print("Keliling persegi :", keliling)
#     print("Luas persegi :", luas)

# sisi = int(input("Masukkan sisi : "))
# keliling_luas_persegi(sisi)

# NOMOR 2
def perbandingan(nilai1, nilai2):
    if nilai1 > nilai2:
        print(nilai1)
    elif nilai1 == nilai2:
        print("Tidak ada, kedua nilai bernilai sama")
    else:
        print(nilai2)

bil1 = int(input("Masukkan nilai pertama : "))
bil2 = int(input("Masukkan nilai kedua : "))
print("Bilangan yang lebih besar adalah :")
perbandingan(bil1, bil2)