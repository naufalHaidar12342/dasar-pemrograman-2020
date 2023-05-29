# matriks A la Lab
#2x2
matriksA=[[1,0],
          [0,1]
        ]
print(matriksA)

#3x3
matriksB=[[1,0,1],
          [0,1,1],
          [0,1,1]
        ]
print(matriksB)

#matriksC
matriksC=[[1,0,1],
          [0,1,1],
          [0,1,1]
        ]
print(matriksC)

#print matrix with inputed rows and columns
rows=int(input("rows="))
columns=int(input("columns="))
#deklarasi elemen sebanyak rows
x=[0]*rows
for i in range(rows):
    x[i]=[2]*columns
print(x)

#hubungkan variabel x dgn list sebesar columns
#(jumlah kolom) thdp i(container)
#nilai dari setiap elemen bernilai 2

#list comprehension
manual_list=[1,2,3,4,5,6,7,7,9,10]
listComp=[x for x in range(1,11)]
print(listComp)

#multiply element by 2
listComp=[[x*2 for x in range(1,11)]

#print even number(bilangan genap)
bilGenap=[e for e in range(10) if %2==0]
print(bilGenap)

#matriks
matriks101=[[1,0,1],
            [2,1,2]]
for i in range (0,len(matriks101)):
    for j in range(0,len(matriks101[0])):
        print(matriks101[i],[j],end='')
    print("")