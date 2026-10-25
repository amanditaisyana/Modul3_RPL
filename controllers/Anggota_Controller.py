import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_views import AnggotaView  # Sesuaikan dengan nama view anggota Anda

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()
        
        # Binding tombol-tombol di View Anggota
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.delete_data)
        
        self.view.tabel.bind("<<TreeviewSelect>>", self.select_item)
        
        # Muat data tabel saat pertama kali dibuka
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        data_anggota = self.model.get_all_anggota() # Sesuaikan fungsi model Anda
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota["id_anggota"], anggota["nama"], anggota["alamat"]))

    def select_item(self, event):
        selected_item = self.view.tabel.focus()
        if selected_item:
            values = self.view.tabel.item(selected_item, 'values')
            if values:
                self.view.entry_nama.delete(0, 'end')
                self.view.entry_nama.insert(0, values[1])
                self.view.entry_alamat.delete(0, 'end')
                self.view.entry_alamat.insert(0, values[2])

    def update_data(self):
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data anggota yang ingin diperbarui!")
            return
            
        values = self.view.tabel.item(selected_item, 'values')
        id_anggota = values[0]
        
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        berhasil = self.model.update_anggota(id_anggota, nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def delete_data(self):
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data anggota yang ingin dihapus!")
            return
                    
        values = self.view.tabel.item(selected_item, 'values')
        id_anggota = values[0]
    
        konfirmasi = messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?")
        if konfirmasi:
            berhasil = self.model.delete_anggota(id_anggota)
            if berhasil:
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        berhasil = self.model.create_anggota(nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")
            
    def run(self):
        self.view.mainloop()
