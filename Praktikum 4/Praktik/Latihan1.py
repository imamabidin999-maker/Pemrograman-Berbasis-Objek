class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_dasar(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"

class Kucing(Hewan):
    def __init__(self, nama, umur, ras, warna):
        super().__init__(nama, umur)
        self.ras = ras
        self.warna = warna

    def tampilkan_hasil(self):
        print(f"[Kucing] {self.tampilkan_dasar()} | Ras: {self.ras}, Warna: {self.warna}")

class Paus(Hewan):
    def __init__(self, nama, umur, habitat, panjang):
        super().__init__(nama, umur)
        self.habitat = habitat
        self.panjang = panjang

    def tampilkan_hasil(self):
        print(f"[Paus]   {self.tampilkan_dasar()} | Habitat: {self.habitat}, Panjang: {self.panjang}m")

class Singa(Hewan):
    def __init__(self, nama, umur, wilayah, jumlah_kawanan):
        super().__init__(nama, umur)
        self.wilayah = wilayah
        self.jumlah_kawanan = jumlah_kawanan

    def tampilkan_hasil(self):
        print(f"[Singa]  {self.tampilkan_dasar()} | Wilayah: {self.wilayah}, Kawanan: {self.jumlah_kawanan} ekor")

hewan1 = Kucing("Neko", 3, "Anggora", "Putih")
hewan2 = Paus("Pause", 25, "Samudra Pasifik", 30)
hewan3 = Singa("Simba", 7, "Sabana Afrika", 15)

hewan1.tampilkan_hasil()
hewan2.tampilkan_hasil()
hewan3.tampilkan_hasil()