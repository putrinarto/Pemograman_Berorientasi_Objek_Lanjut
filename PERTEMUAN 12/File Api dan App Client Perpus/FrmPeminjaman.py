import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1000x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_PEMINJAMAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_PEMINJAMAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_KEMBALI:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_BUKU:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_ANGOTA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_peminjaman = Entry(mainFrame) 
        self.txtKode_peminjaman.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_peminjaman.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTanggal_peminjaman = Entry(mainFrame) 
        self.txtTanggal_peminjaman.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTanggal_kembali = Entry(mainFrame) 
        self.txtTanggal_kembali.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_buku = Entry(mainFrame) 
        self.txtKode_buku.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_angota = Entry(mainFrame) 
        self.txtKode_angota.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_peminjaman','kode_peminjaman','tanggal_peminjaman','tanggal_kembali','kode_buku','kode_angota')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_peminjaman', text='ID_PEMINJAMAN')
        self.tree.column('id_peminjaman', width="100")
        self.tree.heading('kode_peminjaman', text='KODE_PEMINJAMAN')
        self.tree.column('kode_peminjaman', width="200")
        self.tree.heading('tanggal_peminjaman', text='TANGGAL_PEMINJAMAN')
        self.tree.column('tanggal_peminjaman', width="200")
        self.tree.heading('tanggal_kembali', text='TANGGAL_KEMBALI')
        self.tree.column('tanggal_kembali', width="200")
        self.tree.heading('kode_buku', text='KODE_BUKU')
        self.tree.column('kode_buku', width="100")
        self.tree.heading('kode_angota', text='KODE_ANGOTA')
        self.tree.column('kode_angota', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_peminjaman.delete(0,END)
        self.txtKode_peminjaman.insert(END,"")
        self.txtTanggal_peminjaman.delete(0,END)
        self.txtTanggal_peminjaman.insert(END,"")
        self.txtTanggal_kembali.delete(0,END)
        self.txtTanggal_kembali.insert(END,"")
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,"")
        self.txtKode_angota.delete(0,END)
        self.txtKode_angota.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_peminjaman"],d["kode_peminjaman"],d["tanggal_peminjaman"],d["tanggal_kembali"],d["kode_buku"],d["kode_angota"]))
    def onCari(self, event=None):
        kode_peminjaman = self.txtKode_peminjaman.get()
        obj = Peminjaman()
        a = obj.get_by_kode_peminjaman(kode_peminjaman)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_peminjaman = self.txtKode_peminjaman.get()
        obj = Peminjaman()
        res = obj.get_by_kode_peminjaman(kode_peminjaman)
        self.txtKode_peminjaman.delete(0,END)
        self.txtKode_peminjaman.insert(END,obj.kode_peminjaman)
        self.txtTanggal_peminjaman.delete(0,END)
        self.txtTanggal_peminjaman.insert(END,obj.tanggal_peminjaman)
        self.txtTanggal_kembali.delete(0,END)
        self.txtTanggal_kembali.insert(END,obj.tanggal_kembali)
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,obj.kode_buku)
        self.txtKode_angota.delete(0,END)
        self.txtKode_angota.insert(END,obj.kode_angota)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_peminjaman = self.txtKode_peminjaman.get()
        tanggal_peminjaman = self.txtTanggal_peminjaman.get()
        tanggal_kembali = self.txtTanggal_kembali.get()
        kode_buku = self.txtKode_buku.get()
        kode_angota = self.txtKode_angota.get()
        # create new Object
        obj = Peminjaman()
        obj.kode_peminjaman = kode_peminjaman
        obj.tanggal_peminjaman = tanggal_peminjaman
        obj.tanggal_kembali = tanggal_kembali
        obj.kode_buku = kode_buku
        obj.kode_angota = kode_angota
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_peminjaman(kode_peminjaman)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_peminjaman = self.txtKode_peminjaman.get()
        obj = Peminjaman()
        obj.kode_peminjaman = kode_peminjaman
        if(self.ditemukan==True):
            res = obj.delete_by_kode_peminjaman(kode_peminjaman)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()