class hewan:
    def __init__(self,nama,makanan,hidup,berkembangBiak):
        self.nama = nama 
        self.makanan = makanan 
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
        
    def cetak(self):
        print("Hewan ini adalah ",self.nama)
        print("Makanan kesehariannya adalah",self.makanan)
        print("Hidup hewan ini di",self.hidup)
        print("Berkembang biar dengan cara",self.berkembangBiak)
        
class badak(hewan):
    def __init__(self, nama, makanan, hidup, berkembangBiak,bergerak,bernafas):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
        self.bernafas = bernafas
        
    def print(self):
        print("Hewan ini adalah",self.nama)
        print("Makanan kesehariannya adalah",self.makanan)
        print("Hidup hewan ini di",self.hidup)
        print("Berkembang biak dengan cara",self.berkembangBiak)
        print("Cara bergerak dengan", self.bergerak)
        print("Bernafas menggunakan",self.bernafas)
        
    
class ikan(hewan):
    def __init__(self, nama, makanan, hidup, berkembangBiak,bergerak,bernafas):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
        self.bernafas = bernafas
        
    def hasil(self):
        print("Hewan ini adalah",self.nama)
        print("Makanan kesehariannya adalah",self.makanan)
        print("Hidup hewan ini di",self.hidup)
        print("Berkembang biak dengan cara",self.berkembangBiak)
        print("Cara bergerak dengan", self.bergerak)
        print("Bernafas menggunakan",self.bernafas)
         
class ular(hewan):
    def __init__(self, nama, makanan, hidup, berkembangBiak,bergerak,bernafas):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bergerak = bergerak
        self.bernafas = bernafas
        
    def tampil(self):
        print("Hewan ini adalah",self.nama)
        print("Makanan kesehariannya adalah",self.makanan)
        print("Hidup hewan ini di",self.hidup)
        print("Berkembang biak dengan cara",self.berkembangBiak)
        print("Cara bergerak dengan", self.bergerak)
        print("Bernafas menggunakan",self.bernafas)
           
        
#objek hewan
x = hewan("Badak","tumbuhan","darat","melahirkan",)
x.cetak()

#objek badak
dak = badak ("Badak","tumbuhan","darat","melahirkan","jalan","Paru-paru")
dak.print()

#objek ikan
kan = ikan("Ikan","Pelet","Air","Bertelur","Berenang","insang")
kan.hasil()

#objek ular 
lar = ular ("Ular","Daging","Darat","Bertelur","Melata","Kulit")
lar.tampil()