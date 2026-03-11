daftar_buku = [
    ["Algoritma dan Pemrograman", 2000],
    ["Basis Data", 2500],
    ["C++", 3000],
    ["Python", 5000],
    ["Struktur Data", 2200]
]

print("Daftar Buku :")

for i in range(len(daftar_buku)):
    print(f"{i + 1}. {daftar_buku[i][0]} (Denda: Rp{daftar_buku[i][1]} per hari)")

pilihan = input("Masukkan nomor buku yang dipilih: ")

if pilihan.isdigit():
    nomor = int(pilihan)
    if 1 <= nomor <= len(daftar_buku):
        buku_terpilih = daftar_buku[nomor - 1]
        print(f"Judul buku : {buku_terpilih[0]}")
        print(f"Denda per hari : Rp{buku_terpilih[1]}")
    else:
        print("\nError")
else:
    print("\nError")