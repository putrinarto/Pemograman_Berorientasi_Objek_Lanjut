class Orangtua:
    def __init__(self, rambut, umur):
        self.rambut = rambut
        self.umur = umur
    def jenisRambut(self):

        print(self.rambut, "Keriting")

class Anak(Orangtua):
    def __init__(self, rambut, umur, warnaMata):
        super().__init__(rambut, umur)
        self.warnaMata = warnaMata
        
    def JenisKelamin(self):
        print("Laki Laki")
      
kucingA = Anak("Aldi", 12, "biru")
kucingA.jenisRambut() 
kucingA.JenisKelamin()