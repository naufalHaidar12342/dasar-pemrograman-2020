#wujud air

suhu=int(input("Masukkan suhu air = "))

if suhu<=0  :
    print("Air berwujud padat")
elif suhu>0 and suhu<100 :
    print("Air berwujud cair")
elif suhu>100:
    print("Air berwujud gas")