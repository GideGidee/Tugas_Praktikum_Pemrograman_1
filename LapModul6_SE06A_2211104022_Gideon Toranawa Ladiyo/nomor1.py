def ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "genap"
    else:
        return "ganjil"

def tampilkan_hasil(hasil):
    print("Bilangan yang anda masukkan adalah {}".format(hasil))

bil = int(input("Masukkan bilangan : "))
hasil = ganjil_genap(bil)
tampilkan_hasil(hasil)