class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk  : {self.nama}")
        print(f"Harga Asli   : Rp{self.harga:,}")

class Elektronik(Produk):
    def __init__(self, nama, harga, garansi):
        super().__init__(nama, harga)
        self.garansi = garansi

    def hitung_diskon(self):
        return self.harga * 0.9

    def tampilkan_hasil(self):
        self.tampilkan_info()
        print(f"Garansi      : {self.garansi} bulan")
        print(f"Harga Diskon : Rp{self.hitung_diskon():,.0f}")
        print("-" * 30)

class Pakaian(Produk):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran

    def hitung_diskon(self):
        return self.harga * 0.8

    def tampilkan_hasil(self):
        self.tampilkan_info()
        print(f"Ukuran       : {self.ukuran}")
        print(f"Harga Diskon : Rp{self.hitung_diskon():,.0f}")
        print("-" * 30)

prod1 = Elektronik("Iphone 100 Ultimate Pro Max", 5000000000, 12)
prod2 = Pakaian("Jaket Varsity", 500000, "XL")

prod1.tampilkan_hasil()
prod2.tampilkan_hasil()