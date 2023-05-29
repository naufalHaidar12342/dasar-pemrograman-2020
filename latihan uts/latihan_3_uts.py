#lunpia
nama=input("Input nama : ")
jumlah_lunpia=int(input("Jumlah lunpia : "))
print("====================================")
if jumlah_lunpia>=1 and jumlah_lunpia<=10 :
    harga1=20000
    total_biaya=(jumlah_lunpia*harga1)
    print("Nama : ",nama)
    print("Jumlah lunpia : ",jumlah_lunpia)
    print("Total biaya : ",total_biaya)
elif jumlah_lunpia>=11 and jumlah_lunpia<=25 :
    harga2=19500
    total_biaya2=(jumlah_lunpia*harga2)
    print("Nama : ",nama)
    print("jumlah lunpia : ",jumlah_lunpia)
    print("Gratis 1 gantungan kunci")
    print("Total biayanya : ", total_biaya2)
elif jumlah_lunpia>=26 and jumlah_lunpia<=50 :
    harga3=18000
    total_biaya3=(jumlah_lunpia*harga3)
    print("Nama : ",nama)
    print("jumlah lunpia : ",jumlah_lunpia)
    print("Gratis 2 lunpia")
    print("Total biayanya : ", total_biaya3)
elif jumlah_lunpia>50:
    harga4=18000
    total_biaya4=(jumlah_lunpia*harga4)
    print("Nama : ",nama)
    print("jumlah lunpia : ",jumlah_lunpia)
    print("Gratis 5 lunpia")
    print("Total biayanya : ", total_biaya4)

