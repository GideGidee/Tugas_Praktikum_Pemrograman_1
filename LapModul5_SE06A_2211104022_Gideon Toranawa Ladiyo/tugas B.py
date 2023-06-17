def rata_rata(nilai):
    total = sum(nilai)
    rata = total/len(nilai)
    return rata

def hitung_predikat(rata):
    if 100 >= rata >= 90:
        predikat = "A"
    elif rata >= 70:
        predikat = "B"
    elif rata >= 50:
        predikat = "C"
    elif rata >= 30:
        predikat = "D"
    else:
        predikat = "E"
    return predikat

def cetak_hasil(predikat, nilai):
    print("Hasil predikat", predikat, "dengan nilai   :")
    for i, n in enumerate(nilai):
        print("Mata kuliah ke-{} : {}".format(i+1, n))

nilai_matkul = []

n = int(input("Masukkan jumlah mata kuliah : "))
print("")

for i in range(int(n)):
    inputnilai = int(input("Masukkan nilai mata kuliah ke-{} : ".format(i+1)))
    nilai_matkul.append(inputnilai)
print("")

rata = rata_rata(nilai_matkul)

if any(nilai > 100 or nilai < 0 for nilai in nilai_matkul):
    print("Nilai tidak valid!")
else:
    predikat = hitung_predikat(rata)
    cetak_hasil(predikat, nilai_matkul)