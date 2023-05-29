#menentukan suhu air
#kamus
#air mendidih mulai dari 100 derajat celsius
#air menjadi es maksimal di suhu 0 derajat celsius
def main():
    import math

    suhu=float(input("Masukkan suhu air = "))
    suhu1=((5/9) + (suhu -32))
    if suhu1>=100 :
        print("Air mendidih")
    elif suhu1<100 and suhu>0 :
        print("Air belum mendidih")
    else:
        print("Air Es")
if __name__ == "__main__" :
    main()
