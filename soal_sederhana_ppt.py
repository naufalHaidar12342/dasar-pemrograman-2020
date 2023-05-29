#konversi nilai akhir

nilai_akhir=int(input("Masukkan nilai akhir = "))

if nilai_akhir>=85 and nilai_akhir<=100 :
    print("Grade A")
elif nilai_akhir>=70 and nilai_akhir<=85 :
    print("Grade B")
elif nilai_akhir>=60 and nilai_akhir<=70 :
    print("Grade C")
elif nilai_akhir>=40 and nilai_akhir<=60 :
    print("Grade D")
elif nilai_akhir>0 and nilai_akhir<=40 :
    print("Grade E")
else:
    print("Grade F")
