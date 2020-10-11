# Lisa sedang mengikuti kegiatan ukm dikampusnya, dia ingin mengabsen temanteman ukmnya yang hadir. 
# Jumlah anggota di ukmnya ada 30. Setelah dicek, anggota absen ke 4 dan 25 tidak hadir. 
# Lisa ingin memasukan data anggota yang hadir tersebut kedalam program. 
# Bantulah Lisa untuk memasukkan nomor absen anggota yang masuk menggunakan looping ! 

print("\t\t<<< Absen Anggota yang Hadir >>>")
for absen in range(1,31):
    if absen == 4 or absen == 25:
        continue
    print(absen,end= " ")
    print("\nselesai")