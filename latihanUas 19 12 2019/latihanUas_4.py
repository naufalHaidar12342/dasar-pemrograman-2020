def bil_prima(cekPrima):
    cek=int(input("Masukkan bilangan: "))
    if cek>1:
        for i in range(2,cek):
            if (cek%i==0):
                print(cek,"bukan bilangan prima")
                print(i,"dikali",cek//i,"adalah",cek)
                break
        else:
            print(cek,"adalah bilangan prima")
    else:
        print(cek,"bukan bilangan prima")
bil_prima(())


#cekPrima=int(input("Masukkan bilangan="))
#if cekPrima%cekPrima==0 and cekPrima%1==cekPrima:
#    print("{} adalah bilangan prima".format(cekPrima))
#if cekPrima%cekPrima!=0 and cekPrima%2==0 or cekPrima%3==0:
#    for i in cekPrima:
#        bil1=cekPrima/2
#        print("{} bukan bilangan prima".format(cekPrima))
        