import json
import os
from datetime import datetime

class Barang:
    def __init__(self, id_barang, nama, harga):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"[{self.id_barang}] {self.nama:18} | Rp{self.harga:10,}"

    def to_dict(self):
        return {"tipe": "umum", "id": self.id_barang, "nama": self.nama, "harga": self.harga}

class BarangElektronik(Barang):
    def __init__(self, id_barang, nama, harga, garansi):
        super().__init__(id_barang, nama, harga)
        self.garansi = garansi

    def info(self):
        return f"{super().info()} | Garansi: {self.garansi} bln"

    def to_dict(self):
        d = super().to_dict()
        d.update({"tipe": "elektronik", "garansi": self.garansi})
        return d

class BarangKonsumsi(Barang):
    def __init__(self, id_barang, nama, harga, tgl_exp):
        super().__init__(id_barang, nama, harga)
        self.tgl_exp = tgl_exp

    def info(self):
        status = ""
        try:
            sekarang = datetime.now()
            kadaluarsa = datetime.strptime(self.tgl_exp, "%Y-%m-%d")
            
            if sekarang > kadaluarsa:
                status = " >>> [KADALUARSA!]"
            else:
                status = " (Aman)"
        except ValueError:
            status = " (Format tgl salah!)"

        return f"{super().info()} | Exp: {self.tgl_exp}{status}"

    def to_dict(self):
        d = super().to_dict()
        d.update({"tipe": "konsumsi", "tgl_exp": self.tgl_exp})
        return d

class GudangPolimorfik:
    def __init__(self, file_db='gudang_final.json'):
        self.file_db = file_db
        self.koleksi = []
        self.muat_data()

    def tambah_barang(self, objek_barang):
        self.koleksi.append(objek_barang)
        self.simpan_data()

    def simpan_data(self):
        with open(self.file_db, 'w') as f:
            data = [b.to_dict() for b in self.koleksi]
            json.dump(data, f, indent=4)

    def muat_data(self):
        if os.path.exists(self.file_db):
            with open(self.file_db, 'r') as f:
                data_list = json.load(f)
                self.koleksi = []
                for d in data_list:
                    if d['tipe'] == "elektronik":
                        obj = BarangElektronik(d['id'], d['nama'], d['harga'], d['garansi'])
                    elif d['tipe'] == "konsumsi":
                        obj = BarangKonsumsi(d['id'], d['nama'], d['harga'], d['tgl_exp'])
                    else:
                        obj = Barang(d['id'], d['nama'], d['harga'])
                    self.koleksi.append(obj)

    def laporan_stok(self):
        print("\n" + "="*90)
        print(f"{'ID':<6} | {'NAMA BARANG':<18} | {'HARGA':<13} | {'KETERANGAN TAMBAHAN'}")
        print("-" * 90)
        for b in self.koleksi:
            print(b.info())
        print("="*90)

def main():
    app = GudangPolimorfik()

    if not app.koleksi:
        print("💾 Membuat data awal...")
        app.tambah_barang(BarangElektronik("E01", "Monitor 4500K", 3500000, 24))
        app.tambah_barang(BarangKonsumsi("K02", "Susu MBG", 15000, "2023-01-01"))
        app.tambah_barang(BarangKonsumsi("K03", "Roti AOKA", 2500, "2026-12-31"))
        app.tambah_barang(Barang("U04", "Mousepad", 50000))

    app.laporan_stok()

if __name__ == "__main__":
    main()