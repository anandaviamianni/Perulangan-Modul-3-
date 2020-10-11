a = int(input("Masukkan tinggi segitiga: "))
for i in range(0,a):
    for j in range(0,i+1):
            print("*",end = "")
    print("")

#or
angka = int(input("Masukkan tinggi segitiga: "))
for kolom in range(1, angka +1):
        print("*" * kolom)
print()