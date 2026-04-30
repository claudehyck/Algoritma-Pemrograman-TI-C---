# Program Sistem Keamanan Gudang

# arithmetic & assignment operators
stok_awal = 100
barang_masuk = 50
stok_awal += barang_masuk
kapasitas_maksimal = 200
sisa_ruang = kapasitas_maksimal - stok_awal

# comparison & logical operators (untuk mengecek kapasitas stok)
aman = stok_awal > 5 and stok_awal <= kapasitas_maksimal

# identity operators
admin_aktif = "Claudya"
user_sekarang = "Claudya"
apakah_admin = user_sekarang is admin_aktif

print(f"Total Stok : {stok_awal}")
print(f"Status Stok Aman : {aman}") # boolean
print(f"Apakah User adalah Admin : {apakah_admin}")

print("_________________________________________________")
print("\n")

# Program Filter Akses dan Enkripsi Sederhana

# membership operators
# mengecek keberadaan suatu nilai di dalam koleksi (List/Tuple/Set)
daftar_terlarang = ["virus.exe", "malware.py", "keylogger.js"]
file_upload = "dokumen.pdf"

# mengecek keamanan file aman
is_aman = file_upload not in daftar_terlarang # membership

# bitwise operators
# angka dalam kode biner: 5 (0101), 3 (0011)
kode_akses = 5 
kunci_enkripsi = 3

# bitwise AND (&)
hasil_and = kode_akses & kunci_enkripsi

# bitwise XOR (^)
terenkripsi = kode_akses ^ kunci_enkripsi
terdekripsi = terenkripsi ^ kunci_enkripsi

# output
print(f"Apakah file '{file_upload}' aman? {is_aman}")
print(f"Bitwise AND: {hasil_and}")
print(f"Data Terenkripsi (XOR): {terenkripsi}")
print(f"Data Terdekripsi Kembali: {terdekripsi}")