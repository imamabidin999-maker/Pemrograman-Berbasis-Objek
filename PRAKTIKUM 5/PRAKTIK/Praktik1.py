#berjalan dan kecepatan kendaraan
class kendaraan:
    def __init__(self, kecepatan):        
        self.kecepatan = kecepatan
    
    def berjalan(self):
        print("kendaraan sedang berjalan")
    
    def laju(self):
        print(f"kecepatan kendaraan adalah {self.kecepatan} km/jam")

class mobil(kendaraan):
    def __init__(self):
        super().__init__(100)

    def berjalan(self):
        print("mobil berjalan di jalan raya")
        
    def laju(self):
        print(f"kecepatan mobil adalah {self.kecepatan} km/jam")

class motor(kendaraan):
    def __init__(self):
        super().__init__(80)

    def berjalan(self):
        print("motor melaju di jalan raya")

    def laju(self):
        print(f"kecepatan motor adalah {self.kecepatan} km/jam")
        
class pesawat(kendaraan):
    def __init__(self):
        super().__init__(500)

    def berjalan(self):
        print("pesawat terbang di udara")

    def laju(self):
        print(f"kecepatan pesawat adalah {self.kecepatan} km/jam")
        
class kapal(kendaraan):
    def __init__(self):
        super().__init__(50)

    def berjalan(self):
        print("kapal berlayar di laut")
        
    def laju(self):
        print(f"kecepatan kapal adalah {self.kecepatan} km/jam")
        
daftar_kendaraan = [
    mobil(), 
    motor(), 
    pesawat(),
    kapal()
    ]

for kendaraan in daftar_kendaraan:
    kendaraan.berjalan()
    kendaraan.laju()