#### **1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).** ####
  - membuat directory baru yang akan menjadi git local project saya
  - Membuat Aplikasi dengan nama `main`
      - Dengan menjalankan perintah :
        ``` 
        python manage.py startapp main
        ```
  - Melakukan Routing pada Proyek agar Dapat Menjalankan Aplikasi `main`
  - Membuat Model `Product` di Aplikasi `main`
  - Membuat Function `show_main` pada `views.py`
  - Buat folder `templates` di dalam aplikasi `main`, kemudian buat template html `main`
  - Membuat Routing pada `urls.py` di Aplikasi `main`
#### **2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.** ####
![bagan guys](http://Images/photo_2024-09-11_10-01-38.jpg)

#### **3. Jelaskan fungsi git dalam pengembangan perangkat lunak!** ####
Git memungkinkan tim pengembang untuk mengelola berbagai versi kode secara efisien. Setiap perubahan yang dilakukan pada kode dapat dilacak dan disimpan sebagai commit. Git juga mendukung pengembang bekerja bersama pada satu proyek secara bersamaan. 

#### **4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?** ####
Django menggunakan pola Model-View-Controller (MVC) (walaupun di Django disebut Model-Template-View, atau MTV), yang membantu pemula memahami konsep dasar arsitektur pengembangan perangkat lunak.

#### **5. Mengapa model pada Django disebut sebagai ORM?** ####
Model pada Django disebut ORM karena Django menggunakan teknik Object-Relational Mapping untuk memungkinkan pengembang bekerja dengan database relasional menggunakan objek dan kelas Python. Django ORM mengabstraksi detail query SQL dan relasi database, memberikan antarmuka yang lebih intuitif dan efisien untuk mengelola data dalam aplikasi web.
