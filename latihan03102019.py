#input
nama=input(" masukkan nama")
semester=int(input(" input semester "))
ipk=float(input("masukkan ipk "))

#output
cetak1=(" nama: {} Semester: {} ipk: {} ", format (nama, semester, ipk))
print(cetak1)

cetak2=(" nama : %  semester %d ipk %.2f "%(nama,semester, ipk))
print(cetak2)

print("nama:",nama, "semester: ",semester, "ipk nya",ipk)

#sep -> Karakter pemisahnya antar objek
# deafault spasi

nilai1="A"
nilai2="B"
nilai3="C"
print(nilai1, nilai2, nilai3)


universitas="DINUS"
print(" indeks ke [0] = ", univ [0])
print(" indeks ke [1] = ", univ [1])
print(" indeks ke [2] = ", univ [2])
print(" indeks ke [4] = ", univ [4])

#nama_variabel = [indeks awal:indeks_akhir-1]
print("cetak :",univ[0:5]) #hasil: DINUS
print("cetak :",univ[0:5;2]) #hasil: DNS
print("cetak :",univ[::-1]) #hasil: SUNID


"""
----------satu kasus-----------
if (kondisi) :
    ekspresi

-----------satu kasus komplementer------------
if (kondisi) :
    ekspresi
else (kondisi) :
    ekspresi


x=int(input(" input x : "))
y=int(input(" input y : "))