def avg(nilai_uas,nilai_tugas,nilai_uts):
    rata=(nilai_tugas+nilai_uas+nilai_uts)/3
    return rata
#nilai_tugas=float(input("nilai tugas="))
#nilai_uas=float(input("nilai uas="))
#nilai_uts=float(input("nilai uts="))
#average=print("rata2=",avg(nilai_uas,nilai_tugas,nilai_uts))
def prints(nilai_uas,nilai_tugas,nilai_uts):
    nilaiAkhir=rata(nilai_uas,nilai_tugas,nilai_uts)
    print('nilai tugas=',nilai_tugas)
    print('nilai uas=',nilai_uas)
    print('nilai uts=',nilai_uts)