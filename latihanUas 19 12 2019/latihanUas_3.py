list1=[[2,19,29,77,1],
        [1,10,18,8,22],
        [65,34,63,12,1],
        [7,100,1,9,51],
        [2,1,3,4,55]]
maks=[0][0]
minim=[0][0]
for i in range(0,5):
    for j in range(0,5):
        if list1[i][j]>maks:
            maks=list1[i][j]
        if list1[i][j]<minim:
            minim=list1[i][j]
print(list1)
print("maks=",maks)