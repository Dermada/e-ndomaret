# Jawaban Pertanyaan README Tugas 6

### **1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!** ###
- Interaktivitas yang dinamis<br />
  JavaScript memungkinkan pengembang produk untuk membuat elemen web yang interaktif. Dengan JavaScript, pengembang dapat menambahkan animasi, dropdowns, dan elemen lainnya yang dapat meningkatkan kualitas penggunaan web.

- *Asynchronus Programming* (AJAX)<br />
  Dengan AJAX (Asynchronous JavaScript and XML), JavaScript dapat berkomunikasi dengan server secara asinkron, memungkinkan pengambilan data tanpa perlu memuat ulang seluruh halaman, sehingga aplikasi terasa lebih responsif.

- Kompabilitas yang luas<br />
  Sudah banyak sekali browser yang *compatilbe* dengan JavaScript hal ini memungkinkan pengguna untuk mengakses produk dari hampir semua *web browser*.

### **2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?** ###

Fungsi penggunaan `await` saat menggunakan `fetch()` dalam JavaScript adalah untuk menunggu resolusi promise yang dikembalikan oleh fungsi `fetch()`. `fetch()` adalah fungsi asinkron yang mengembalikan sebuah promise yang mewakili operasi pengambilan data dari server. Menggunakan `await` memastikan bahwa kode akan menunggu hingga promise selesai (baik berhasil atau gagal) sebelum melanjutkan ke baris kode berikutnya.

Jika kita tidak menggunakan `fetch()`, maka kode akan langsung bergerak ke baris berikutnya meskipun `fetch()` belum selesai mengambil data. Akibatnya, variabel yang seharusnya menyimpan hasil `fetch()` (misalnya, `response`) mungkin berisi promise yang belum selesai.

### **3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?** ###

**Margin:** Jarak antara elemen dengan elemen lain di sekitarnya. Margin adalah ruang luar elemen.
Decorator `@csrf_exempt` digunakan untuk menonaktifkan proteksi CSRF pada view yang menangani AJAX POST request.

### **4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?** ###

Pembersihan di backend sangat penting untuk mencegah serangan seperti XSS karena backend adalah lapisan yang tidak dapat dimanipulasi oleh pengguna. Backend bertanggung jawab untuk memastikan bahwa semua input dibersihkan dan output diencode dengan aman sebelum ditampilkan kepada pengguna lain. Hal ini, bersama dengan kebijakan keamanan konten (CSP) dan best practice lainnya, dapat membantu melindungi aplikasi dari serangan seperti XSS yang berbahaya.

### **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!** ###

- menambahkan *error message* pada login di `views.py`
- menambahkan fungsi AJAX untuk menambah data *mood* di `views.py`
- mengimplementasikan modal form untuk menambahkan *mood* pada *Tailwind*
- menambahkan tombol *Add Mood* dengan menggunakan AJAX pada `main.html`
- melindungi web dari serangan XSS dengan membersihkan data di *backend* menggunakan DOMPurifty `strip_tags`