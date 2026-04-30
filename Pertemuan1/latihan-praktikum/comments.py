# Program Manajemen Stok Sederhana

# inisialisasi data awal barang
nama_barang = "Lenovo LOQ"
stok_awal = 77
barang_terjual = 23
barang_rusak = 6

# menghitung total pengurangan stok
# menjumlahkan barang terjual dan barang rusak
total_kurang = barang_terjual + barang_rusak

# menghitung sisa stok
stok_akhir = stok_awal - total_kurang

# menampilkan hasil ke layar
print(f"Barang : {nama_barang}")
print(f"Total Kurang : {total_kurang} unit")
print(f"Stok Akhir : {stok_akhir} unit")