#neested if
nama=input("nama pembeli = ")
alamat=input("alamat pembeli = ")
telpon=int(input("no telpon = "))



print("=====================UNIT MOBIL DEALER JAYA ABADI==============================")
print(" pilih jenis mobil : ")
print("\t 1. Daihatsu")
print("\t 2. Honda")
print("\t 3. Toyota")
print("")
pilihan=int(input("masukkan merk mobil yang dibeli : "))
print("")

if (pilihan==1) :
    print(">>>>>macam macam mobil Daihatsu<<<<<")
    print("\t a. Grand New Xenia")
    print("\t b. All New Terios")
    print("\t c. New Ayla")
    pilih1=input("masukkan jenis mobil yang dibeli :")

    if (pilih1=="a") :
        print("Harga mobil Grand New Xenia adalah 183 juta")
    if (pilih1=="b"):
        print(" Harga mobil All New Terios adalah 215 juta")
    if (pilih1== "c"):
        print("Harga mobil New Ayla adalah 110 juta")

elif (pilihan==2 ):
    print(">>>>>macam macam mobil Honda<<<<<")
    print("\t a. Honda Brio Satrya")
    print("\t b. Honda Jazz")
    print("\t c. Honda Brio")
    pilih2=input("masukkan jenis mobil yang dibeli :")

    if (pilih2== "a") :
        print("Harga mobil Honda Brio Satya adalah 131 juta")
    if (pilih2== "b") :
        print( "Harga mobil Honda Jazz adalah 232 juta")
    if (pilih2== "c") :
        print("Harga Honda Brio adalah 189 juta")
elif (pilihan==3) :
    print(">>>>>macam macam mobil Toyota<<<<<")
    print("\t a. Alphard")
    print("\t b. Camry")
    print("\t c. Fortuner")
    pilih3=input("masukkan jenis mobil yang dibeli :")

    if (pilih3== "a") :
        print("Harga mobil Alphard adalah 870 juta")
    if (pilih3== "b") :
        print("Harga mobil Camry adalah 560 juta")
    if (pilih3== "c") :
        print("hARGA MOBIL Fortuner adalah 492 juta")
else:
    print("tak terdefinisi")
