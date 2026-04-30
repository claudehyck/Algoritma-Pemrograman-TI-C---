# Program Identifikasi dan Konversi Tipe Numerik

# mendefinisikan tipe numerik
angka_bulat = 10 # int
angka_desimal = 10.5 # float
angka_kompleks = 3 + 5j #complex, j adalah simbol imajiner

# menampilkan tipe data
print(f"Nilai : {angka_bulat}, Tipe : {type(angka_bulat)}")
print(f"Nilai : {angka_desimal}, Tipe : {type(angka_desimal)}")
print(F"Nilai : {angka_kompleks}, Tipe : {type(angka_kompleks)}")

# casting
konversi_ke_float = float(angka_bulat) # 10 menjadi 10.0
konversi_ke_int = int(angka_desimal) # 10.5 menjadi 10

print(f"Int ke float : {konversi_ke_float}")
print(f"Float ke int : {konversi_ke_int}")
