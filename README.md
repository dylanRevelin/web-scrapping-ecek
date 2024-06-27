# Kelompok 6

Penjelasan terkait program yang dikembangkan, cara kerja program, pembagian tugas per masing-masing anggota, library yang perlu diinstal, serta dokumen referensi

### 1. Deskripsi Program

Aplikasi yang kami kembangkan adalah sebuah aplikasi web scraping yang bertujuan untuk mengumpulkan data produk dari berbagai situs e-commerce. Aplikasi ini dibangun menggunakan Flask, sebuah framework web berbasis Python, untuk memberikan antarmuka pengguna yang sederhana dan intuitif. Fitur utama dari aplikasi ini mencakup:

1. Pengumpulan Data Produk:
    Pengguna dapat memasukkan nama produk yang ingin mereka cari serta jumlah halaman yang akan discan. Aplikasi kemudian akan melakukan scraping data dari berbagai situs e-commerce, mengumpulkan informasi seperti nama produk, harga, rating, dan website asal.

2. Analisis Data:
    Setelah data dikumpulkan, aplikasi akan melakukan analisis untuk menghitung statistik penting seperti harga rata-rata, harga median, rating rata-rata, dan rating median dari produk yang ditemukan. Informasi tentang harga tertinggi dan terendah juga disertakan.

3. Penyajian Hasil:
    Hasil scraping dan analisis disajikan dalam bentuk tabel yang terorganisir, dengan produk diurutkan berdasarkan harga. Pengguna dapat melihat informasi detail mengenai setiap produk yang ditemukan.

4. Fitur Unduh:
    Aplikasi menyediakan opsi untuk mengunduh hasil scraping dalam format Excel. File Excel ini mencakup semua data produk yang ditemukan serta statistik yang dihitung, sehingga pengguna dapat menganalisis data lebih lanjut atau menggunakannya untuk keperluan lain.

5. Batasan Jumlah Data:
    Untuk memastikan performa yang optimal dan penyajian data yang mudah dibaca, aplikasi membatasi jumlah produk yang ditampilkan hingga 100 produk teratas berdasarkan harga.

### 2. Teknologi yang Digunakan
- Flask: Digunakan sebagai framework utama untuk pengembangan aplikasi web.
- Pandas: Digunakan untuk manipulasi dan analisis data.
- Jinja2: Template engine yang digunakan oleh Flask untuk merender HTML dengan data dinamis.
- Bootstrap: Digunakan untuk membuat antarmuka pengguna yang responsif dan menarik.
- Selenium: Digunakan untuk melakukan web scraping.

### 3. Cara Kerja Aplikasi

1. Input Pengguna:
    Pengguna memasukkan nama produk dan jumlah halaman yang ingin discan melalui antarmuka web.

2. Proses Scraping:
    Aplikasi mengirimkan permintaan HTTP ke situs-situs e-commerce yang relevan dan mengunduh halaman-halaman produk yang sesuai dengan kriteria pencarian.

3. Ekstraksi Data:
    Data produk diekstraksi dari halaman-halaman yang diunduh menggunakan BeautifulSoup, lalu disimpan dalam format yang terstruktur.

4. Analisis Data:
    Data produk yang terkumpul dianalisis menggunakan Pandas untuk menghitung statistik penting seperti harga rata-rata dan rating rata-rata.

5. Penyajian dan Unduhan:
    Hasil analisis ditampilkan di halaman web dalam bentuk tabel. Pengguna juga dapat mengunduh hasil analisis dalam format Excel untuk penggunaan lebih lanjut.

Dengan aplikasi ini, pengguna dapat dengan mudah mengumpulkan dan menganalisis data produk dari berbagai sumber, membantu mereka dalam membuat keputusan pembelian yang lebih baik dan memahami tren pasar.
