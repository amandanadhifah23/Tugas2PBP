## Jelaskan perbedaan antara JSON, XML, dan HTML!
- HTML (Hypertext Markup Language) merupakan bahasa markup untuk mengelola serangkaian data dan informasi sehingga dapat diakses dan ditampilkan pada halaman dan aplikasi web. Intinya HTML membuat halaman web.
- XML (Extensible Markup Language) merupakan bahasa markup untuk menyimpan dan transfer data dari satu aplikasi ke aplikasi lain melalui internet dengan lebih terstruktur.
- JSON (JavaScript Object Notation) merupakan format data untuk menyimpan, membaca, dan menukar informasi dari web server, agar dapat dibaca user. JSON lebih sederhana dibanding XML. Dari segi penyimpanan, JSON menyimpan elemen dengan lebih efisien dibanding XML, tetapi tidak rapi untuk dilihat.


## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Pada saat membuat atau mengembangkan suatu platform, pasti kita memerlukan pertukaran data user dengan data server. Data delivery (HTML, XML, JSON) diperlukan untuk memudahkan developers transfer atau pengiriman data dari satu stack ke stack lain dengan baik dan lebih mudah dibaca.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Hal pertama yang dilakukan adalah membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 dengan menjalankan python manage.py startapp mywatchlist. Lalu, mendaftarkan aplikasi tersebut pada variabel INSTALLED_APPS dengan menambahkan 'mywatchlist'. Menambahkan path mywatchlist dengan menambahkan path('mywatchlist/°,include('mywatchlist.urls")). Kemudian, membuat sebuah model MyWatchList yang memiliki 5 atribut pada models.py. Selanjutnya, menjalankan perintah python manage.py makemigrations dan python manage.py migrate. Membuat folder bernama fixtures dan membuat file initial_watchlist.json, kemudian loaddata dengan menjalankan python manage.py loaddata initial_watchlist.json. Pada views.py, membuat fungsi show_mywatchlist, show_mywatchlist_xml, dan show_mywatchlist_json. Lalu, buka urls.py yang ada pada folder wishlist dan import fungsi yang sudah dibuat.

## HTML Postman
![Screenshoot HTML](/HTML Postman.jpg)
## XML Postman
![Screenshoot XML](/XML Postman.jpg)
## JSON Postman
![Screenshoot JSON](/JSON Postman.jpg)