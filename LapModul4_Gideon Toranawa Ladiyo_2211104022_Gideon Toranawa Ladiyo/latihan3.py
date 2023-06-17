def fpb(x, y):
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range (1,terkecil + 1):
        if ((x % i == 0)and(y % i == 0)):
            fpb = i
    return fpb

nilai1 = int(input("Masukkan bilangan pertama : "))
nilai2 = int(input("Masukkan bilangan kedua : "))
print("FPB =", fpb(nilai1, nilai2))  

# total = 0
# angka_pertama = 1

# for i in range(100):
#     total += angka_pertama
#     angka_pertama += 1

# print("Jumlah 10 angka pertama pada 100 deret angka:", total)
