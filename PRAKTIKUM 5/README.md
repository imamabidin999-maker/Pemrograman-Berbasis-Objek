1. Penjelasan Practice 1
Kode `Praktik1.py` mendemonstrasikan konsep dasar polimorfisme melalui metode yang memiliki nama yang sama tetapi perilaku yang berbeda sesuai dengan jenis kendaraannya.

* Inheritance (Pewarisan): Kelas `kendaraan` bertindak sebagai parent class yang memiliki atribut `kecepatan`. Kelas `mobil`, `motor`, `pesawat`, dan `kapal` mewarisi atribut ini menggunakan fungsi `super().__init__()`.
* Polimorfisme pada Method `berjalan()`: Setiap kelas anak melakukan override pada method `berjalan()` untuk memberikan pesan spesifik, misalnya pesawat "terbang di udara" sementara kapal "berlayar di laut".
* Implementasi List & Looping: Semua objek kendaraan dimasukkan ke dalam satu list `daftar_kendaraan`. Saat dilakukan looping, Python secara otomatis mengenali method `berjalan()` dan `laju()` mana yang harus dijalankan berdasarkan tipe objeknya.

2. Penjelasan Practice 2
Kode `Praktik2.py` menunjukkan penerapan polimorfisme dalam perhitungan logika bisnis yang lebih kompleks.

* Logika Berbeda dalam Method yang Sama: Method `hitung_gaji()` pada `KaryawanTetap` mengembalikan gaji bulanan ditambah bonus 10%. Sedangkan pada `KaryawanFreelance`, gaji dihitung berdasarkan perkalian jam kerja dengan tarif.
* Method `gaji_bersih()`: Method ini berada di parent class (`Karyawan`) dan digunakan oleh semua anak kelas. Di dalamnya terdapat logika pengecekan pajak 5% jika total gaji kotor melebihi 5 juta.
* Kemudahan Manajemen: Melalui polimorfisme, Anda bisa menghitung gaji berbagai jenis karyawan hanya dengan satu perulangan `for` tanpa perlu menggunakan banyak instruksi `if-else` untuk mengecek tipe karyawannya.

3. Penjelasan Practice 3: Sistem Gudang Polimorfik (Standar Industri)
Kode `Praktik3.py` adalah tahap lanjutan yang menggabungkan OOP dengan penyimpanan data eksternal (JSON).

* Solusi Identitas "Tipe": Agar program tahu objek mana yang harus menjadi `BarangElektronik` atau `BarangKonsumsi` saat dimuat kembali, ditambahkan atribut `"tipe"` pada data JSON.
* Method `to_dict()`: Digunakan untuk mengubah objek Python menjadi format dictionary agar bisa disimpan ke dalam file `.json`.
* Validasi Tanggal dengan `datetime`: Pada kelas `BarangKonsumsi`, method `info()` dimodifikasi untuk membandingkan tanggal kadaluarsa dengan waktu sistem saat ini menggunakan modul `datetime`. Jika sudah lewat, akan muncul label (KADALUARSA!).
* Muat Data Cerdas:** Method `muat_data()` menggunakan logika `if-elif` untuk membaca label tipe dari JSON dan membangun kembali objek dengan kelas yang tepat.

4. Penjelasan Tugas Praktik: Final Warehouse System
Kode `Praktik.py` adalah implementasi utuh dari seluruh materi yang telah dipelajari, yang kini diaplikasikan pada dataset spesifik sesuai instruksi tugas.

* Otomasi Laporan: Polimorfisme bekerja penuh pada method `laporan_stok()`. Meskipun list `koleksi` berisi berbagai macam jenis barang, pemanggilan `b.info()` secara otomatis akan menampilkan "Garansi" untuk monitor dan "Status Aman/Kadaluarsa" untuk susu atau roti.
* Persistensi Data: Data hasil input (seperti Monitor 4500K atau Susu MBG) tersimpan secara permanen dalam file `gudang_final.json`. Hal ini menjamin bahwa saat aplikasi dijalankan ulang, objek tetap memiliki perilaku dan data yang konsisten sesuai kelas asalnya[cite: 153].
* Error Handling: Terdapat blok `try-except` pada pengecekan tanggal untuk mengantisipasi jika format tanggal pada file JSON tidak sesuai, sehingga program tidak langsung berhenti (*crash*).
