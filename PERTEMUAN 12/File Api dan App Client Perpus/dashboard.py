import tkinter as tk
from tkinter import Menu
from FrmAnggota import *
from FrmBuku import *
from FrmPeminjaman import *
from FrmPengembalian import *
from tkinter import *



# root window
root = tk.Tk()
root.title('Aplikasi Perpustakaan')
#root.attributes('-fullscreen', True)
root.geometry("1366x670")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu


file_menu.add_command(
    label='Keluar', command=root.destroy
)

app_menu.add_command(
    label='App Pengembalian', command= lambda: new_window("Data Peminjaman", FrmPengembalian )
)
app_menu.add_command(
    label='App Peminjaman', command= lambda: new_window("Data Peminjaman", FrmPeminjaman )
)
app_menu.add_command(
    label='App Buku', command= lambda: new_window("Data Buku", FrmBuku )
)

data_menu.add_command(
    label='Data Anggota', command= lambda: new_window("Daftar Anggota", FrmAnggota)
)

gambar = PhotoImage(file="C:/xampp/htdocs/perpusputri/perpus.png") 
w = Label(root, image=gambar).pack(side="top")



def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="Aplikasi", menu=app_menu
)
menubar.add_cascade(
    label="Data", menu=data_menu
)

menubar.add_cascade(
    label="LOGOUT", menu=file_menu
)
root.mainloop()