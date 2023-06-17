print("==========================")
print("Menghitung volume limas segi empat dan prisma segitiga")
print("==========================")
print("menghitung volume limas")
p_alas = float(input("panjang alas limas : "))
l_alas = float(input("lebar alas limas : "))
luas_alas = p_alas * l_alas
t_limas = float(input("tinggi limas : "))
v_limas = 1/3 * luas_alas * t_limas
print("==========================")
print("Luas volume limas segi empat adalah", v_limas)
print("==========================")
print("menghitung volume prisma segitiga")
t_a_prisma = float(input("tinggi alas prisma : "))
a_segitiga_alasprisma = float(input("alas segitiga : "))
l_segitiga = 1/2 * a_segitiga_alasprisma * t_a_prisma
t_prisma = float(input("tinggi prisma : "))
v_prisma = l_segitiga * t_prisma
print("==========================")
print("Volume prisma segitiga adalah", v_prisma)