#uang bulanan anak kos
#kamus
#bayar kos 500000
#uang makan 500000/bulan
#beli buku 200000

def main():
    uang_bulanan=int(input("Masukkan uang bulanan = "))

    if uang_bulanan<1200000 :
        print("Input tidak valid")
    elif uang_bulanan>500000 and uang_bulanan<=1500000 :
        print("Andi tidak dapat menyaksikan konser karena uang kurang")
    elif uang_bulanan>1500000 and uang_bulanan<=2000000:
        print("Andi dapat menyaksikan konser dengan tempat kursi biasa")
    elif uang_bulanan>2000000 and uang_bulanan<=5000000 :
        print("Andi dapat menyaksikan konser dengan tempat duduk VIP ")
if __name__ == "__main__" :
    main()
    
    
         
