class Barang:
    def __init__(self, id_barang, nama):
        self.id_barang = id_barang
        self.nama = nama

class Gudang:
    def __init__(self):
        self.koleksi_barang = []

    def tambah_barang(self, barang_baru):
        self.koleksi_barang.append(barang_baru)
        print(f"✅ {barang_baru.nama} berhasil masuk gudang.")

    def tambah_dengan_validasi(self, barang_baru):
        if any(item.id_barang == barang_baru.id_barang for item in self.koleksi_barang):
            print("❌ Error: ID sudah terdaftar!")
        else:
            self.koleksi_barang.append(barang_baru)

    def tampilkan_semua(self):
        print("\n--- DAFTAR BARANG DI GUDANG ---")
        for item in self.koleksi_barang:
            print(f"ID: {item.id_barang} | Nama: {item.nama}")

    def cari_by_id(self, id_cari):
        for item in self.koleksi_barang:
            if item.id_barang == id_cari:
                return item
        return None

    def filter_nama(self, kata_kunci):
        hasil = [item for item in self.koleksi_barang if kata_kunci.lower() in item.nama.lower()]
        return hasil

    def hitung_total_aset(self):
        total = sum(item.harga for item in self.koleksi_barang)
        return total

    def urutkan_nama(self):
        self.koleksi_barang.sort(key=lambda x: x.nama)
        print("Sorting selesai.")

    def update_nama(self, id_target, nama_baru):
        objek = self.cari_by_id(id_target)
        if objek:
            objek.nama = nama_baru
            print("📝 Nama barang berhasil diperbarui.")

    def hapus_barang(self, id_hapus):
        objek = self.cari_by_id(id_hapus)
        if objek:
            self.koleksi_barang.remove(objek)
            print(f"🗑️ Barang ID {id_hapus} telah dihapus.")
        else:
            print("❌ Barang tidak ditemukan.")

gudang_utama = Gudang()

gudang_utama.tambah_barang(Barang("A1", "Laptop ASUS"))
gudang_utama.tambah_barang(Barang("B2", "Mouse Logi"))

gudang_utama.tampilkan_semua()

gudang_utama.update_nama("B2", "Mouse Logitech Wireless")
hasil = gudang_utama.cari_by_id("A1")
if hasil:
    print(f"Hasil Cari: {hasil.nama}")

gudang_utama.hapus_barang("A1")
gudang_utama.tampilkan_semua()