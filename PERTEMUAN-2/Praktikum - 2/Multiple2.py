class Manusia:
    def __init__(self, nama ,umur):
        self.nama = nama
        self.umur = umur
        
class Penari:
    def __init__(self, style):
        self.style = style
        
class Murid (Manusia, Penari):
    def __init__(self, nama, umur, style):
        Manusia.__init__(self, nama, umur)
        Penari.__init__(self,style)
        
Deku = Murid( 'Deku', 20, 'Hiphop')
print (Deku.nama)
print (Deku.umur)
print (Deku.style)       