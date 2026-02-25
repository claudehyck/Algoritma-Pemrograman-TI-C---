# Misalnya, Sontri punya 10 permen yang ingin dibagikan secara rata kepada sejumlah orang yang diinput oleh user.
# 1.	Program akan meminta input jumlah orang.
# 2.	Input harus berupa angka bulat (integer).
# 3.	Program harus menangani jika user memasukkan "0”
# 4.	Program harus menangani jika user memasukkan teks/huruf, bukan angka.

print("--- Program Pembagi 10 Permen ---")

try:
    jumlah_orang = int(input("Masukkan jumlah orang: "))
    hasil = 10 / jumlah_orang

except ValueError:
    print("Error: Tolong masukkan angka bulat, bukan huruf atau simbol.")

except ZeroDivisionError:
    print("Error: Kamu tidak bisa membagi permen kepada 0 orang.")

except Exception as e:
    print(f"Terjadi kesalahan yang tidak terduga: {e}")

else:
    print(f"Masing-masing orang mendapatkan {hasil} permen.")

finally:
    print("Terima kasih telah menggunakan program pembagi permen ini.")