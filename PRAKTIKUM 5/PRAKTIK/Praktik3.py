from datetime import datetime
import json
import os

class Barang:
    def __init__(self, id_barang, nama, harga):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"[{self.id_barang}] {self.nama:18} | Rp{self.harga:10,}"

    def to_dict(self):
        # Menambahkan identitas tipe "umum" [cite: 143]
        return {"tipe": "umum", "id": self.id_barang, "nama": self.nama, "harga": self.harga}

class BarangElektronik(Barang):
    def __init__(self, id_barang, nama, harga, garansi):
        super().__init__(id_barang, nama, harga)
        self.garansi = garansi

    def info(self):
        return f"{super().info()} | Garansi: {self.garansi} bln"

    def to_dict(self):
        # Mengambil dict dari parent dan update tipenya [cite: 144]
        d = super().to_dict()
        d.update({"tipe": "elektronik", "garansi": self.garansi})
        return d

class BarangKonsumsi(Barang):
    def __init__(self, id_barang, nama, harga, tgl_exp):
        super().__init__(id_barang, nama, harga)
        self.tgl_exp = tgl_exp

    # Tugas Praktikum: Validasi Tanggal Kadaluarsa [cite: 155, 158]
    def info(self):
        status = ""
        try:
            # Menggunakan datetime untuk cek waktu sistem [cite: 157]
            tgl_sekarang = datetime.now()
            tgl_kadaluarsa = datetime.strptime(self.tgl_exp, "%Y-%m-%d")
            
            if tgl_sekarang > tgl_kadaluarsa:
                status = " (KADALUARSA!)"
        except:
            status = " (Format tgl salah)"
            
        return f"{super().info()} | Exp: {self.tgl_exp}{status}"

    def to_dict(self):
        d = super().to_dict()
        d.update({"tipe": "konsumsi", "tgl_exp": self.tgl_exp})
        return d
    
class GudangPolimorfik:
    def __init__(self, file_db='gudang_v3.json'):
        self.file_db = file_db
        self.koleksi = []
        self.muat_data()

    def tambah_barang(self, objek_barang):
        self.koleksi.append(objek_barang)
        self.simpan_data()

    def simpan_data(self):
        with open(self.file_db, 'w') as f:
            # Mengubah objek menjadi list of dictionary [cite: 145]
            data = [b.to_dict() for b in self.koleksi]
            json.dump(data, f, indent=4)

    def muat_data(self):
        if os.path.exists(self.file_db):
            with open(self.file_db, 'r') as f:
                data_list = json.load(f)
                self.koleksi = []
                for d in data_list:
                    # Polimorfisme: Memilih class berdasarkan tipe [cite: 146]
                    if d['tipe'] == "elektronik":
                        obj = BarangElektronik(d['id'], d['nama'], d['harga'], d['garansi'])
                    elif d['tipe'] == "konsumsi":
                        obj = BarangKonsumsi(d['id'], d['nama'], d['harga'], d['tgl_exp'])
                    else:
                        obj = Barang(d['id'], d['nama'], d['harga'])
                    self.koleksi.append(obj)

    def laporan_stok(self):
        print("\n" + "="*85)
        print(f"{'ID':<6} | {'NAMA BARANG':<18} | {'HARGA':<13} | {'KETERANGAN TAMBAHAN'}")
        print("-" * 85)
        # Inilah Polimorfisme: Python otomatis tahu info() mana yang dipanggil [cite: 151, 152]
        for b in self.koleksi:
            print(b.info())
        print("="*85)    
        
def main():
    app = GudangPolimorfik()

    if not app.koleksi:
        print("💾 Database kosong, membuat data awal...")
        app.tambah_barang(BarangElektronik("E01", "Laptop Pro", 12000000, 12))
        app.tambah_barang(BarangKonsumsi("K02", "Roti Coklat", 15000, "2024-05-10"))
        app.tambah_barang(Barang("U03", "Kabel Data", 25000))

    app.laporan_stok()

if __name__ == "__main__":
    main()