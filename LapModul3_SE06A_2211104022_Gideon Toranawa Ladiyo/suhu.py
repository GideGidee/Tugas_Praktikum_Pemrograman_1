suhu = int(input("Masukkan besarnya suhu: "))

if(suhu <= 0):
    print("pada suhu", suhu, "derajat celcius, air akan berwujud es")
elif(suhu > 0 & suhu < 100):
    print("pada suhu", suhu, "derajat celcius, air akan berwujud air")
else:
    print("pada suhu", suhu, "derajat celcius, air akan berwujud gas")


    