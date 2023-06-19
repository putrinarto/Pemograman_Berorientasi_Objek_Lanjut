import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pengembalian import *
class FrmPengembalian:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("800x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_PENGEMBALIAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAGGAL_PENGEMBALIAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='DENDA:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_BUKU:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_ANGGOTA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_pengembalian = Entry(mainFrame) 
        self.txtKode_pengembalian.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_pengembalian.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTaggal_pengembalian = Entry(mainFrame) 
        self.txtTaggal_pengembalian.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtDenda = Entry(mainFrame) 
        self.txtDenda.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_buku = Entry(mainFrame) 
        self.txtKode_buku.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_pengembalian','kode_pengembalian','taggal_pengembalian','denda','kode_buku','kode_anggota')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_pengembalian', text='ID_PENGEMBALIAN')
        self.tree.column('id_pengembalian', width="180")
        self.tree.heading('kode_pengembalian', text='KODE_PENGEMBALIAN')
        self.tree.column('kode_pengembalian', width="100")
        self.tree.heading('taggal_pengembalian', text='TAGGAL_PENGEMBALIAN')
        self.tree.column('taggal_pengembalian', width="200")
        self.tree.heading('denda', text='DENDA')
        self.tree.column('denda', width="100")
        self.tree.heading('kode_buku', text='KODE_BUKU')
        self.tree.column('kode_buku', width="100")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_pengembalian.delete(0,END)
        self.txtKode_pengembalian.insert(END,"")
        self.txtTaggal_pengembalian.delete(0,END)
        self.txtTaggal_pengembalian.insert(END,"")
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,"")
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,"")
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pengembalian
        obj = Pengembalian()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_pengembalian"],d["kode_pengembalian"],d["taggal_pengembalian"],d["denda"],d["kode_buku"],d["kode_anggota"]))
    def onCari(self, event=None):
        kode_pengembalian = self.txtKode_pengembalian.get()
        obj = Pengembalian()
        a = obj.get_by_kode_pengembalian(kode_pengembalian)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_pengembalian = self.txtKode_pengembalian.get()
        obj = Pengembalian()
        res = obj.get_by_kode_pengembalian(kode_pengembalian)
        self.txtKode_pengembalian.delete(0,END)
        self.txtKode_pengembalian.insert(END,obj.kode_pengembalian)
        self.txtTaggal_pengembalian.delete(0,END)
        self.txtTaggal_pengembalian.insert(END,obj.taggal_pengembalian)
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,obj.denda)
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,obj.kode_buku)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_pengembalian = self.txtKode_pengembalian.get()
        taggal_pengembalian = self.txtTaggal_pengembalian.get()
        denda = self.txtDenda.get()
        kode_buku = self.txtKode_buku.get()
        kode_anggota = self.txtKode_anggota.get()
        # create new Object
        obj = Pengembalian()
        obj.kode_pengembalian = kode_pengembalian
        obj.taggal_pengembalian = taggal_pengembalian
        obj.denda = denda
        obj.kode_buku = kode_buku
        obj.kode_anggota = kode_anggota
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_pengembalian(kode_pengembalian)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_pengembalian = self.txtKode_pengembalian.get()
        obj = Pengembalian()
        obj.kode_pengembalian = kode_pengembalian
        if(self.ditemukan==True):
            res = obj.delete_by_kode_pengembalian(kode_pengembalian)
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
    aplikasi = FrmPengembalian(root2, "Aplikasi Data Pengembalian")
    root2.mainloop()