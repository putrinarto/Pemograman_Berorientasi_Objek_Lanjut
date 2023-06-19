import requests
import json
class Pengembalian:
    def __init__(self):
        self.__id=None
        self.__kode_pengembalian = None
        self.__taggal_pengembalian = None
        self.__denda = None
        self.__kode_buku = None
        self.__kode_anggota = None
        self.__url = "http://localhost/perpusputri/pengembalian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_pengembalian(self):
        return self.__kode_pengembalian
        
    @kode_pengembalian.setter
    def kode_pengembalian(self, value):
        self.__kode_pengembalian = value
    @property
    def taggal_pengembalian(self):
        return self.__taggal_pengembalian
        
    @taggal_pengembalian.setter
    def taggal_pengembalian(self, value):
        self.__taggal_pengembalian = value
    @property
    def denda(self):
        return self.__denda
        
    @denda.setter
    def denda(self, value):
        self.__denda = value
    @property
    def kode_buku(self):
        return self.__kode_buku
        
    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_pengembalian(self, kode_pengembalian):
        url = self.__url+"?kode_pengembalian="+kode_pengembalian
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pengembalian']
            self.__kode_pengembalian = item['kode_pengembalian']
            self.__taggal_pengembalian = item['taggal_pengembalian']
            self.__denda = item['denda']
            self.__kode_buku = item['kode_buku']
            self.__kode_anggota = item['kode_anggota']
        return data
    def simpan(self):
        payload = {
            "kode_pengembalian":self.__kode_pengembalian,
            "taggal_pengembalian":self.__taggal_pengembalian,
            "denda":self.__denda,
            "kode_buku":self.__kode_buku,
            "kode_anggota":self.__kode_anggota
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_pengembalian(self, kode_pengembalian):
        url = self.__url+"?kode_pengembalian="+kode_pengembalian
        payload = {
            "kode_pengembalian":self.__kode_pengembalian,
            "taggal_pengembalian":self.__taggal_pengembalian,
            "denda":self.__denda,
            "kode_buku":self.__kode_buku,
            "kode_anggota":self.__kode_anggota
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_pengembalian(self,kode_pengembalian):
        url = self.__url+"?kode_pengembalian="+kode_pengembalian
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
