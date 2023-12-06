import math
def tambah(bil1, bil2): 
    hasil= bil1 + bil2 
    print('penjumlahan',bil1, "+",bil2,'=',hasil)
     
def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print('pengurangan', bil1, '-', bil2, '=', hasil)
    
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print('perkalian dari', bil1, '*', bil2, '=', hasil )
    
def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print('pembagian dari', bil1, '/', bil2, '=', hasil)

def pangkat(bilangan1,pangkat):
    print('pangkat',bilangan1,'**',pangkat,'adalah',math.pow(bilangan1, pangkat))
    
def akar(bil):
    print('akar dari', bil,'adalah', math.sqrt(bil))

def sin(bil):
    hasil = math.sin(math.radians(bil))
    print('hasil dari',bil,'adalah', hasil)
    
def cos(bil):
    hasil = math.cos(math.radians(bil))
    print('hasil dari',bil,'adalah', hasil)
    
def tan(bil):
    hasil = math.tan(math.radians(bil))
    print('hasil dari',bil,'adalah', hasil)
        
def log(bil):
    print('log dari', bil, 'adalah', math.log(bil))