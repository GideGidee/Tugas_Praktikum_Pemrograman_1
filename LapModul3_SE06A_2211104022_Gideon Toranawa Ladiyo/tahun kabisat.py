tahun = int(input("masukkan tahun saat ini : "))
hasil = tahun%4
if (hasil == 0):
    print("tahun kabisat")
else:
    print("bukan tahun kabisat")