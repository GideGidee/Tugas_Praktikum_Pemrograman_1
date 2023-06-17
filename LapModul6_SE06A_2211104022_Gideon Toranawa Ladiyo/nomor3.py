def tambah(i, j):
    return i + j

def kurang(i, j):
    return i - j

def kali(i, j):
    return i * j

def bagi(i, j):
    if j != 0:
        return i / j
    else:
        print("Tidak dapat melakukan pembagian dengan bilangan 0!" 
              "\nSilahkan masukkan angka kedua selain 0")
        return None

def pangkat(i, j):
    return i ** j

def kalkulator():
    while True:
        print("\n=============KALKULATOR=============")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat")

        pilihan = input("\nMasukkan pilihan (1/2/3/4/5) : ")
        if pilihan == "1":
            print("\nAnda memilih operasi Penjumlahan")
            i = float(input("Masukkan angka pertama     : "))
            j = float(input("Masukkan angka kedua       : "))
            hasil = tambah(i, j)
            print("Hasil Penjumlahan          :", hasil)
        elif pilihan == "2":
            print("\nAnda memilih operasi Pengurangan")
            i = float(input("Masukkan angka pertama     : "))
            j = float(input("Masukkan angka kedua       : "))
            hasil = kurang(i, j)
            print("Hasil Pengurangan          :", hasil)
        elif pilihan == "3":
            print("\nAnda memilih operasi Perkalian")
            i = float(input("Masukkan angka pertama     : "))
            j = float(input("Masukkan angka kedua       : "))
            hasil = kali(i, j)
            print("Hasil Perkalian            :", hasil)
        elif pilihan == "4":
            print("\nAnda memilih operasi Pembagian")
            while True:   
                i = float(input("Masukkan angka pertama     : "))
                j = float(input("Masukkan angka kedua       : "))
                hasil = bagi(i, j)
                if hasil != None:
                    print("Hasil Pembagian            :", hasil)
                    break
                else:
                    continue
        elif pilihan == "5":
            print("\nAnda memilih operasi Pangkat")
            i = float(input("Masukkan angka pertama     : "))
            j = float(input("Masukkan angka kedua       : "))
            hasil = pangkat(i, j)
            print("Hasil Pangkat              :", hasil)
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")
            continue

        while True:
            lanjut = input("\nApakah Anda ingin melanjutkan? (y/n): ")
            if lanjut.lower() == "y" or lanjut.lower() == "n":
                break
            else:
                print("\nInput tidak valid. Silakan masukkan 'y' untuk melanjutkan atau 'n' untuk selesai.")

        if lanjut.lower() == "n":
            print("\nTerima kasih!")
            break

kalkulator()