#nilai_akhir

nilai_tugas=int(input("Masukkan nilai tugas = "))
nilai_uts=int(input("Masukkan nilai uts = "))
nilai_uas=int(input("Masukkan nilai uas = "))

nilai_tugas1=((30/100) * nilai_tugas)
nilai_uts1=((30/100) * nilai_uts)
nilai_uas1=((40/100) * nilai_uas)

nilai_akhir=(nilai_tugas1 + nilai_uts1 + nilai_uas1)
rata_rata= (nilai_akhir/3)

print("nilai akhir :",nilai_akhir)
print("rata rata %.2f" %(rata_rata))
