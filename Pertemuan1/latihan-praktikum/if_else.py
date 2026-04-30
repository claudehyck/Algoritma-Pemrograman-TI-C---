# Program Validasi Login

# data akun yang disimpan
user = "Alga Merah"
password = "T1nggiK4lsium"
akun_aktif = True

# input simulasi
input_user = "Alga Merah"
input_pass = "Tingg1K4lsium"

# nested if
if input_user == user :
    print("[Sistem]: Username benar, mengecek password...")

    if input_pass == password :
        # mengecek status akun aktif
        if akun_aktif :
            print ("Login Berhasil")
        else :
            print("Login Gagal")
    else :
        print("Password Salah")
else :
    print("Username Tidak Ditemukan")

# note : passwordnya memang sengaja dibuat salah hehe