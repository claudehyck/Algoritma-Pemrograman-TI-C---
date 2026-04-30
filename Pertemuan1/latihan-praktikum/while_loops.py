# Program Tebak Angka

# tentukan angka rahasia
angka_rahasia = 9
tebakan = 0

print("TEBAK ANGKA (1-10)!")

# loop akan terus berjalan selagi tebakan tidak sama dengan angka_rahasia
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan Anda : "))
    
    if tebakan != angka_rahasia:
        print("Salah! Coba lagi.")

# keluar dari loop jika tebakan benar
print("Selamat! Anda berhasil menebak angkanya.")