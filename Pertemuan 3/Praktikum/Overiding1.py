class Matematika:
    def add(self, p, u):
        return p + u
    def add(self, p, u, t=0):
        return p + u + t
mat = Matematika()
Hitung = mat.add(6, 3, 3)
print(Hitung)
mut = Matematika()
Tambah = mut.add(6,3)
print(Tambah)