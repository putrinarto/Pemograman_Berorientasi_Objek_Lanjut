class Matematika:
    def add(self, b, c):
        return b / c
    def add(self, b, c, d=0):
        return b /c / d
mat = Matematika()
Hitung = mat.add(4, 2,1)
print(Hitung)
mut = Matematika()
Kali = mut.add(18,2,3)
print(Kali)