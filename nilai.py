'''
nilai akhir :   
nilai tugas :   50%
niali uts   :   25%
nilai uas   :   25%
'''
tugas = float(input(" Masukkan nilai tugas : "))
uts = float(input(" Masukkan nilai uts : "))
uas = float(input(" Masukkan nilai uas : "))

nilai_tugas=(50/100)*tugas
nilai_uts=(25/100)*uts
nilai_uas=(25/100)*uas

nilai_akhir=nilai_uts + nilai_uas + nilai_tugas
print("nilai akhir : ",nilai_akhir)

rata=(tugas + uts + uas)
print(" rata-rata : ",rata)