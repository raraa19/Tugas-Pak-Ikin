class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status =status

    def __str__(self):
        return f"{self.judul} - {self.penulis} - ({self.genre}) - Status: {self.status}"
    
    #kelas perpustakaan :

class perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("koleksi buku kosong.")

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
            print(f"Buku dengan judul '{judul}'tidak ditemukan.")

    def pinjam_buku(self, buku, anggota):
        if buku.status == "Tersedia":
            buku.status = "Dipinjam"
            anggota.buku_pinjaman.append(buku)
            print(f"Buku '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
        else:
            print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")

# KELAS ANGGOTA

        class Anggota:
            def __init__(self, nama, ID):
                self.nama = nama
                self.ID = ID
                self.buku_pinjaman = []

            def tampilkan_buku_pinjaman(self):
                if self.buku_pinjaman:
                    print(f"-- Buku Pinjaman {self.nama} --")
                for buku in self.buku_pinjaman:
                    print(buku)
                else:
                    print(f"{self.nama} tidak memiliki buku pinjaman.")

 #KELAS MAIN;

    def main():
    # buat beberapa buku
        buku1 = Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")   
        buku2 = Buku("Laskar Pelangi", "Andrea Hirata", "Fiksi", "Tersedia")   
        buku3 = Buku("Filosofi Terbang", "Dewi Lestari", "Fiksi", "Dipinjam") 

    # buat perpustakaan dan anggota
    perpustakaan = perpustakaan()
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

    anggota1 = Anggota("Sinar", 12345)
    anggota2 = Anggota("Ayass", 56789)

    # jalankan program
    print("\n-- Menu Persputakaan --")
    print("1. Tampilkan Daftar Buku")
    print("2. Cari Buku")
    print("1. Pinjam Buku")
    print("1. Kembalian")
    angka=int(input("pilih menu :_"))

    if angka == 1:
        perpustakaan.tampilkan_buku()
    elif angka == 2:
        judul=input("input judul buku:")
        perpustakaan.cari_buku(judul)
    elif angka== 3:
        buku=input("buku yang dipinjam:")
        anggota=input("input nama anggota:")
        perpustakaan.pinjam_buku(buku, anggota)
    else:
        print("anda salah pilih")

if __name__=="__main__":
    main()


























