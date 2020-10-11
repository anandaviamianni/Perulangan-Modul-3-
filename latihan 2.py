print("\t\t Jurusan Sistem Informasi terdapat pada fakultas...")

while True:
    for i in range(5):
        tebakan= input("Masukkan tebakan mu: ")
        if tebakan == "FRI":
            print("Jawaban Benar")
            break
        else:
            print("Jawaban salah")
    if tebakan == "FRI":
        break
    else:
        print("\t\t=============================")
        print("KAMU SUDAH MENEBAK SEBANYAK 5 KALI. KAMU GAGAL!")
    break
