# for i in range(20, 0, -2):
#     print(i)

# for i in range(1, 10):
#     print(f"Perulangan ke-{i}")

# for i in range(20, 0, -2):
#     print(f"step ke-{i}")

# while i <= 7:
#     print("Hello World!")
#     i += 1

# a = 1
# b = 10
# while a < b:
#     print("Step ke-", a)
#     a += 1    

# a = 10
# b = 0
# while a > b:
#     print("Kuota internet anda sisa", a, "GB")
#     a -= 1

for i in range(1, 10):
    print("ini perulangan ke -", i)
    if i == 7:
        print("perulangan ke -", i, "dihentikan!")
        break

for i in range(0, 10):
    if i == 7:
        continue
    print(i)

a = 0
while True:
    print("step ke -", a, "!")
    a += 1
    if a == 7:
        print("step ke -", a, "dihentikan!")
        break

angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
i = -1
while i < len(angka):
    i += 1
    if i % 2 == 0 and i > 0:
        print("skip")
        continue
    print(angka[i])
