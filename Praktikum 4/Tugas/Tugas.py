import json

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def info_barang(self):
        return f"Produk: {self.nama}\nHarga: {self.harga}"

    def hitung_total(self, jumlah_beli):
        if jumlah_beli <= self.stok:
            total = self.harga * jumlah_beli
            return total
        else:
            return "Stok tidak mencukupi!"

class Elektronik(Produk):
    def __init__(self, nama, harga, stok, garansi):
        super().__init__(nama, harga, stok)
        self.garansi = garansi

    def info_barang(self):
        return f"{super().info_barang()}\nGaransi: {self.garansi} bulan"

class Pakaian(Produk):
    def __init__(self, nama, harga, stok, ukuran):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran

    def info_barang(self):
        return f"{super().info_barang()}\nUkuran: {self.ukuran}"
    
try:
    with open('Dataset.json', 'r') as file:
        produk_marketplace = json.load(file)
    
    print("=== SISTEM MARKETPLACE ===\n")

    for data in produk_marketplace:
        if data["kategori"] == "Elektronik":
            objek_produk = Elektronik(data["nama"], data["harga"], data["stok"], data["garansi"])
        else:
            objek_produk = Pakaian(data["nama"], data["harga"], data["stok"], data["ukuran"])

        jumlah = 2
        print(objek_produk.info_barang())
        print(f"Total harga ({jumlah} unit): Rp{objek_produk.hitung_total(jumlah):,}")
        print("-" * 40)

except FileNotFoundError:
    print("Error: File 'Dataset.json' tidak ditemukan!")