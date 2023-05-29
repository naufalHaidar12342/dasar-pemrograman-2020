n=int(input(" N= "))
sum=0
if n>=0 and n%2==0:
    for i in range(0,n+1,2):
        print(i,end=" ")
        sum=sum+i
    print("total=",sum)
if n<0:
    print("invalid")
