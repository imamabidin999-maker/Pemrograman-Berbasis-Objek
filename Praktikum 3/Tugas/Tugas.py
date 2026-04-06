import json
import os

class Karyawan:
    def __init__(self, nik, nama, jabatan):
        self.nik = nik
        self.nama = nama
        self.jabatan = jabatan

    def __str__(self):
        return f"| {self.nik:8} | {self.nama:15} | {self.jabatan:12} |"

    def to_dict(self):
        return {"nik": self.nik, "nama": self.nama, "jabatan": self.jabatan} # [cite: 65]

class SistemKaryawan:
    def __init__(self, file_db='database_karyawan.json'):
        self.file_db = file_db
        self.database_karyawan = []
        self.muat_data()

    def simpan_data(self):
        try:
            with open(self.file_db, 'w') as f:
                list_dict = [k.to_dict() for k in self.database_karyawan]
                json.dump(list_dict, f, indent=4)
        except Exception as e:
            print(f"❌ Gagal menyimpan data: {e}")

    def muat_data(self):
        if os.path.exists(self.file_db):
            try:
                with open(self.file_db, 'r') as f: 
                    data_load = json.load(f)
                    self.database_karyawan = [Karyawan(d['nik'], d['nama'], d['jabatan']) for d in data_load]
            except Exception as e:
                print(f"⚠️ Gagal memuat data lama: {e}")

    def tambah_karyawan(self, karyawan_baru):
        if any(k.nik == karyawan_baru.nik for k in self.database_karyawan):
            print("❌ Gagal: NIK sudah terdaftar!")
            return False
        
        self.database_karyawan.append(karyawan_baru)
        self.simpan_data()
        print("✅ Karyawan berhasil ditambahkan!")
        return True

    def cari_karyawan(self, nik_cari):
        for k in self.database_karyawan:
            if k.nik == nik_cari:
                return k
        return None

    def tampilkan_semua(self):
        if not self.database_karyawan:
            print("\n[ Database Kosong ]")
            return
        
        print("\n" + "="*45)
        print(f"| {'NIK':8} | {'NAMA':15} | {'JABATAN':12} |")
        print("-" * 45)
        for k in self.database_karyawan:
            print(k)
        print("="*45)

def main():
    app = SistemKaryawan()
    
    while True:
        print("\n1. Tambah Karyawan")
        print("2. Cari Karyawan (NIK)")
        print("3. Lihat Semua")
        print("4. Keluar")
        
        pilihan = input("Pilihan: ")
        
        if pilihan == '1':
            nik = input("\nMasukkan NIK: ")
            nama = input("Masukkan Nama: ")
            jabatan = input("Masukkan Jabatan: ")
            
            karyawan_baru = Karyawan(nik, nama, jabatan)
            app.tambah_karyawan(karyawan_baru)
            
        elif pilihan == '2':
            nik_c = input("\nMasukkan NIK yang dicari: ")
            hasil = app.cari_karyawan(nik_c)
            if hasil:
                print(f"✅ Data Ditemukan: {hasil.nama} ({hasil.jabatan})")
            else:
                print("❌ Karyawan tidak ditemukan.")
                
        elif pilihan == '3':
            app.tampilkan_semua()
            
        elif pilihan == '4':
            print("Program selesai. Terimakasih!")
            break
        else:
            print("⚠️ Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()