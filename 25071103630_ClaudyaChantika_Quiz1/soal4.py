jumlah_minggu = int(input("Masukkan jumlah minggu untuk rekap: "))
jumlah_kategori = int(input("Masukkan jumlah kategori buku: "))

matriks_rekap = []

for i in range(jumlah_minggu):
    baris_data = []
    print(f"Minggu ke-{i+1}:")
    for j in range(jumlah_kategori):
        jumlah = int(input(f"  Jumlah buku kategori {j+1}: "))
        baris_data.append(jumlah)
    matriks_rekap.append(baris_data)

print("\nTabel Rekapitulasi Peminjaman")
header = "Minggu   |" + "".join([f"  Kategori {j+1}  " for j in range(jumlah_kategori)])
print(header)
print("-" * len(header))

for i in range(jumlah_minggu):
    row_str = f"Mgg {i+1}    |"
    for j in range(jumlah_kategori):
        row_str += f"    {matriks_rekap[i][j]}    "
    print(row_str)

print("\nHasil Rekap")

for i in range(jumlah_minggu):
    total_minggu = sum(matriks_rekap[i])
    print(f"Total Peminjaman Minggu ke-{i+1}: {total_minggu} buku")

for j in range(jumlah_kategori):
    total_kat = 0
    for i in range(jumlah_minggu):
        total_kat += matriks_rekap[i][j]
    print(f"Total Peminjaman Kategori {j+1}: {total_kat} buku")
