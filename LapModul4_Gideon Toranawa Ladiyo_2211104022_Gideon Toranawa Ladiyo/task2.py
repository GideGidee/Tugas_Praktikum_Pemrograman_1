bilangan = int(input("Masukkan bilangan : "))
pangkat = int(input("Masukkan pencacah : "))
hasil = 1

for i in range(pangkat):
    hasil *= bilangan

print("Hasil pangkat :", hasil)