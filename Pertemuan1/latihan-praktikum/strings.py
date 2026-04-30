# Program Pemrosesan Username dan Kode

# escape Character
pesan_awal = "Data Masuk: \"User_Baru_2026\"\nStatus: Aktif"
print(pesan_awal)

# modify Strings
teks_bersih = pesan_awal.upper().strip()

# string Slicing
username = teks_bersih[12:21]

# mengambil 4 karakter terakhir (Tahun) menggunakan indeks negatif
tahun = teks_bersih[-4:]

print(f"Username hasil slice: {username}")
print(f"Tahun hasil slice: {tahun}")

print("_________________________________________________")
print("\n")

# Program Generator Kartu Nama

nama_depan = "Claudya"
nama_belakang = "Tampubolon"
pekerjaan = "UI/UX Designer"

# string concatenation
nama_lengkap = nama_depan + " " + nama_belakang
print("Nama Lengkap : " + nama_lengkap)

# string format (menggunakan placeholder {} yang diisi oleh argumen di dalam .format())
info_pekerjaan = "Bekerja sebagai: {}".format(pekerjaan)
print(info_pekerjaan)

# F-String
kartu_nama = f"""
----------------------------
Nama      : {nama_lengkap} |
Pekerjaan : {pekerjaan}     |
----------------------------
"""
print(kartu_nama)