total = 0
bil = int (input("Masukan bilangan = "))
print("Total nilai =", end = ' ')

while bil >= 1:
    print(bil, end = ' ')
    if bil == 1:
        print('=', end = ' ')
    else:
        print('+', end = ' ')
    total += bil
    bil -= 1
print(total)