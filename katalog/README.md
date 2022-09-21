Amanda Nadhifah Zahra Andini

2106637246

PBP-A

Link hasil deploy: https://pbp-tugas-deploy-amanda.herokuapp.com/

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![](https://github.com/amandanadhifah23/Tugas2PBP/blob/main/Bagan/Bagan%20README.png)

Kaitan antara urls.py, views.py, models.py, dan berkas html:  
User memberikan request yang akan diterima oleh si url dan mengekstrak argumen. Url akan melakukan routing ke views yang sesuai. Jika views sudah menerima, voews mengakses httml template dan mengambil data melalui models.py untuk mengakses database. Data yang diperolah tersebut akan membentuj halaman html dan akan dikirim kepada user sebagai respons.

## Jelaskan kenapa menggunakan virtual environment? 
Virtual environment penting untuk memberikan batasan dan lingkungan yang terisolasi agar project berjalan sesuai versi yang dibutuhkan. Virtual environment dapat dapat mencegah terjadinya issue dependency saat ada update atau perbedaan versi. Project juga tidak akan berubah pada storage local komputer kita.

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Bisa saja membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Akan tetapi, project yang sedang dijalankan memiliki risiko tinggi menampilkan hasil yang berbeda-beda. Jika tidak ada virtual environment, tidak ada ruang terpisah untuk sebuah proyek dan dapat berdependensi dengan proyek lainnya.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas
### 1. Membuat sebuah fungsi pada views.py
Pada folder katalog yang disediakan template, pemanggilan fungsi show_katalog akan melakukan render sebuah halaman HTML. Fungsi show_katalog pada views.py akan memanggil fungsi query ke model database dan menyimpan hasil query tersebut. Penambahan context sebagai parameter ketiga untuk return fungsi render.

### 2. Routing pada urls.py
Penambahan path('wishlist/', include('wishlist.urls')) pada variabel urlpatterns. Hal tersebut untuk melakukan routing terhadap fungsi views yang telah dibuat sebelumnya sehingga nantinya halaman HTML dapat ditampilkan.

### 3. Memetakan data dengan katalog.html
Untuk memetakan data terhadap data yang telah di-render pada views, menggunakan sintaks khusus template, yaitu {{data}}. Misal, mengubah Fill me! yang terdapat pada file html menjadi {{nama}} dan {{Student_ID}}. Untuk menampilkan list barang ke dalam tabel pada halaman html, dilakukan iterasi untuk mengambil data-data pada database.

### 4. Deployment ke heroku
Pertama-tama, buat aplikasi baru terlebih dahulu pada heroku dengan nama pbp-tugas-deploy-amanda. Setelah itu, memasukan variabel repository secret HEROKU_APP_NAME dan HEROKU_API_KEY pada GitHub Actions (Settings -> Secrets -> Actions). Lalu disimpan.