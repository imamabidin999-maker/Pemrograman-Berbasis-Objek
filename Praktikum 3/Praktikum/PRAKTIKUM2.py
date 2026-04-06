import json
import os

class Barang:
    def __init__(self, id_barang, nama, harga):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"| {self.id_barang:8} | {self.nama:20} | Rp{self.harga:10,} |"

    def to_dict(self):
        return {"id": self.id_barang, "nama": self.nama, "harga": self.harga}

class Gudang:
    def __init__(self, file_db='database_gudang.json'):
        self.file_db = file_db
        self.koleksi_barang = []
        self.muat_data()

    def simpan_data(self):
        try:
            with open(self.file_db, 'w') as f:
                data_json = [item.to_dict() for item in self.koleksi_barang]
                json.dump(data_json, f, indent=4)
        except Exception as e:
            print(f"❌ Gagal menyimpan data: {e}")

    def muat_data(self):
        if os.path.exists(self.file_db):
            try:
                with open(self.file_db, 'r') as f:
                    data_load = json.load(f)
                    self.koleksi_barang = [Barang(d['id'], d['nama'], d['harga']) for d in data_load]
            except Exception as e:
                print(f"⚠️ Gagal memuat data lama: {e}")

    def tambah_barang(self, barang_baru):
        if any(item.id_barang == barang_baru.id_barang for item in self.koleksi_barang):
            return False, "ID sudah terdaftar!"
        
        self.koleksi_barang.append(barang_baru)
        self.simpan_data()
        return True, "Berhasil ditambahkan."

    def tampilkan_semua(self):
        if not self.koleksi_barang:
            print("\n [ Gudang Kosong ]")
            return
        
        print("\n" + "="*50)
        print(f"| {'ID':8} | {'NAMA BARANG':20} | {'HARGA':12} |")
        print("-" * 50)
        for item in self.koleksi_barang:
            print(item)
        print("="*50)

    def cari_by_id(self, id_cari):
        for item in self.koleksi_barang:
            if item.id_barang == id_cari:
                return item
        return None 

    def hapus_barang(self, id_hapus):
        for item in self.koleksi_barang:
            if item.id_barang == id_hapus:
                self.koleksi_barang.remove(item)
                self.simpan_data()
                return True
        return False

def main():
    app = Gudang()
    
    while True:
        print("\n>>> SISTEM MANAJEMEN GUDANG V.1.0 <<<")
        print("1. Tambah Barang Baru")
        print("2. Lihat Semua Inventaris")
        print("3. Cari Barang (ID)")
        print("4. Hapus Barang")
        print("5. Keluar")

        pilihan = input("Pilih Menu (1-5): ")
        
        if pilihan == '1':
            print("\n-- Input Barang Baru --")
            id_b = input("Masukkan ID Barang: ")
            nama = input("Masukkan Nama Barang: ")
            try:
                harga = int(input("Masukkan Harga: "))
                status, pesan = app.tambah_barang(Barang(id_b, nama, harga))
                print(f"Status: {pesan}")
            except ValueError:
                print("❌ Input Gagal: Harga harus berupa angka!")
                
        elif pilihan == '2':
            app.tampilkan_semua()
            
        elif pilihan == '3':
            id_c = input("\nMasukkan ID yang dicari: ")
            hasil = app.cari_by_id(id_c)
            if hasil:
                print(f"✅ Ditemukan: {hasil.nama} - Rp{hasil.harga:,}")
            else:
                print("❌ Barang tidak ditemukan.")
                
        elif pilihan == '4':
            id_h = input("\nMasukkan ID yang akan dihapus: ")
            if app.hapus_barang(id_h):
                print("🗑️ Barang berhasil dihapus dari sistem.")
            else:
                print("❌ Gagal: ID tidak ditemukan.")
                
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("⚠️ Pilihan tidak tersedia, silakan coba lagi.")

if __name__ == "__main__":
    main()