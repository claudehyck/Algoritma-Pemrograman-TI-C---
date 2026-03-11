daftar_buku = [
    ["Algoritma dan Pemrograman", 2000],
    ["Basis Data", 2500],
    ["C++", 3000],
    ["Python", 5000],
    ["Struktur Data", 2200]
]

keranjang_pinjaman = []

while True:
    print("\nDaftar Buku Tersedia:")
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. {buku[0]} (Denda: Rp{buku[1]}/hari)")
    
    pilihan = input("\nMasukkan nomor buku yang dipilih (ketik 0 untuk selesai): ")

    if pilihan == '0':
        break

    if pilihan.isdigit():
        nomor = int(pilihan)
        if 1 <= nomor <= len(daftar_buku):
            buku_terpilih = daftar_buku[nomor - 1]
            lama = int(input(f"Berapa hari ingin meminjam '{buku_terpilih[0]}'? "))
            keranjang_pinjaman.append([buku_terpilih[0], lama, buku_terpilih[1]])
            print(f"Berhasil menambahkan '{buku_terpilih[0]}' ke daftar.")
        else:
            print("\nError: Nomor buku tidak tersedia di daftar.")
    else:
        print("\nError: Mohon masukkan angka yang valid.")

if len(keranjang_pinjaman) > 0:
    print("DAFTAR BUKU YANG ANDA PINJAM:")
    for i, item in enumerate(keranjang_pinjaman, 1):
        print(f"{i}. {item[0]} | Durasi: {item[1]} hari")

    print("\nPENGEMBALIAN BUKU")
    while True:
        input_hari = input("Masukkan jumlah hari keterlambatan pengembalian: ")
        
        if input_hari.lstrip('-').isdigit(): 
            hari_terlambat = int(input_hari)
            
            if hari_terlambat >= 0:
                break 
            else:
                print("Error: Hari keterlambatan tidak boleh kurang dari 0!")
        else:
            print("Error: Mohon masukkan angka yang valid.")

    total_denda = 0
    for item in keranjang_pinjaman:
        tarif_denda = item[2]
        total_denda += (tarif_denda * hari_terlambat)

    if hari_terlambat == 0:
        print("STATUS: Tidak ada denda. Terima kasih!")
    else:
        print(f"STATUS: Terlambat {hari_terlambat} hari.")
        print(f"TOTAL DENDA ANDA: Rp{total_denda}")

else:
    print("\nAnda tidak meminjam buku apapun hari ini.")

print("\nTerima kasih telah menggunakan layanan kami!")