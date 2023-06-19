import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__kode_peminjaman = None
        self.__tanggal_peminjaman = None
        self.__tanggal_kembali = None
        self.__kode_buku = None
        self.__kode_angota = None
        self.__url = "http://f0832633.xsph.ru/perpus/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_peminjaman(self):
        return self.__kode_peminjaman
        
    @kode_peminjaman.setter
    def kode_peminjaman(self, value):
        self.__kode_peminjaman = value
    @property
    def tanggal_peminjaman(self):
        return self.__tanggal_peminjaman
        
    @tanggal_peminjaman.setter
    def tanggal_peminjaman(self, value):
        self.__tanggal_peminjaman = value
    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali
        
    @tanggal_kembali.setter
    def tanggal_kembali(self, value):
        self.__tanggal_kembali = value
    @property
    def kode_buku(self):
        return self.__kode_buku
        
    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value
    @property
    def kode_angota(self):
        return self.__kode_angota
        
    @kode_angota.setter
    def kode_angota(self, value):
        self.__kode_angota = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_peminjaman(self, kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_peminjaman']
            self.__kode_peminjaman = item['kode_peminjaman']
            self.__tanggal_peminjaman = item['tanggal_peminjaman']
            self.__tanggal_kembali = item['tanggal_kembali']
            self.__kode_buku = item['kode_buku']
            self.__kode_angota = item['kode_angota']
        return data
    def simpan(self):
        payload = {
            "kode_peminjaman":self.__kode_peminjaman,
            "tanggal_peminjaman":self.__tanggal_peminjaman,
            "tanggal_kembali":self.__tanggal_kembali,
            "kode_buku":self.__kode_buku,
            "kode_angota":self.__kode_angota
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_peminjaman(self, kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        payload = {
            "kode_peminjaman":self.__kode_peminjaman,
            "tanggal_peminjaman":self.__tanggal_peminjaman,
            "tanggal_kembali":self.__tanggal_kembali,
            "kode_buku":self.__kode_buku,
            "kode_angota":self.__kode_angota
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_peminjaman(self,kode_peminjaman):
        url = self.__url+"?kode_peminjaman="+kode_peminjaman
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text