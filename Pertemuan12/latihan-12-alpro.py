struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder: dict) -> int:
    total = 0
    for item, nilai in folder.items():
        if type(nilai) == dict:
            total += total_ukuran(nilai)
        else:
            total += nilai
    return total

def hitung_file(folder: dict) -> int:
    jumlah = 0
    for item, nilai in folder.items():
        if type(nilai) == dict:
            jumlah += hitung_file(nilai)
        else:
            jumlah += 1
    return jumlah

def cari_terbesar(folder: dict) -> tuple:
    nama_terbesar = ""
    ukuran_terbesar = -1
    for item, nilai in folder.items():
        if type(nilai) == dict:
            sub_nama, sub_ukuran = cari_terbesar(nilai)
            if sub_ukuran > ukuran_terbesar:
                ukuran_terbesar = sub_ukuran
                nama_terbesar = sub_nama
        else:
            if nilai > ukuran_terbesar:
                ukuran_terbesar = nilai
                nama_terbesar = item
    return nama_terbesar, ukuran_terbesar

def tampilkan_tree(folder: dict, level: int = 0):
    for item, nilai in folder.items():
        indentasi = " " * level
        if type(nilai) == dict:
            print(f"{indentasi}{item}")
            tampilkan_tree(nilai, level + 1)
        else:
            print(f"{indentasi}{item} ({nilai} KB)")

print("=== LAPORAN SKRIPSI AQIL ===")
print(f"Total ukuran skripsi: {total_ukuran(struktur)} KB")
print(f"Jumlah file: {hitung_file(struktur)} file")
file_top, ukuran_top = cari_terbesar(struktur)
print(f"File terbesar: {file_top} ({ukuran_top} KB)")
print("\nStruktur Folder:")
tampilkan_tree(struktur)