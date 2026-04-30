# Program Sistem Diskon (Menggunakan Decorator, Lambda, *args atau *kwargs, dan Scope)

pajak = 0.1 # global scope

# Decorator : fungsi yang membungkus fungsi lain
def info_dekorator(fungsi):
    def bungkus(*args, **kwargs):
        print(f"\n[LOG]: Menjalankan fungsi '{fungsi.__name__}'")
        return fungsi(*args, **kwargs)
    return bungkus

# Menggunakan Decorator dan *args atau **kwargs
@info_dekorator
def hitung_total(nama_produk, *harga_item, **info_tambahan):
    # local scope : variabel total hanya ada di dalam fungsi ini
    total = sum(harga_item)
    # lambda : fungsi anonim singkat untuk menghitung diskon
    # jika member ada di **kwargs, diskon 20%, jika tidak maka 0%
    diskon_func = lambda t: t*0.2 if info_tambahan.get("member") else 0

    hasil_akhir = total - diskon_func(total)
    return f"Produk : {nama_produk} | Total Bayar : {hasil_akhir + (hasil_akhir * pajak)}"

print(hitung_total("Belanja Mingguan", 50000, 25000, 25000, member = True))

print("_______________________________________________________________________________")
print("\n")

# Program Matematika

# Recursion : fungsi memanggil dirinya sendiri
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Generator : menggunakan 'yield' agar tidak menggunakan RAM besar
def deret_angka(maksimal):
    angka = 1
    while angka <= maksimal:
        yield angka  # mengembalikan nilai sementara dan 'pause'
        angka += 1

# Eksekusi gabungan
for nomor in deret_angka(5):
    hasil = faktorial(nomor)
    print(f"Faktorial dari {nomor} adalah: {hasil}")