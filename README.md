# Kelompok 6

Penjelasan terkait program yang dikembangkan, cara kerja program, pembagian tugas per masing-masing anggota, library yang perlu diinstal, video presentasi serta dokumen referensi

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

### 4. Pembagian Tugas

#### 1. Michael - 221110659 : Penanggung Jawab Scraping dari Lazada

Tugas Utama: Melakukan scraping data produk dari situs e-commerce Lazada.

Detail Pekerjaan:
- Mengembangkan skrip scraping yang mampu mengumpulkan informasi produk seperti nama, harga, rating, dan website asal dari Lazada.
- Menjaga agar skrip scraping tetap up-to-date dengan perubahan struktur situs web Lazada.
- Menguji dan memastikan bahwa data yang di-scrape akurat dan lengkap.
  
#### 2. Dylan Revelin - 221110096 : Penanggung Jawab Scraping dari Tokopedia dan Bukalapakserta Pengembangan BackEnd

Tugas Utama: Melakukan scraping data produk dari situs e-commerce Tokopedia dan Bukalapak serta mengembangkan backend aplikasi.

Detail Pekerjaan:
- Mengembangkan skrip scraping untuk mengumpulkan informasi produk dari Tokopedia dan Bukalapak.
- Mengelola backend aplikasi menggunakan Flask, termasuk mengatur rute dan fungsi utama di dalam app.py.
- Mengintegrasikan hasil scraping dengan backend untuk memastikan data dapat diakses dan diolah dengan mudah.
  
#### 3. Veilind Maynius - 221111085 : Penanggung Jawab Analisis Data dan Pengembangan Tampilan

Tugas Utama: Menganalisis data yang telah di-scrape dan mengembangkan tampilan antarmuka pengguna.

Detail Pekerjaan:
- Menulis modul analysis.py untuk menghitung statistik penting seperti harga rata-rata, median harga, rata-rata rating, dan median rating dari data yang di-scrape.
- Mengembangkan template HTML menggunakan Jinja2 dan Bootstrap untuk menampilkan hasil scraping dan analisis data dengan cara yang menarik dan mudah dipahami.
- Memastikan antarmuka pengguna responsif dan user-friendly

#### 4. Vincent - 221110485 : Penanggung Jawab Pengujian dan Analisa Bug serta Data

Tugas Utama: Menjalankan kode, mengidentifikasi, dan memperbaiki bug, serta melakukan analisis data hasil scraping.

Detail Pekerjaan:
- Menjalankan keseluruhan kode aplikasi untuk memastikan semuanya berjalan dengan lancar.
- Mengidentifikasi dan memperbaiki bug yang ditemukan selama pengujian.
- Melakukan analisis mendalam terhadap data yang dihasilkan, memastikan data tersebut siap digunakan untuk tujuan lebih lanjut, seperti pelaporan atau penelitian.

### 5. Library yang perlu diinstall

1. Flask

Fungsi: Framework web mikro yang digunakan untuk mengembangkan aplikasi web. Flask memudahkan dalam pengelolaan rute, render template, dan menangani permintaan HTTP.

Instalasi: pip install Flask

2. Selenium

Fungsi: Pustaka yang digunakan untuk otomatisasi browser. Selenium digunakan untuk melakukan scraping data dari situs web dengan mensimulasikan interaksi pengguna.

Instalasi: pip install selenium

3. Openpyxl

Fungsi: Pustaka untuk membaca dan menulis file Excel (xlsx). Digunakan untuk menyimpan hasil scraping ke dalam file Excel.

Instalasi: pip install openpyxl

4. Pandas

Fungsi: Pustaka untuk manipulasi dan analisis data. Digunakan untuk memproses dan menganalisis data yang telah di-scrape.

Instalasi: pip install pandas

5. Xlsxwriter

Fungsi: Pustaka untuk menulis file Excel dengan format yang lebih kompleks. Digunakan untuk menambahkan statistik ke dalam file Excel.

Instalasi: pip install XlsxWriter

Untuk menjalankan program ini, kita juga perlu meng-install driver Chrome yang sesuai dengan versi browser Chrome yang kita gunakan.

Link untuk menginstall Chromedriver : https://googlechromelabs.github.io/chrome-for-testing/#stable

Note : Pilih bagian Stable lalu install sesuai sistem operasi yang diinginkan

### 6. Video Presentasi 
https://mikroskilacid-my.sharepoint.com/:v:/g/personal/221110659_students_mikroskil_ac_id/EYqdTYHIabFKrOAYQQH8XDgBjKBLqyVGu06MPH2HaO1Gtw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=61EuXU


### 7. Referensi Pendukung

**1. Website Dokumentasi**
- https://azcv.readthedocs.io/en/latest/
- https://github.com/SeleniumHQ/seleniumhq.github.io

**2. Jurnal**
Khder, M. A. (2021). Web scraping or web crawling: State of art, techniques, approaches and application. International Journal of Advances in Soft Computing & Its Applications, 13(3). http://www.i-csrs.org/Volumes/ijasca/2021.3.11.pdf

Rinanda, P. D. (2024, January). Implementation of PNN, ANN And K-NN Algorithms on Indonesian Marketplace Reviews on Google Play Store. In 2024 ASU International Conference in Emerging Technologies for Sustainability and Intelligent Systems (ICETSIS) (pp. 1070-1074). IEEE. http://repository.uin-suska.ac.id/78865/1/PALING%20FIX%20LAPORAN%20TA%20PUJI%20.pdf

RITA, A. (2020). ANALISIS SENTIMEN MENGGUNAKAN ALGORITMA NAÏVE BAYES TERHADAP KOMENTAR APLIKASI TOKOPEDIA (Doctoral dissertation, Nusa Putra University). http://repository.nusaputra.ac.id/id/eprint/93/1/RITA%20APRIANI%20_Si20.pdf

**3. Youtube**
- https://youtu.be/NB8OceGZGjA?si=jyCwOVTODrYDR0fR
- https://youtu.be/RKeJPXrbT8w?si=WpQ7OPvtuYbkwhBI
