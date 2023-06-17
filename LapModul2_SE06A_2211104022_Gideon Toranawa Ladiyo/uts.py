# total_harga = int(input("total : "))

# diskon = total_harga * 0.2

# if total_harga >= 150000:
#     total_harga = total_harga - diskon
#     print(total_harga)
# else :
#     print(total_harga)

# a = int(input("a : "))
# b = int(input("b : "))
# c = int(input("c : "))

# if a**2 + b**2 == c**2:
#     print("segitiga siku-siku")


a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if a >= b and a >= c:
    if b >= c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b >= a and b >= c:
    if a >= c:
        print(b,a,c)
    else:
        print(b,c,a)
elif c >= a and c >= b:
    if a >= b:
        print(c,a,b)
    else:
        print(c,b,a)