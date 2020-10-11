# Johan adalah seorang Mahasiswa Prodi Sistem Informasi Telkom University, 
# dia mendapat tugas untuk membuat sebuah program untuk menebak berapa tinggi dia menngunakan perulangan, 
# dimana program tersebut akan terus berjalan hingga jawaban yang diinputkan benar ! 

print("\t\t>>>> Aplikasi tebak tinggi badan <<<<")

while True:
    tebakan = int(input("Masukkan Tebakan anda: "))
    if tebakan == 160:
        print("Selamat Tebakan anda benar! ")
        break
    else: 
        print("Tebakan Salah!!!")