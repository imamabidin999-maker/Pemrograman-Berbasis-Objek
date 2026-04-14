class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}")
        
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim

    def tampilkan_mahasiswa(self):
        self.tampilkan_info()
        print(f"NIM: {self.nim}")

class Dosen(Person):
    def __init__(self, nama, umur, nidn):
        super().__init__(nama, umur)
        self.nidn = nidn

    def tampilkan_dosen(self):
        self.tampilkan_info()
        print(f"NIDN: {self.nidn}")

mhs = Mahasiswa("Fadil", 20, "D12345")
mhs.tampilkan_mahasiswa()

dsn = Dosen("Dr. Budi", 40, "N67890")
dsn.tampilkan_dosen()

class Barang:
    def __init__(self, id_barang, nama, harga):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"[{self.id_barang}] {self.nama:15} | Rp{self.harga:10,}"

class BarangElektronik(Barang):
    def __init__(self, id_barang, nama, harga, garansi):
        super().__init__(id_barang, nama, harga)
        self.garansi = garansi

    def info(self):
        return f"{super().info()} | Garansi: {self.garansi} bln"
    
class BarangKonsumsi(Barang):
    def __init__(self, id_barang, nama, harga, tgl_exp):
        super().__init__(id_barang, nama, harga)
        self.tgl_exp = tgl_exp

    def info(self):
        return f"{super().info()} | Exp: {self.tgl_exp}"
    
laptop = BarangElektronik("E01", "Laptop Gaming", 15000000, 24)
susu = BarangKonsumsi("K05", "Susu UHT", 18000, "2026-12-01")

print(laptop.info())
print(susu.info())