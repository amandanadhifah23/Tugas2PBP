Amanda Nadhifah Zahra Andini
2106637246
PBP-A
Link hasil deploy: https://pbp-tugas-deploy-amanda.herokuapp.com/ 

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
•	Kegunaan dari {% csrf_token %} adalah untuk untuk membandingan key csrf saat end-user ingin melakukan method post atau get sehingga form digunakan dan diakses oleh user yang tepat.
•	Jika tidak ada {% csrf_token %} pada elemen <form>, website yang kita miliki dapat tetap berjalan. Akan tetapi, memiliki risiko yang tinggi untuk bisa diakses secara umum.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita dapat membuat elemen <form> secara manual dengan membuat tag table dan menggunakan {% csrf_token %}. Kemudian, pada views.py menggunakan method POST untuk mengirim data yang diinput saat submit user ke server dan method GET untuk mengambil data tersebut.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika user mengisi form dan menekan tombol submit, data yang diinput tadi akan dapat diakses menggunakan method get. Jika form dan data valid, data akan tersimpan pada database dengan perintah form.save() yang terdapat pada create_task di views.py. urls.py akan melakukan routing dan mencari views yang sesuai pada views.py Setelah data disimpan, looping pada file html akan mengakses data yang tersimpan untuk ditampilkan sebagai respons.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
•	Membuat aplikasi baru bernama todolist dengan menjalankan perintah python manage.py startapp todolist.
•	Menambahkan ‘todolist’ pada variabel INSTALLED_APPS di settings.py
•	Menambahkan path todolist/ pada variabel urlpatterns di urls.py yang terdapat di direktori project_django
•	Memodifikasi models.py dengan membuat model data Task dengan atribut user, date, title, dan description.
•	Memodifikasi views.py dengan menambahkan fungsi show_todolist, register, login, logout, create_task
•	Membuat file todolist.html pada direktori templates untuk halaman utama
•	Membuat file create_task.html pada direktori templates untuk halaman pembuatan task baru
•	Membuat halaman form untuk pembuatan task pada file forms.py
•	Membuat file urls.py dan menambahkan path url dari fungsi-fungsi yang sudah dibuat pada file views.py pada variabel urlpatterns untuk melakukan routing.
