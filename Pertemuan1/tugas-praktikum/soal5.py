# Soal 5 (Fungsi)

# membuat fungsi bernama hitung(a, b)
def hitung(a, b):
    tambah = a + b
    kurang = a - b
    return tambah, kurang

# memanggil fungsi tersebut
hasil_tambah, hasil_kurang = hitung(5, 3)

# menampilkan hasil ke layar
print("Penjumlahan =", hasil_tambah)
print("Pengurangan =", hasil_kurang)