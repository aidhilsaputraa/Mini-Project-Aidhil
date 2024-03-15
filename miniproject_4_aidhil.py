import os
os.system("cls")

class Node:
    def __init__(self, data, berat=None, ukuran=None, warna=None, harga=None):
        self.data = data
        self.berat = berat
        self.ukuran = ukuran
        self.warna = warna
        self.harga = harga
        self.kualitas = self.periksa_kualitas()
        self.next = None

    def periksa_kualitas(self):
        if self.berat is not None and self.ukuran is not None:
            if float(self.berat) > 1 and float(self.ukuran) > 10:
                return "Baik"
        return "Biasa"


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_ikan_dari_depan(self, data, berat=None, ukuran=None, warna=None, harga=None):
        ikan_baru = Node(data, berat, ukuran, warna, harga)
        ikan_baru.next = self.head
        self.head = ikan_baru

    def tambah_ikan_dari_belakang(self, data, berat=None, ukuran=None, warna=None, harga=None):
        if self.head is None:
            self.head = Node(data, berat, ukuran, warna, harga)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data, berat, ukuran, warna, harga)

    def tambah_ikan_di_tengah(self, data, posisi, berat=None, ukuran=None, warna=None, harga=None):
        if posisi <= 0:
            self.tambah_ikan_dari_depan(data, berat, ukuran, warna, harga)
        elif posisi > self.hitung_jumlah_ikan():
            self.tambah_ikan_dari_belakang(data, berat, ukuran, warna, harga)
        else:
            ikan_baru = Node(data, berat, ukuran, warna, harga)
            current = self.head
            for _ in range(posisi - 2):
                current = current.next
            ikan_baru.next = current.next
            current.next = ikan_baru

    def hapus_ikan(self, posisi):
        if self.head is None:
            print("Daftar ikan masih kosong")
            return
        elif posisi <= 0:
            print("Posisi harus lebih besar dari 0")
            return
        elif posisi == 1:
            self.head = self.head.next
        elif posisi > self.hitung_jumlah_ikan():
            print("Posisi yang dimasukkan melebihi jumlah ikan yang ada")
            return
        else:
            current = self.head
            prev = None
            count = 1
            while current and count != posisi:
                prev = current
                current = current.next
                count += 1
            if current is None:
                print("Posisi yang dimasukkan melebihi jumlah ikan yang ada")
                return
            prev.next = current.next

    def tampilkan_daftar_ikan(self):
        current = self.head
        nomor = 1
        if current is None:
            print("Daftar ikan masih kosong")
            return
        while current:
            print("Nomor:", nomor)
            print("Nama:", current.data)
            print("Berat:", current.berat)
            print("Ukuran:", current.ukuran)
            print("Warna:", current.warna)
            print("Harga:", current.harga)
            print("Kualitas:", current.kualitas)
            current = current.next
            nomor += 1
        print()

    def hitung_jumlah_ikan(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def perbarui_informasi_ikan(self, posisi, data, berat=None, ukuran=None, warna=None, harga=None):
        current = self.head
        count = 1
        while current and count != posisi:
            current = current.next
            count += 1
        if current is None:
            print("Posisi yang dimasukkan melebihi jumlah ikan yang ada")
            return
        else:
            current.data = data
            current.berat = berat
            current.ukuran = ukuran
            current.warna = warna
            current.harga = harga
            current.kualitas = current.periksa_kualitas()

    def sort_berat(self, ascending=True):
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if (ascending and current.berat > current.next.berat) or (
                        not ascending and current.berat < current.next.berat):
                    current.data, current.next.data = current.next.data, current.data
                    current.berat, current.next.berat = current.next.berat, current.berat
                    current.ukuran, current.next.ukuran = current.next.ukuran, current.ukuran
                    current.warna, current.next.warna = current.next.warna, current.warna
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.kualitas, current.next.kualitas = current.next.kualitas, current.kualitas
                    swapped = True
                current = current.next

    def sort_nama(self, ascending=True):
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if (ascending and current.data > current.next.data) or (
                        not ascending and current.data < current.next.data):
                    current.data, current.next.data = current.next.data, current.data
                    current.berat, current.next.berat = current.next.berat, current.berat
                    current.ukuran, current.next.ukuran = current.next.ukuran, current.ukuran
                    current.warna, current.next.warna = current.next.warna, current.warna
                    current.harga, current.next.harga = current.next.harga, current.harga
                    current.kualitas, current.next.kualitas = current.next.kualitas, current.kualitas
                    swapped = True
                current = current.next

    def sort_ascending(self, key='berat'):
        if key == 'berat':
            self.sort_berat()
        elif key == 'nama':
            self.sort_nama()

    def sort_descending(self, key='berat'):
        if key == 'berat':
            self.sort_berat(ascending=False)
        elif key == 'nama':
            self.sort_nama(ascending=False)

    def jump_search(self, key, by='nama'):
        n = self.hitung_jumlah_ikan()
        step = int(n ** 0.5)
        prev = None
        current = self.head
        
        while current and current.data < key:
            prev = current
            for _ in range(min(step, n)):
                if current.next:
                    current = current.next
            n -= step
        
        while prev:
            if by == 'nama' and prev.data == key:
                return prev
            elif by == 'warna' and prev.warna == key:
                return prev
            prev = prev.next
        
        return None


def main():
    daftar_ikan = LinkedList()
    daftar_ikan.tambah_ikan_dari_depan("Nila", berat=0.8, ukuran=10, warna="Silver", harga=12000)
    daftar_ikan.tambah_ikan_dari_belakang("Lele", berat=0.9, ukuran=8, warna="Coklat", harga=10000)
    daftar_ikan.tambah_ikan_dari_depan("Gurame", berat=1.8, ukuran=12, warna="Merah Maron", harga=17000)
    daftar_ikan.tambah_ikan_dari_belakang("Patin", berat=1.3, ukuran=12, warna="Putih", harga=15000)
    daftar_ikan.tambah_ikan_dari_depan("Bawal", berat=0.6, ukuran=10, warna="Orange", harga=9000)
    daftar_ikan.tambah_ikan_dari_belakang("Papuyu", berat=0.7, ukuran=7, warna="Hijau", harga=6000)
    daftar_ikan.tambah_ikan_dari_depan("Belut", berat=0.5, ukuran=11, warna="Coklat", harga=11000)

    while True:
        print("Menu:")
        print("1. Tampilkan daftar ikan")
        print("2. Tambah ikan di depan")
        print("3. Tambah ikan di belakang")
        print("4. Tambah ikan di tengah")
        print("5. Hapus ikan")
        print("6. Perbarui daftar ikan")
        print("7. Search atau mencari ikan")
        print("8. Sorting berdasarkan berat (Ascending)")
        print("9. Sorting berdasarkan berat (Descending)")
        print("10. Sorting berdasarkan nama (Ascending)")
        print("11. Sorting berdasarkan nama (Descending)")
        print("12. Keluar")

        pilihan = input("Masukkan pilihan (1-12): ")

        if pilihan == "1":
            print("Daftar Ikan:")
            daftar_ikan.tampilkan_daftar_ikan()
            input("Tekan Enter untuk kembali ke menu")
        elif pilihan == "2":
            data = input("Masukkan nama ikan: ")
            berat = input("Masukkan berat ikan: ")
            ukuran = input("Masukkan ukuran ikan: ")
            warna = input("Masukkan warna ikan: ")
            harga = input("Masukkan harga ikan: ")
            daftar_ikan.tambah_ikan_dari_depan(data, berat, ukuran, warna, harga)
        elif pilihan == "3":
            data = input("Masukkan nama ikan: ")
            berat = input("Masukkan berat ikan: ")
            ukuran = input("Masukkan ukuran ikan: ")
            warna = input("Masukkan warna ikan: ")
            harga = input("Masukkan harga ikan: ")
            daftar_ikan.tambah_ikan_dari_belakang(data, berat, ukuran, warna, harga)
        elif pilihan == "4":
            data = input("Masukkan nama ikan: ")
            posisi = int(input("Masukkan nomor posisi untuk menambahkan ikan: "))
            berat = input("Masukkan berat ikan: ")
            ukuran = input("Masukkan ukuran ikan: ")
            warna = input("Masukkan warna ikan: ")
            harga = input("Masukkan harga ikan: ")
            daftar_ikan.tambah_ikan_di_tengah(data, posisi, berat, ukuran, warna, harga)
        elif pilihan == "5":
            posisi = int(input("Masukkan nomor posisi ikan yang ingin dihapus: "))
            daftar_ikan.hapus_ikan(posisi)
        elif pilihan == "6":
            posisi = int(input("Masukkan nomor posisi untuk memperbarui ikan: "))
            data = input("Masukkan nama ikan: ")
            berat = input("Masukkan berat ikan: ")
            ukuran = input("Masukkan ukuran ikan: ")
            warna = input("Masukkan warna ikan: ")
            harga = input("Masukkan harga ikan: ")
            daftar_ikan.perbarui_informasi_ikan(posisi, data, berat, ukuran, warna, harga)
        elif pilihan == "7":
            print("Pilihan pencarian:")
            print("1. Berdasarkan nama")
            print("2. Berdasarkan warna")
            search_choice = input("Masukkan pilihan pencarian (1/2): ")
            if search_choice == "1":
                keyword = input("Masukkan nama ikan yang ingin dicari: ")
                result = daftar_ikan.jump_search(keyword, by='nama')
                if result:
                    print("Ikan ditemukan:")
                    print("Nama:", result.data)
                    print("Berat:", result.berat)
                    print("Ukuran:", result.ukuran)
                    print("Warna:", result.warna)
                    print("Harga:", result.harga)
                    print("Kualitas:", result.kualitas)
                else:
                    print("Ikan tidak ditemukan.")
            elif search_choice == "2":
                keyword = input("Masukkan warna ikan yang ingin dicari: ")
                result = daftar_ikan.jump_search(keyword, by='warna')
                if result:
                    print("Ikan ditemukan:")
                    print("Nama:", result.data)
                    print("Berat:", result.berat)
                    print("Ukuran:", result.ukuran)
                    print("Warna:", result.warna)
                    print("Harga:", result.harga)
                    print("Kualitas:", result.kualitas)
                else:
                    print("Ikan tidak ditemukan.")
        elif pilihan == "8":
            daftar_ikan.sort_ascending(key='berat')
        elif pilihan == "9":
            daftar_ikan.sort_descending(key='berat')
        elif pilihan == "10":
            daftar_ikan.sort_ascending(key='nama')
        elif pilihan == "11":
            daftar_ikan.sort_descending(key='nama')
        elif pilihan == "12":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
