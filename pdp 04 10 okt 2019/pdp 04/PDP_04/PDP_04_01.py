import os,sys
def main () :
    #kamus
    nilai=int(input("Masukkan nilai : "))

    #algoritma
    if nilai>0 :
        if (nilai>=100) :
            print ("A")
        elif ((nilai<100) and (nilai>50)):                              
            print("B")
        else:
            print("C")
    else:
        if (nilai>-100):
            print("D")
        else:
            print("E")
if __name__ == "__main__" :
    main ()


    
    
    