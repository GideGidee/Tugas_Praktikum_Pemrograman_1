def fpb(a, b):
    if a > b:
        terkecil = b
    else:
        terkecil = a
    for i in range (1,terkecil + 1):
        if ((a % i == 0)and(b % i == 0)):
            fpb = i
    return fpb

def kpk (a, b):
    kpk = int (a * b / fpb(a, b))
    return kpk

angka1 = int (input("Masukan bilangan pertama = "))
angka2 = int (input("Masukan bilangan kedua = "))
print ("kpk =", kpk(angka1, angka2))