class Tenaga : 
    def setTenaga (self,tenaga):
        self.tenaga = tenaga
        
    def showTenaga(self):
        print(self.tenaga)

class Kelompok :
    def setKelompok(self,kelompok):
        self.kelompok = kelompok
        
    def showKelompok (self):
        print (self.kelompok)
        
class Pahlawan (Tenaga,Kelompok):
    def __init__(self,name,health):
        self.name = name 
        self.health = health

Deku = Pahlawan ('Deku', 200)
Deku.setKelompok('Pro')
Deku.setTenaga('Super')

Deku.showKelompok()
Deku.showTenaga()    