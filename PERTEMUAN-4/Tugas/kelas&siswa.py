class Kelas:
    def __init__(self, nama_kelas, jurusan):
        self.nama_kelas = nama_kelas
        self.jurusan = jurusan
        self.daftar_siswa = []

    def tambah_siswa(self, siswa):
        self.daftar_siswa.append(siswa)

class Siswa:
    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIS: {self.nis}")
        print(f"Kelas: {self.kelas.nama_kelas}")
        print(f"Jurusan: {self.kelas.jurusan}")

# contoh penggunaan
kelas_1 = Kelas("XII-A", "IPA")
siswa_1 = Siswa("Andi", "1234", kelas_1)
kelas_1.tambah_siswa(siswa_1)

siswa_2 = Siswa("Budi", "5678", kelas_1)
kelas_1.tambah_siswa(siswa_2)

print("Daftar Siswa:")
for siswa in kelas_1.daftar_siswa:
    siswa.tampilkan_info()
