import math
def luasSegitiga(tinggi, alas):
    hasil = (tinggi * alas) * 0.5
    print('luas segitiga dengan tinggi', tinggi,
            'dan alas', alas,
            'adalah', hasil)
def kelilingSegitiga (sisi):
    hasil = sisi + sisi +sisi
    print('keliling segitiga', sisi, '+', sisi, '+', sisi, '=', hasil)
def luasPersegi(sisi):
    hasil = sisi * sisi
    print('luas persegi dengan sisi', sisi,
          'adalah', hasil)  
def kelilingPersegi (sisi):
    hasil = sisi + sisi +sisi+sisi
    print('keliling segitiga', sisi, '+', sisi, '+', sisi, sisi, '=', hasil)
def luasPersegiPanjang(panjang, lebar):
    hasil = panjang * lebar
    print('luas persegi dengan panjang', panjang,
            'dan lebar', lebar,
            'adalah', hasil)
def kelilingPersegiPanjang (panjang,lebar):
    hasil = 2 * (panjang+lebar)
    print('keliling persegi panjang dengan panjang', panjang, 'dan lebar', lebar, 'adalah', hasil)
def luasBelahKetupat(diagonal1, diagonal2):
    hasil = 0.5 * (diagonal1 * diagonal2)
    print('luas belah ketupat dengan diagonal 1 =', diagonal1,
    'dan diagonal 2 =', diagonal2, 'adalah', hasil)
def KelilingBelahKetupat (sisi):
    hasil = sisi+sisi+sisi+sisi
    print("keliling belah ketupat dengan", sisi, 'adalah', hasil)
def luasJajarGenjang(alas,tinggi):
    hasil = alas * tinggi
    print('luas jajar genjang dengan alas',alas ,'dan tinggi', tinggi,'adalah',hasil)
def kelilingJajarGenjang(a, b):
    hasil = 2 *(a+b)
    print('hasil keliling jajar genjang dengan a', a, 'dan b', b, 'adalah', hasil)