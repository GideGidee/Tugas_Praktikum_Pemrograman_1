# nilai = int(input("masukkan bilangan bulat : "))
# if (nilai > 0):
#     print("bilangan", nilai, "merupakan bilangan positif")
# elif (nilai < 0) :
#     print("bilangan", nilai, "merupakan bilangan negatif")
# else:
#     print("bilangan nol")

# ===============================
# t = int(input("suhu air saat ini : "))
# if t <= 0 : 
#     print("air akan berwujud padat")
# elif t > 0 and t < 100:
#     print("air akan berwujud cair")
# elif t >= 100 :
#     print("air akan berwujud Gas atau uap")

# =============================
# hh = int(input("masukkan jam saat ini : "))
# mm = int(input("masukkan menit saat ini : "))
# ss = int(input("masukkan detik saat ini"))

# total_detik = hh*3600 + mm * 60 + ss
# print(total_detik)

# =============================
# huruf = str(input("masukkan huruf : "))
# if (huruf == "a" or huruf == "A"):
#     print("huruf vokal")
# elif (huruf == "i" or huruf == "I"):
#     print("huruf vokal")
# elif (huruf == "u" or huruf == "U"):
#     print("huruf vokal")
# elif (huruf == "e" or huruf == "E"):
#     print("huruf vokal")
# elif (huruf == "o" or huruf == "O"):
#     print("huruf vokal")
# else:
#     print("huruf konsonan")

# ==================================
# nilai = int(input("masukkan nilai : "))
# pembagi = int(input("masukkan nilai pembagi : "))

# hasil = nilai/pembagi

# if (hasil == int(hasil)):
#     print("hasil valid")
# else : 
#     print("hasil tidak valid")

tahun = int(input("masukkan tahun saat ini : "))
hasil = tahun%4
if (hasil == 0):
    print("tahun kabisat")
else:
    print("bukan tahun kabisat")