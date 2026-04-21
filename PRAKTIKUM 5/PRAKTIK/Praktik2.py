class Karyawan:
    def __init__(self, nama):
        self.nama = nama

    def hitung_gaji(self):
        pass

    def gaji_bersih(self):
        gaji_kotor = self.hitung_gaji()
        if gaji_kotor > 5000000:
            pajak = gaji_kotor * 0.05
            return gaji_kotor - pajak
        return gaji_kotor

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_bulanan):
        super().__init__(nama)
        self.gaji_bulanan = gaji_bulanan

    def hitung_gaji(self):
        return self.gaji_bulanan * 1.10

class KaryawanFreelance(Karyawan):
    def __init__(self, nama, jam_kerja, tarif_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.tarif_per_jam = tarif_per_jam

    def hitung_gaji(self):

        return self.jam_kerja * self.tarif_per_jam

daftar_karyawan = [
    KaryawanTetap("Andi", 5000000),
    KaryawanFreelance("Budi", 100, 20000),
    KaryawanTetap("Citra", 7000000),
    KaryawanFreelance("Dewi", 80, 25000)
]

for karyawan in daftar_karyawan:
    print(f"Nama: {karyawan.nama}")
    print(f"Gaji Kotor  : {karyawan.hitung_gaji():,.0f}")
    print(f"Gaji Bersih : {karyawan.gaji_bersih():,.0f}")
    print("-" * 30)