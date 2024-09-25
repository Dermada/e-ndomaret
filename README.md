
# Jawaban Pertanyaan README Tugas 4


### **1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?** ###

- HttpResponseRedirect: Ini adalah kelas di Django yang digunakan untuk mengembalikan respons HTTP yang mengarahkan pengguna ke URL tertentu. Anda harus memberikan URL lengkap atau relatif sebagai argumen.
- redirect: Ini adalah fungsi shortcut di Django yang lebih mudah digunakan. Fungsi ini dapat menerima URL, nama view, atau bahkan objek model dan secara otomatis akan mengonversinya menjadi URL yang sesuai.

### **2. Jelaskan cara kerja penghubungan model Product dengan User** ###

Untuk menghubungkan model Product dengan User, Anda biasanya menggunakan ForeignKey. Berikut adalah langkah-langkahnya:

1. **Definisikan Model:** Buat model Product dan tambahkan field user yang merupakan ForeignKey ke model User.
2. **Migrasi:** Jalankan perintah makemigrations dan migrate untuk membuat dan menerapkan migrasi.
3. **Gunakan dalam View:** Dalam view, Anda bisa mengakses produk yang terkait dengan user tertentu.

### **3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.** ###

**Perbedaan antara Authentication dan Authorization**
- Authentication: Proses verifikasi identitas pengguna. Ini biasanya dilakukan dengan memeriksa kredensial seperti username dan password.
- Authorization: Proses menentukan apa yang diizinkan dilakukan oleh pengguna yang telah terautentikasi. Ini melibatkan pengecekan izin atau peran pengguna.
Saat pengguna login, Django melakukan proses authentication dengan memverifikasi kredensial pengguna. Jika berhasil, Django membuat session untuk pengguna tersebut.

**Implementasi Authentication dan Authorization di Django**
- Authentication: Django menggunakan `django.contrib.auth` untuk menangani proses login, logout, dan manajemen user.
- Authorization: Django menggunakan izin dan grup untuk mengatur apa yang bisa dilakukan oleh pengguna.

### **4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?** ###

Django menggunakan session untuk mengingat pengguna yang telah login. Saat pengguna berhasil login, Django membuat session dan menyimpan session ID dalam cookie di browser pengguna.

**Kegunaan Lain dari Cookies dan Keamanan**
- Kegunaan Lain: Cookies dapat digunakan untuk menyimpan preferensi pengguna, melacak aktivitas pengguna, dan menyimpan data sementara.
- Keamanan: Tidak semua cookies aman. Cookies yang menyimpan informasi sensitif harus dienkripsi dan diberi atribut HttpOnly dan Secure.

### **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).** ###

- membuat fungsi `login_user` ke dalam `views.py`
- membuat dan mengisi `login.html` untuk login pagenya
- membuat fungsi `logout_user` ke dalam `views.py`
- membuat *logout button* di `main.html`
- restriksi halaman main dengan `@login_required(login_url='/login')`
- menambahkan `last_login` pada `login_user` untuk melihat kapan terakhir kali login
- menambahkan *last login* pada fungsi `show_main`
- menghubungkan product entry dengan user menggunakan *foreignkey*
- melakukan url routing untuk semua fungsi yang ditambahkan
- migrate
