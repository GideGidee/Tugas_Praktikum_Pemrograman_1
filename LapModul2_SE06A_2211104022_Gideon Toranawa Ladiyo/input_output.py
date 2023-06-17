# print("Hallo, hari ini kita belajar python")

# belajar = "Hallo, hari ini kita belajar"
# print(belajar)

# nama = "Gideon"
# print("Selamat pagi {}!".format(nama))

# fauzan = "ikan goreng"
# zaki = "ayam bakar"
# luthfi = "rendang sapi"

# print(f"makanan favorit fauzan adalah {fauzan}, makanan favorit zaki adalah {zaki}, dan makanan favorit luthfi adalah {luthfi}")

# print("makanan favorit fauzan adalah {}, makanan favorit zaki adalah {}, dan makanan favorit luthfi adalah {}" \
#       .format(fauzan, zaki, luthfi))

# print("makanan favorit fauzan adalah " + str(fauzan) + \
#       ", makanan favorit zaki adalah " + str(zaki) + \
#         ", dan makanan favorit luthfi adalah " + str(luthfi))

# panjang = 120
# lebar = 20
# luas = panjang * lebar
# print("luas =", luas)

# nama = input("Nama : ")
# nim = input("NIM : ")
# print("Nama : " + nama)
# print("NIM : " + nim)

# panjang = int(input("Masukkan panjang : "))
# lebar = int(input("Masukkan lebar : "))
# luas = panjang * lebar
# print("Luas =", luas)

data = ['6', '6', '8', '3', '2', '1']

maks = data[0]

for i in data:
    if i > maks:
        maks = i

print(maks)

