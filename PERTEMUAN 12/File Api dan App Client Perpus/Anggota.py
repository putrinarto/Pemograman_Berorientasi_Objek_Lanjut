import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__kode_anggota = None
        self.__nama_anggota = None
        self.__jk_anggota = None
        self.__prodi = None
        self.__url = "http://localhost/perpusputri/anggota_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    @property
    def nama_anggota(self):
        return self.__nama_anggota
        
    @nama_anggota.setter
    def nama_anggota(self, value):
        self.__nama_anggota = value
    @property
    def jk_anggota(self):
        return self.__jk_anggota
        
    @jk_anggota.setter
    def jk_anggota(self, value):
        self.__jk_anggota = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_anggota(self, kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_anggota']
            self.__kode_anggota = item['kode_anggota']
            self.__nama_anggota = item['nama_anggota']
            self.__jk_anggota = item['jk_anggota']
            self.__prodi = item['prodi']
        return data
    def simpan(self):
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nama_anggota":self.__nama_anggota,
            "jk_anggota":self.__jk_anggota,
            "prodi":self.__prodi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_anggota(self, kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nama_anggota":self.__nama_anggota,
            "jk_anggota":self.__jk_anggota,
            "prodi":self.__prodi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_anggota(self,kode_anggota):
        url = self.__url+"?kode_anggota="+kode_anggota
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text