DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]

riwayat = []

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    if pilihan_pemain == pilihan_komputer:
        return "Seri"

    if (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
       (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
       (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "Pemain"
    else:
        return "Komputer"

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)] 
    while True:
        tebakan = input("Masukkan pilihan batu / gunting / kertas : ").lower()
        if tebakan in DAFTAR_PILIHAN:
            break
        print("Input tidak valid! Pilih antara batu, gunting, atau kertas.")
    hasil = tentukan_pemenang(tebakan, pilihan_komputer)
    if hasil == "pemain":
        print("Pemain menang")
    elif hasil == "seri":
        print("Seri")
    else:
        print("Kalah")

def main_satu_ronde(nama, nomor_ronde):
    nomor_ronde = 0
    menang_pemain = 0
    menang_komputer = 0
    while menang_pemain < 3 and menang_komputer < 3:
        hasil = main_satu_giliran(nomor_ronde)
        if hasil == "pemain":
            menang_pemain += 1
        elif hasil == "komputer":
            menang_komputer += 1
        
        total_giliran += 1
        print(f"Skor Sementara - {nama}: {menang_pemain}, Komputer: {menang_komputer}")

    skor = 0
    if menang_pemain == 3:
        print(f"\nSelamat! {nama} memenangkan ronde ini.")
        skor = menang_pemain * 10
    else:
        print("\nKomputer memenangkan ronde ini.")
        skor = 0
        
        return [nama, skor]

# Bagian B ________

def tampilkan_riwayat(riwayat):
    if not riwayat:
        print("\nBelum ada riwayat.")
        return

    print("\n=== RIWAYAT PERMAINAN ===")
    print(f"{'No'} | {'Nama'} | {'Skor'}")
    print("----------------------------")
    
    for i in range(len(riwayat)):
        nomor = i + 1
        nama_pemain = riwayat[i][0]
        skor_pemain = riwayat[i][1]
        print(f"{nomor} | {nama_pemain} | {skor_pemain}")

tampilkan_riwayat(riwayat)