daftar_buku = [
    ["Algoritma dan Pemrograman", 2000],
    ["Basis Data", 2500],
    ["C++", 3000],
    ["Python", 5000],
    ["Struktur Data", 2200]
]

keranjang_pinjaman = [] 

while True:
    print("\nDaftar Buku :")
    for i in range(len(daftar_buku)):
        print(f"{i + 1}. {daftar_buku[i][0]} (Denda: Rp{daftar_buku[i][1]} per hari)")
    
    pilihan = input("\nMasukkan nomor buku yang dipilih (ketik 0 untuk selesai): ")

    if pilihan == '0':
        break

    if pilihan.isdigit():
        nomor = int(pilihan)
        if 1 <= nomor <= len(daftar_buku):
            buku_terpilih = daftar_buku[nomor - 1]
            lama_pinjam = int(input(f"Berapa hari ingin meminjam '{buku_terpilih[0]}'? "))
            keranjang_pinjaman.append([buku_terpilih[0], lama_pinjam, buku_terpilih[1]])
            print(f"'{buku_terpilih[0]}' ditambahkan ke daftar pinjaman.")
        else:
            print("\nError: Nomor buku tidak tersedia.")
    else:
        print("\nError: Masukkan angka yang valid.")

print("DAFTAR BUKU YANG DIPINJAM :")
total_estimasi_denda = 0

for i, item in enumerate(keranjang_pinjaman, 1):
    judul_buku = item[0]
    durasi = item[1]
    denda_buku = item[2]
    total_estimasi_denda += denda_buku
    
    print(f"{i}. {judul_buku} | Durasi: {durasi} hari")

print(f"Total Estimasi Denda (jika telat 1 hari): Rp{total_estimasi_denda}")
