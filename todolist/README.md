Amanda Nadhifah Zahra Andini
2106637246
PBP-A
Link hasil deploy: https://pbp-tugas-deploy-amanda.herokuapp.com/

# README Tugas 4

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

- Kegunaan dari {% csrf_token %} adalah untuk untuk membandingan key csrf saat end-user ingin melakukan method post atau get sehingga form digunakan dan diakses oleh user yang tepat.
- Jika tidak ada {% csrf_token %} pada elemen <form>, website yang kita miliki dapat tetap berjalan. Akan tetapi, memiliki risiko yang tinggi untuk bisa diakses secara umum.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Kita dapat membuat elemen <form> secara manual dengan membuat tag table dan menggunakan {% csrf_token %}. Kemudian, pada views.py menggunakan method POST untuk mengirim data yang diinput saat submit user ke server dan method GET untuk mengambil data tersebut.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Ketika user mengisi form dan menekan tombol submit, data yang diinput tadi akan dapat diakses menggunakan method get. Jika form dan data valid, data akan tersimpan pada database dengan perintah form.save() yang terdapat pada create_task di views.py. urls.py akan melakukan routing dan mencari views yang sesuai pada views.py Setelah data disimpan, looping pada file html akan mengakses data yang tersimpan untuk ditampilkan sebagai respons.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Membuat aplikasi baru bernama todolist dengan menjalankan perintah python manage.py startapp todolist.
- Menambahkan ‘todolist’ pada variabel INSTALLED_APPS di settings.py
- Menambahkan path todolist/ pada variabel urlpatterns di urls.py yang terdapat di direktori project_django
- Memodifikasi models.py dengan membuat model data Task dengan atribut user, date, title, dan description.
- Memodifikasi views.py dengan menambahkan fungsi show_todolist, register, login, logout, create_task
- Membuat file todolist.html pada direktori templates untuk halaman utama
- Membuat file create_task.html pada direktori templates untuk halaman pembuatan task baru
- Membuat halaman form untuk pembuatan task pada file forms.py
- Membuat file urls.py dan menambahkan path url dari fungsi-fungsi yang sudah dibuat pada file views.py pada variabel urlpatterns untuk melakukan routing.

# README Tugas 5

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Inline CSS

Kode CSS yang langsung ditulis di dalam elemen HTML sebagai atribut. Kelebihan: Efektif jika ingin menguji dan melihat perubahan pada satu elemen saja, dapat memperbaiki kode dan tampilan dengan cepat. Kekurangan: tidak efisien karena hanya dapat diterapkan pada satu elemen HTML atau halaman kode yang diubah saja.

### Internal CSS

Internal CSS adalah kode CSS yang ditulis di bagian atas (header) HTML pada HTMLtag <style>. Kelebihan: tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file. Kekurangan: perubahan pada Internal CSS hanya berlaku pada satu halaman saja, tidak efisien apabila jika ingin menggunakan CSS yang sama dalam beberapa file.

### External CSS

Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML yang biasanya ditulis di suatu file khusus berekstensi .css. Kelebihan: berguna jika ingin mendesain beberapa halaman website atau file html secara bersamaan karena ile CSS dapat digunakan di beberapa halaman website sekaligus, ukuran file HTML akan menjadi lebih kecil, dan struktur dari kode HTML jadi lebih rapi. Kekurangan:tidak efisien jika digunakan hanya untuk halaman atau elemen yang sedikit.

## Jelaskan tag HTML5 yang kamu ketahui.

- p: untuk membuat paragraf
- h1: sampai h6 untuk header
- br: new line
- hr: membuat garis horizontal
- title: untuk judul halaman
- body: untuk membuat isi dari halaman
- form: untuk membuat form
- img: insert picture
- a: insert hyperlink
- input: untuk membuat sebuah kontrol input
- button: membuat tombol yang bisa diklik
- ul: membuat list selain nomor
- ol: membuat list dengan nomor
- table: membuat tabel
- th: header tabel
- tr: baris tabel
- td: kolom tabel

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- "." untuk elemen dalam suatu class
- ID selector menggunakan "#"
- Tag selector, misal tag body, p, span, h1, h2, h3, dsb

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Pada base.html di template, menambahkan <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous"> pada head dan <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script> pada body agar dapat mengimplementasikan bootstrap.
- Masih pada base.html, tambahkan <meta name="viewport" content="width=device-width, initial-scale=1.0"> pada head agar keempat halaman menjadi responsive.
- Kustomisasi file register.html, login.html, create_task.html, todolist.html dengan kode-kode yang terdapat pada web bootsrap, misal mengubah backround color, text-color, padding, table, dsb.
