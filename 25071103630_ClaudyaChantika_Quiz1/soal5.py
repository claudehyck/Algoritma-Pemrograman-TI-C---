class Buku:
    def __init__(self, judul, denda_per_hari):
        self.judul = judul
        self.denda_per_hari = denda_per_hari

    def tampilkan(self):
        print(f"{self.judul} - Denda Rp {self.denda_per_hari}/hari")

class Peminjaman:
    def __init__(self):
        self.total_denda = 0

    def tambah(self, buku, hari_terlambat):
        denda_tambahan = buku.denda_per_hari * hari_terlambat
        self.total_denda += denda_tambahan
        print(f"Berhasil menambahkan denda untuk '{buku.judul}'.")

    def ringkasan(self):
        print("\n" + "-"*30)
        print(f"TOTAL DENDA AKHIR: Rp {self.total_denda}")
        print("-"*30)

data_buku_raw = [
    ["Algoritma dan Pemrograman", 2000],
    ["Basis Data", 2500],
    ["C++", 3000],
    ["Python", 5000],
    ["Struktur Data", 2200]
]

daftar_objek_buku = []
for data in data_buku_raw:
    objek = Buku(data[0], data[1])
    daftar_objek_buku.append(objek)

print(" DAFTAR BUKU ")
for i, buku in enumerate(daftar_objek_buku, 1):
    print(f"{i}. ", end="")
    buku.tampilkan()

transaksi = Peminjaman()

while True:
    pilihan = input("\nPilih nomor buku (0 untuk selesai): ")
    
    if pilihan == '0':
        break
        
    if pilihan.isdigit():
        indeks = int(pilihan) - 1
        if 0 <= indeks < len(daftar_objek_buku):
            buku_yang_dipilih = daftar_objek_buku[indeks]
            hari = int(input(f"Berapa hari keterlambatan untuk '{buku_yang_dipilih.judul}'? "))
            transaksi.tambah(buku_yang_dipilih, hari)
        else:
            print("Nomor tidak tersedia.")
    else:
        print("Masukkan angka!")

transaksi.ringkasan()