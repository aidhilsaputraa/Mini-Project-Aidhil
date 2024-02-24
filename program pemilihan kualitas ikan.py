import os
os.system ("cls")

class Ikan:
    def __init__(self, nama, berat, panjang, warna, harga):
        self.nama = nama
        self.berat = berat
        self.panjang = panjang
        self.warna = warna
        self.harga = harga


#ikan ikan tersebut nantinya akan ditentukan kualitasnya dengan menggunakan pengukuran berat dana panjang
# apabila berat melebihi 1 dan panjang melebihi 10cm maka akan termasuk kualitas baik

    def kualitas(self):
        if self.berat >= 1 and self.panjang >= 10:
            return "Kualitas baik"
        else:
            return "Kualitas rendah"

def tampilkan_info(ikan):
    print("Nama:", ikan.nama)
    print("Berat:", ikan.berat, "kg")
    print("Panjang:", ikan.panjang, "cm")
    print ("Warna:", ikan.warna)
    print("Kualitas:", ikan.kualitas())
    print("Dengan Harga: Rp", ikan.harga)

def tambah_ikan():
    nama = input("Masukkan nama ikan: ")
    berat = float(input("Masukkan berat ikan (kg): "))
    panjang = float(input("Masukkan panjang ikan (cm): "))
    warna = float(input("Masukan warna ikan: "))
    harga = int(input("Masukan harga ikan (Rp):"))
    return Ikan(nama, berat, panjang, warna, harga)

def update_ikan(ikan):
    ikan.nama = input("Masukkan nama ikan baru: ")
    ikan.berat = float(input("Masukkan berat ikan baru (kg): "))
    ikan.panjang = float(input("Masukkan panjang ikan baru (cm): "))
    ikan.warna = (input("masukan warna baru ikan: "))
    ikan.harga = int(input("Masukan harga baruk ikan (Rp): "))

def hapus_ikan(daftar_ikan):
    nama_ikan = input("Masukkan nama ikan yang ingin dihapus: ")
    for i in range(len(daftar_ikan)):
        if daftar_ikan[i].nama == nama_ikan:
            del daftar_ikan[i]
            print("Ikan dengan nama", nama_ikan, "telah dihapus.")
            break
    else:
        print("Ikan dengan nama", nama_ikan, "tidak ditemukan.")

# Membuat daftar ikan
daftar_ikan = [
    Ikan("Ikan Lele", 0.8, 7, "coklat", 14000),
    Ikan("Ikan Gurame", 1.5, 12, "merah", 25000),

]

while True:
    os.system("cls")
    print("Menu:")
    print("1. Tampilkan daftar ikan")
    print("2. Tambah ikan")
    print("3. Update informasi ikan")
    print("4. Hapus ikan")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == "1":
        print("Daftar Ikan:")
        for i in range(len(daftar_ikan)):
            print("Ikan", i+1)
            tampilkan_info(daftar_ikan[i])
            print()
        input("Tekan Enter untuk kembali ke menu.")
    elif pilihan == "2":
        ikan_baru = tambah_ikan()
        daftar_ikan.append(ikan_baru)
        print("Ikan telah ditambahkan.")
        input("Tekan Enter untuk kembali ke menu.")
    elif pilihan == "3":
        index = int(input("Masukkan nomor ikan yang ingin diupdate: ")) - 1
        if 0 <= index < len(daftar_ikan):
            update_ikan(daftar_ikan[index])
            print("Informasi ikan telah diupdate.")
        else:
            print("Nomor ikan tidak valid.")
        input("Tekan Enter untuk kembali ke menu.")
    elif pilihan == "4":
        hapus_ikan(daftar_ikan)
        input("Tekan Enter untuk kembali ke menu.")
    elif pilihan == "5":
        print("Program Selesai Terima kasih")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        input("Tekan Enter untuk melanjutkan.")
