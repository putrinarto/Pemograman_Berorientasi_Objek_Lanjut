data_mahasiswa = [
    {"nim": 12345, "nama": "Putri", "jurusan": "Informatika"},
    {"nim": 67890, "nama": "Auris", "jurusan": "Sistem Informasi"}
]

for mahasiswa in data_mahasiswa:
    try:
        nilai = mahasiswa["nilai"]
    except KeyError:
        print("Mahasiswa", mahasiswa["nim"], "tidak memiliki nilai!")