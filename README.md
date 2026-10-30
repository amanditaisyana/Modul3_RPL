# Sistem Informasi Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Informasi Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk membantu pengelolaan data perpustakaan. Aplikasi ini menerapkan arsitektur Model-View-Controller (MVC) dan menggunakan database MySQL untuk menyimpan data. 
Fitur aplikasi meliputi:
* Login dan autentikasi pengguna.
* Registrasi pengguna.
* Pengelolaan data buku.
* Pengelolaan data anggota.
* Hak akses berdasarkan role pengguna.

---

## 2. Struktur Direktori MVC

```text
MODUL3_RPL/
│
├── models/
│   ├── buku_model.py
│   ├── anggota_model.py
│   └── user_model.py
│
├── views/
│   ├── buku_view.py
│   ├── anggota_view.py
│   └── login_view.py
│
├── controllers/
│   ├── buku_controller.py
│   ├── anggota_controller.py
│   └── auth_controller.py
│
├── tests/
│   ├── test_buku.py
│   └── test_auth.py
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── config/
│   └── database.py
│
├── main.py
├── main_auth.py
├── requirements.txt
└── README.md

## Cara Menjalankan Aplikasi
1. Pastikan virtual environment aktif.
2. Jalankan perintah: `python main.py`

## Cara pengjuan 
1. pytest -v 