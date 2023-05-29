def tinggiBadan(tinggi):
    tB=int(input("masukkan tinggi badan="))
    while not tB==0:
        tinggi.append(tB)
        tB=int(input("masukkan tinggi badan="))

def cetakTb(tinggi):
    for i in range (len(tinggi)):
        print(tinggi[i],end=" ")
def rata2Tb(tinggi):
    sums=0
    counter=0
    rata2=0
    for i in range(len(tinggi)):
        counter=counter+i
        sums=sums+tinggi[i]
    rata2=sums/counter
    return rata2

def panggil():
    listTb=[]
    tinggiBadan(listTb)
    print("\n")
    cetakTb(listTb)
    print("\n")
    print("rata2=",rata2Tb(listTb))
panggil()