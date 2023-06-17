def insertion_asc(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item

def insertion_desc(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while j >= 0 and array[j] < item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item

def add_buku(arr):
    total_buku = int(input("Masukkan Total Buku : "))
    for i in range(total_buku):
        nama_buku = input(f"Masukkan judul buku ke-{i+1} : ")
        arr.append(nama_buku)

def pilih_sort(arr):
    print("\n<========= Urutkan? =========>")
    print("1. Insertion Ascending")
    print("2. Insertion Descending")
    while True:
        pilihan = input("Pilih(1/2) : ")
        if pilihan == '1' or pilihan == '2':
            break
        else:
            print("Masukkan pilihan 1 atau 2")
    while True:
        if pilihan == '1':
            insertion_asc(arr)
            print("\nSorting buku secara Ascending")
            break
        elif pilihan == '2':
            insertion_desc(arr)
            print("\nSorting buku secara Descending")
            break
        else:
            print("Masukkan pilihan yang valid!")

def cetak_hasil(arr):
    print(" ")
    for i, n in enumerate(arr):
        print(f"Judul buku ke-{i+1} : {n}")

data_buku = []
add_buku(data_buku)
pilih_sort(data_buku)
cetak_hasil(data_buku)