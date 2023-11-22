#tugas 1
def biodata(Nama,Alamat,Gender,Umur,Hobby):
    print("Nama saya adalah",Nama)
    print("Alamat saya di",Alamat)
    print("Jenis kelamin adalah",Gender)
    print("Umur saya adalah",Umur)
    print("Hobbi saya adalah",Hobby)
    
biodata("Amanda Aprilia Permata Putri","Bojonggede","Perempuan","18 Tahun","Menghafal")

#tugas 2
def cetak_nilai(nilai):
    if(nilai <=60):
        print("gagal")
    elif(nilai >=61 and nilai <=70):
        print("baik")
    elif(nilai >=71 and nilai <=80):
        print("sangat baik")
    elif(nilai >= 81 and nilai <=100):
        print("istemewa")
    else:
        print("nilai tidak ada")

cetak_nilai(95)
cetak_nilai(61)
cetak_nilai(77)

#tugas 3
def bilangan_ganjil(ganjil):

    for i in range(ganjil):
        if (i %2 !=0):
            print(i,end=' ')
bilangan_ganjil(50)