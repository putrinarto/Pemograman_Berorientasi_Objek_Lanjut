class Mobil:
    def __init__(self, nama, tahun):
        self.nama = nama
        self.tahun = tahun
mobil = Mobil("Pajero", 2003)
try:
    print(mobil.umur)
except AttributeError:
    print("Error: Atribut 'umur' tidak ada pada objek Mobil!")
