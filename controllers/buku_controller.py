# Amandita Isyana_017
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_views import BukuView

class BukuController:
    def __init__logout(self):
        # Menginisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()
        
        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_delete.configure(command=self.delete_data)

        self.view.tabel.bind("<<TreeviewSelect>>", self.select_item)
       
        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        # Mengambil data dari Model (Database)
        data_buku = self.model.get_all_buku()
        
        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku["id_buku"], buku["judul"], buku["penulis"], buku["tahun_terbit"]))

       #📍 POSISI 2: TAMBAHKAN KETIGA FUNGSI INI DI SINI 
       #(Di bawah muat_data_tabel dan sebelum simpan_data atau run)
    def select_item(self, event):
        selected_item = self.view.tabel.focus()
        if selected_item:
            values = self.view.tabel.item(selected_item, 'values')
            if values:
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, values[1])
                self.view.entry_Penulis.delete(0, 'end')
                self.view.entry_Penulis.insert(0, values[2])
                self.view.entry_tahun.delete(0, 'end')
                self.view.entry_tahun.insert(0, values[3])

    def update_data(self):
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data buku pada tabel yang ingin diperbarui!")
            return
            
        values = self.view.tabel.item(selected_item, 'values')
        id_buku = values[0]
        
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_Penulis.get()
        tahun = self.view.entry_tahun.get()
        
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        berhasil = self.model.update_buku(id_buku, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_Penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")
# update
    def update_data(self):
        if self.user_role == "anggota":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

    def delete_data(self):
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data buku pada tabel yang ingin dihapus!")
            return
                        
        values = self.view.tabel.item(selected_item, 'values')
        id_buku = values[0]  # Mengambil nilai ID dari kolom pertama
        
        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            # Memanggil fungsi dalate dari model
            berhasil = self.model.delete_buku(id_buku)
            
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_Penulis.delete(0, 'end')  
                self.view.entry_tahun.delete(0, 'end')
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")
# Delete
    def delete_data(self):
        if self.user_role == "anggota":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

    def simpan_data(self):
        # Mengambil teks dari inputan di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_Penulis.get()
        tahun = self.view.entry_tahun.get()
        
        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)
        
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            # Bersihkan form input
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_Penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            # Muat ulang tabel agar data baru muncul
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_views import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()
        self.view.btn_logout.configure(command=self.logout)

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding tombol simpan
        self.view.btn_simpan.configure(command=self.simpan_data)

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_Penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

# Tugas 2
        if self.user_role == "anggota":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_Penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")
            
            # Tambahan untuk mengunci tombol Update dan Delete jika ada di view
        if hasattr(self.view, 'btn_update'):
                self.view.btn_update.configure(state="disabled")
        if hasattr(self.view, 'btn_hapus'):
                self.view.btn_hapus.configure(state="disabled")
        
            # Mengunci tombol Update dan Delete khusus untuk anggota
        if hasattr(self.view, 'btn_update'):
            self.view.btn_update.configure(state="disabled")
        if hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(state="disabled")

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")
# Tugas
# Hubungkan tombol logout ke fungsi logout
        if hasattr(self.view, 'btn_logout'):
            self.view.btn_logout.configure(command=self.logout)

    def logout(self):
        from controllers.auth_controller import AuthController
        if messagebox.askyesno("Konfirmasi Logout", "Apakah Anda yakin ingin keluar dari sistem?"):
            self.view.destroy()  # Menutup jendela saat ini secara tuntas
            app_auth = AuthController()
            app_auth.run()
   
    def run(self):
        self.view.mainloop()

   