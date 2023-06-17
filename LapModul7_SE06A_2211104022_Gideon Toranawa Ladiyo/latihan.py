#Menu
def panggil(mhs):
    print("\n======== Menu Data Mahasiswa ========")
    print("1. Tambah Data Mahasiswa ")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa ")
    print("4. Lihat Data Mahasiswa ")
    print("5. Keluar ")

    while True:
        pilih = input("Pilih: ")
        if pilih == '1':
            addmhs(mhs)
            break
        elif pilih == '2':
            removemhs(mhs)
            break
        elif pilih == '3':
            ascmhs(mhs)
            break
        elif pilih == '4':
            viewmhs(mhs)
            break
        elif pilih == '5':
            print("Anda Keluar!")
            break
        else:
            print("Masukkan pilihan yang valid")

#Tambah
def addmhs(mhs):
    while True:
        jumlah = input("Jumlah Mahasiswa: ")
        if not jumlah.isdigit():
            print("Jumlah mahasiswa harus berupa angka")
            continue

        jumlah = int(jumlah)
        
        if jumlah <= 0:
            print("Jumlah mahasiswa harus lebih besar dari 0")
            continue

        while(jumlah > 0):
            nama = input("Nama Mahasiswa: ")
            mhs.append(nama)
            jumlah = jumlah - 1
        panggil(mhs)
        break

#Hapus
def removemhs(mhs):
    print("Data Mahasiswa %s" %mhs)
    remove_mhs = input("Hapus Mahasiswa: ")
    while True:
        if remove_mhs in mhs:
            mhs.remove(remove_mhs)
            print("Data Mahasiswa: %s"%mhs)
            panggil(mhs)
            break
        else:
            print("Nama tersebut tidak ada adalam data")
            removemhs(mhs)
            break

#urut
def ascmhs(mhs):
    mhs.sort()
    print(mhs)
    panggil(mhs)

#lihat
def viewmhs(mhs):
    if not mhs :
        print("Belum ada mahasiswa")
    else:
        for x in mhs:
            print("Nama Mahasiswa: %s" %x)
    panggil(mhs)

mhs = []
panggil(mhs)