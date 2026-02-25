#nomor 1
def rata_rata(nilai):
    if not nilai:
        return "Data kosong"
    
    total = sum(nilai)
    jumlah_data = len(nilai)
    hasil = total / jumlah_data
    return hasil

daftar_nilai = [80, 75, 90, 60, 85]
hasil_perhitungan = rata_rata(daftar_nilai)

print(f"List nilai: {daftar_nilai}")
print(f"Rata-rata: {hasil_perhitungan}")
print()

#nomor 2
def bilangan_prima(n):
    daftar_prima = []
    for angka in range(1, n + 1):
        if angka > 1:
            adalah_prima = True
            for i in range(2, int(angka**0.5) + 1):
                if (angka % i) == 0:
                    adalah_prima = False
                    break
            if adalah_prima:
                daftar_prima.append(angka)
    return daftar_prima
n_input = 50
hasil_prima = bilangan_prima(n_input)
print(f"Bilangan prima dari 1 sampai {n_input} adalah:")
print(hasil_prima)
print()

#nomor 3
def jumlah_digit(n):
    if n < 10:
        return n
    else:
        return (n % 10) + jumlah_digit(n // 10)
input_angka = 1234
hasil_jumlah = jumlah_digit(input_angka)

print(f"Input: {input_angka}")
print(f"Output: {hasil_jumlah}")
print()

#nomor 4
def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)
hasil = pangkat_rekursif(2, 5)
print(f"Output: {hasil}")
print()

#nomor 5
import math
def jarak(x1, y1, x2, y2):
    dx = (x2 - x1) ** 2
    dy = (y2 - y1) ** 2
    return math.sqrt(dx + dy)

hasil_jarak = jarak(0, 0, 3, 4)
print(f"Jarak = {hasil_jarak}")