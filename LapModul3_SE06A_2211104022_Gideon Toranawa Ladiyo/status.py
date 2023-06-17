gender = input("Perempuan atau Laki-laki ? (L/P): ")

if(gender == 'L'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bapak!")
    elif(status == 'N'):
        print("Hallo Mas!")
    else:
        print("Tidak ada dalam pilihan")
if(gender == 'P'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Ibu!")
    elif(status == 'N'):
        print("Hallo Mba!")
    else:
        print("Tidak ada dalam pilihan")
else:
    print("Tidak ada dalam pilihan")