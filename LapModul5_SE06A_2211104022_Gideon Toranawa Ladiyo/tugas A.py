kata = []
bilangan = int(input("masukkan jumlah kata : "))

for i in range(bilangan):
    inputkata = input("masukkan kata ke-{} : ".format(i+1))
    kata.append(inputkata)
   
m = input("masukkan kata yang dicari : ")
if m in kata:
    index = kata.index(m)
    print(m, "ditemukan pada index ke-"+ str(index))
else:
    print("kata {} tidak ditemukan dalam array".format(m))