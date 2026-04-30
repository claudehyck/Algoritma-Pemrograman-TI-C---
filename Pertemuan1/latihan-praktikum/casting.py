# Program kalkulator kasir sederhana

nama_barang = input("Nama barang : ") # input data dengan tipe data string
harga_satuan = input("Harga satuan : ")
jumlah = input("Jumlah yang dibeli : ")

# casting
harga_satuan = float(harga_satuan) # harga barang dijadikan tipe data float
jumlah = int(jumlah) # jumlah barang dijadikan tipe data int
total = harga_satuan * jumlah #melakukan perhitungan harga

print("Total yang harus dibayar : Rp" + str(total)) #casting kembali ke str untuk penggabungan teks saat output