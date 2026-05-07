import os

def tampilkan_menu():
    print("\n===========================")
    print("  PYTHON FILE MANAGER v1.0 ")
    print("===========================")
    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")

def list_files():
    semua_file = os.listdir()
    daftar_txt = []
    for file in semua_file:
        if file.endswith(".txt"):
            daftar_txt.append(file)
    return daftar_txt

def main():
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            files = list_files()
            if not files:
                print("Tidak ada file .txt ditemukan.")
            else:
                print("\nFile tersedia:")
                for i in range(len(files)):
                    print(f"[{i+1}] {files[i]}")
                
                try:
                    nomor = int(input("Pilih file (nomor): "))
                    nama_file = files[nomor-1]
                    f = open(nama_file, "r")
                    print(f"\n--- Isi {nama_file} ---")
                    print(f.read())
                    f.close()
                except:
                    print("Terjadi kesalahan atau input tidak valid.")

        elif pilihan == "2":
            files = list_files()
            print("\nDaftar file saat ini:")
            for i in range(len(files)):
                print(f"[{i+1}] {files[i]}")
            print("Ketik nomor file lama atau masukkan nama file baru (contoh: baru.txt):")
            input_user = input("Pilihan: ")

            try:
                if input_user.isdigit() and 1 <= int(input_user) <= len(files):
                    nama_file = files[int(input_user)-1]
                else:
                    nama_file = input_user
                    if not nama_file.endswith(".txt"):
                        nama_file += ".txt"
                
                isi_teks = input("Masukkan isi teks: ")
                f = open(nama_file, "w")
                f.write(isi_teks)
                f.close()
                print("File berhasil disimpan!")
            except:
                print("Gagal menulis file.") 

        elif pilihan == "3":
            files = list_files()
            if not files:
                print("Tidak ada file .txt ditemukan.")
            else:
                for i in range(len(files)):
                    print(f"[{i+1}] {files[i]}")
                
                try:
                    nomor = int(input("Pilih nomor file untuk dihapus: "))
                    nama_file = files[nomor-1]
                    
                    konfirmasi = input(f"Yakin ingin menghapus {nama_file}? (y/n): ")
                    if konfirmasi.lower() == "y":
                        os.remove(nama_file)
                        print("File berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                except:
                    print("Gagal menghapus file.")

        elif pilihan == "0":
            print("Keluar program...")
            break
        
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()