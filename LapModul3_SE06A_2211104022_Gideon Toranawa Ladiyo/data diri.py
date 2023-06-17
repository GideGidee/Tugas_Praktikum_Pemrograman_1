print("===========INPUT==========")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
# 1 = islam; 2= protestan; 3 = katolik; 4 = hindu; 5 = buddha
if(agama == 1):
    agama = "Islam"
elif(agama == 2):
    agama = "Protestan"
elif(agama == 3):
    agama = "Katolik"
elif(agama == 4):
    agama = "Hindu"
elif(agama == 5):
    agama = "Buddha"
else:
    agama = "Agama tidak ditemukan"

print("==========OUTPUT========")
print("Nama :", nama)
print("Jenis Kelamin :", jk)
print("Agama :", agama)