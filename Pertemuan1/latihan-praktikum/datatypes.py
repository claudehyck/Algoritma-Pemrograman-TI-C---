# Program Profil Karakter Game

karakter = {
    "nama" : "Kaz Brekker",   # string
    "level" : 25,             # int
    "power" : 96.7,           # float
    "status_hidup" : True     # bool
}

# menggunakan list
inventori = ["Sarung Tangan", "Tongkat", "Bubuk Parem"]

# menampilkan informasi
print(f" PROFIL KARAKTER")
print(f"Nama : {karakter['nama']}")
print(f"Level : {karakter['level']}")

# menambahkan item baru ke dalam list
inventori.append("Pedang")

# pengecekan kondisi karakter
if karakter["status_hidup"]:
    status = "Siap Bertarung"
else :
    status = "Gugur"

print(f"Status : {status}")
print(f"Item : {inventori}") # mencetak list
print(f"Jumlah Item : {len(inventori)}") # len() menghasilkan int