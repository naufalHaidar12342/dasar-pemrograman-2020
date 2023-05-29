#miss indonesia
nama=str(input("Input nama : "))
umur=int(input("Input umur : "))
tinggi_badan=int(input("Tinggi : "))
print("----------------------------")
print("\t 1.Miss Indonesia")
print("\t 2.Putri Indonesia")
print("\t 3.Denok Semarang")
pilihan=int(input("Input pilihan : "))
print("-----------------------------")
if pilihan==1 :
    if umur>=20 and umur<=25 and tinggi_badan>=180 :
        print("Lolos Miss Indonesia")
    else:
        print("invalid")
elif pilihan==2:
    if umur>=18 and umur<=25 and tinggi_badan>=170 :
        print("Lolos Putri Indonesia")
    else:
        print("Invalid")
elif pilihan==3 :
    if umur>=17 and umur<=24 and tinggi_badan>=160:
        print("Lolos Denok Semarang")
    else:
        print("Invalid")