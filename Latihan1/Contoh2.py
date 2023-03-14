class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNIM: {self.npm}")
mahasiswaB = Mahasiswa("Putri", "210511068")
mahasiswaB.info()