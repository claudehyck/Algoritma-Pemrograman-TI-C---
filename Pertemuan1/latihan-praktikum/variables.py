# Program Pendaftaran Mahasiswa

# variable names (nama variabel harus diawali huruf/underscore, tidak boleh angka atau spasi)
namaLengkap = "Claudya Tampubolon" 
usia = 18
StatusAktif = True

# assign multiple values
kelas, jurusan, hobi = 12, "Informatika", "Rakit lego"

# ekskul
nilai_mtk = nilai_fisika = nilai_kimia = 90

# global variable
versi_aplikasi_yang_biasa_digunakannya ="1.0.0"

def update_versi():
    global versi_aplikasi
    versi_aplikasi = "1.1.0"
update_versi()

# output variables
print("Nama Siswa:", namaLengkap)
print("Siswa berada di kelas", kelas, "jurusan", jurusan)
print("Nilai rata-rata eksak:", nilai_mtk)
print("Versi aplikasi yang biasa digunakannya saat ini:", versi_aplikasi)