#program menentukan predikat kelulusan
#{is=ipk bertipe float,input ipk bertipe float
#fs= predikat kelulusan diketahui}

#kamus
#input(ipk)
#ipk:float
#Algoritma
#   depends on ipk ()
def main ():
    ipk=float(input("Masukkan IPK Anda = "))
    if ipk>=3.5 :
        print("Dengan Pujian/Cum Laude")
    elif ipk>=3.0 and ipk<3.5 :
        print("Sangat Memuaskan/Very Good")
    elif ipk>2.75 and ipk<3.0 :
        print("Memuaskan/Good")
if __name__ == "__main__":
    main()
    