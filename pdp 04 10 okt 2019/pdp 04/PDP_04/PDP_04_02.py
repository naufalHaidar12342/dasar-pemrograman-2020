import os,sys
def main ():
    #Kamus
    score=int(input("Masukkan score : "))
    stars=0
    #Algoritma
    if score>=80 :
        stars=3
    elif ((score>45) and (score<80)):
        stars=2
    else:
        stars=1
    print("Selamat Anda mendapatkan bintang : " +str(stars))
if __name__ == "__main__":
    main()
    