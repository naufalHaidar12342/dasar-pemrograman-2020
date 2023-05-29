n=int(input("N="))
sum=0
average=0
if n>=0:
    for i in range (0,n+1):
        sum=sum+i
        average=sum/i
    print(i)
    print(" Total= ",sum)
    print("rata-rata=",average)
else:
    print("invalid")
    
    
    