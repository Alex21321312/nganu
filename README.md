# Panduan Dalam Menggunakan aplikasi Django dan aktivasi project_1 🚀

Repositori ini berisi panduan langkah demi langkah untuk menginisiasi dan membuat aplikasi web menggunakan framework **Django** dari nol.

## 📋 Persyaratan Dasar (Prerequisites)

Sebelum dimulai, pastikan sistem Anda sudah terinstal:
* **Python** (versi 3.x atau terbaru). Bisa diunduh di [python.org](https://www.python.org/).
* **Pip** (Package installer untuk Python, biasanya sudah sepaket dengan instalasi Python).
* **SQL Server 2012/2025** (Database default dari project_1).

---

## 🛠️ Langkah-langkah Pembuatan

### 1. Membuat dan Mengaktifkan Virtual Environment
Virtual environment sangat direkomendasikan agar *library* (dependensi) proyek ini terisolasi dan tidak bentrok dengan proyek Python lainnya di komputer Anda.

Buka terminal/command prompt, arahkan ke folder tempat Anda ingin menyimpan proyek, dan jalankan perintah:

```bash
# Membuat virtual environment dengan nama "myworld"
python -m venv myworld
```

Aktifkan virtual environment

```bash
# Windows
myworld\Scripts\activate

# Linux/macOS
source myworld/bin/activate
```

Setelah virtual environment aktif, instal Django menggunakan pip:

```bash
python -m pip install django
```

### 2. Membuat aplikasi Django
Proyek adalah fondasi utama yang akan menampung konfigurasi aplikasi Anda. Buat proyek baru dengan nama project_1 (Anda bebas mengganti namanya, project_1 ini hanya digunakan agar folder project_1 di dalam GitHub sesuai dengan yang akan anda aktifkan):

```bash
django-admin startproject project_1 .
```

Catatan: Tanda titik . di akhir perintah berguna agar Django membuat file proyek di folder saat ini tanpa membuat sub-folder baru yang bertumpuk.

Setelah project dibuat, copy seluruh folder project_1 di GitHub dan ganti file bawaan yang telah di setup saat pembuatan project.

Lalu, navigasi ke folder yang terdapat file manage.py di dalamnya dan ketik command berikut:

```bash
python manage.py runserver
# Jika suatu projek ingin diakses dari device lain, lakukan
python manage.py runserver 0.0.0.0:8000
```

Setelah itu, buka browser dan ketik 127.0.0.1:8000 untuk mengaktivasi projek Django

Sebelum menyambungkan django dengan python, unduh library mssql agar terjadi koneksi antara sql server dan python

```bash
python -m pip install mssql
```

Lalu, buka settings.py dan ubah kolom DATABASE menjadi database yang anda miliki:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'nama_database',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'nama_server',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    },

    'django_builtin': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    },
}
