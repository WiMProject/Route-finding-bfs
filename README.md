# Pencarian Jalur Antar TPS tercepat dengan Algoritma Greedy dan A*

Proyek ini adalah sebuah aplikasi web yang memungkinkan pengguna untuk melakukan pencarian jalur tps tercepat dari posisi awal truk dan tujuan truk yang ingin dituju menggunakan algoritma Greedy dan A*. Aplikasi ini dibangun menggunakan python, html, serta menggunakan boostrap, untuk module python yang dipakai adalah Flask dan matplotlib untuk memvisualisasikan hasil pencarian jalur pada sebuah graf, aplikasi ini sangat berguna untuk truk-truk sampah yang ada di kota Bandung untuk mencari tps yang penuh untuk di ambil ke tps akhir.

## Fitur

- Memilih algoritma pencarian jalur (Greedy atau A*)
- Menentukan posisi awal dan tujuan
- Menampilkan jalur yang diikuti dalam pencarian
- Visualisasi graf yang menunjukkan jalur yang diikuti

## Prasyarat

- Python 3.10 atau versi terbaru
- Pip (Python package installer)
- Flask
- NetworkX
- Matplotlib

## Instalasi

1. Clone repositori ini
   bash
   git clone https://github.com/WiMProject/Route-finding-bfs.git
   cd Route-finding-bfs
2. Buat virtual environment dan aktifkan
   python -m venv env
   source env/bin/activate   
   # Pada Windows gunakan `env\Scripts\activate`
3. Instal dependensi yang diperlukan
   pip install -r requirements.txt

## Menjalankan Aplikasi

1. python app.py
   atau jika memakai code editor bisa klik saja file app.py dan klik tombol run untuk menjalankan local server
2. lalu akan keluar link local akses http://127.0.0.1:5000
3. klik link nya dan nanti akan diarahkan ke browser

## Cara Penggunaan

1. Masukkan nomor posisi awal dan nomor tujuan.
2. Pilih algoritma pencarian jalur (Greedy atau A*).
3. Klik tombol "Cari Jalur".
4. Hasil pencarian jalur akan ditampilkan bersama dengan visualisasi graf.

## Struktur Proyek
- app.py: File utama untuk menjalankan aplikasi Flask dan mengatur routing.
- greedy.py: Mengandung implementasi algoritma Greedy dan graf terkait.
- astar.py: Mengandung implementasi algoritma A* dan graf terkait.
- templates/index.html: Template HTML untuk tampilan web.
- static/: Folder untuk menyimpan file statis seperti gambar hasil visualisasi graf.

## Kontak

- Gmail : wildanmiladji53@gmail.com
- WhatsApp : 087819471008
- Telegram : @WildanM53
