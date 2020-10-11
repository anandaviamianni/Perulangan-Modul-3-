batasan = int(input("Masukkan batas angka: "))
kelipatan = int(input("Masukkan kelipatan angka: "))
for i in range(1, batasan):
    print(i, end= " ")
print("")
for j in range(0,batasan,kelipatan):
    print(j, end= " ")