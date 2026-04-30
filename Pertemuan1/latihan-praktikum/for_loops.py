# Program Filter Email

# daftar alamat email
list_email = {
    "claudyatampubolon@gmail.com",
    "sun.ctchan@gmail.com",
    "grishaverse@gmail.com",
    "himmel.ubi@gmail.com"
}

print("Mencari email dengan domain 'ubi' : ")

jumlah_ditemukan = 0

# loop
for email in list_email :
    # mengecek kata yang telah ditentukan ada di dalam string email
    if "ubi" in email :
        print(f"[DITEMUKAN]: {email}")
        jumlah_ditemukan += 1
    else :
        print(f"[TIDAK DITEMUKAN]: {email}")
