=======
#### **1. Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?** ####

Data delivery diperlukan untuk memastikan bahwa data dapat diakses dan digunakan oleh berbagai komponen dalam platform. Ini memungkinkan integrasi yang mulus antara berbagai layanan dan aplikasi, memastikan bahwa data yang tepat tersedia pada waktu yang tepat untuk pengambilan keputusan dan operasi yang efisien.

#### **2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?** ####

JSON lebih baik dibandingkan XML dalam banyak kasus karena lebih ringan dan lebih mudah dibaca oleh manusia. JSON lebih populer karena sintaksnya yang sederhana dan kemampuannya untuk dengan mudah diintegrasikan dengan bahasa pemrograman modern, terutama JavaScript. JSON juga lebih efisien dalam hal parsing dan serialisasi data.

#### **3. Jelaskan fungsi git dalam pengembangan perangkat lunak!** ####

Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dikirimkan ke form memenuhi semua aturan validasi yang telah ditentukan. Kita membutuhkan method ini untuk memastikan bahwa data yang diterima adalah valid sebelum diproses lebih lanjut, sehingga dapat mencegah kesalahan dan potensi masalah keamanan.

#### **4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?** ####

Kita membutuhkan `csrf_token` untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Jika kita tidak menambahkan `csrf_token`, penyerang dapat membuat permintaan palsu dari situs lain yang tampak sah, yang dapat menyebabkan tindakan yang tidak diinginkan pada aplikasi kita. Tanpa `csrf_token`, penyerang dapat mengeksploitasi sesi pengguna yang sedang aktif untuk melakukan tindakan tanpa sepengetahuan pengguna.

#### **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).** ####

- membuat berkas baru dengan nama `forms.py` untuk menerima products baru
- menambahkan fungsi baru `create_mood_entry` yang menerima parameter `request`
- tambahkan Fungsi `Products.objects.all()` digunakan untuk mengambil seluruh objek `Products` yang tersimpan pada *database*.
- membuat berkas HTML untuk form dengan nama `create_product_entry.html`
- menambahkan tampilan data *mood* dan tombol *new entry* pada `main.html`
- Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID
- update path urls pada `urls.py`

#### **Screenshot hasil url pada Postman** ####

**xml**
![xml](Images\Screenshot_2024-09-17_114800.png)

**xml id**
![xmlid](Images\Screenshot_2024-09-17_115121.png)

**json**
![json](Images\Screenshot_2024-09-17_115144.png)

**json id**
![jsonid](Images\Screenshot_2024-09-17_115154.png)
