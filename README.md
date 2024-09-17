# PR 3 #

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
![xml](https://github.com/user-attachments/assets/6574ffe9-1f22-452a-ac6e-d20eba923b63)

**xml id**
![xmlid](https://github.com/user-attachments/assets/a4ccdb13-ba86-4bed-b3e8-1aebb9e74860)

**json**
![json](https://github.com/user-attachments/assets/d39e71bf-84d3-4ae1-86d8-a72be2ac0121)

**json id**
![jsonid](https://github.com/user-attachments/assets/9fe9fa3b-ac36-4b6a-88b6-0c26088c0c49)
