# Program menentukan pemberian akses berdasarkan umur minimal

usia_minimal = 21
input_usia = int(input("Masukkan usia : ")) # input dari user
diberiakses = input_usia >= usia_minimal # penggunaan boolean untuk mengecek data

print(f"Status akses : {diberiakses}")

if diberiakses :
    print("Halo! Selamat datang.")
else :
    print("Maaf, anda belum memenuhi batas usia.")