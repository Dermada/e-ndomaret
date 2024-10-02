# Jawaban Pertanyaan README Tugas 5

### **1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!?** ###

- Specificity (Kekhususan): CSS menentukan elemen mana yang paling spesifik.

  - Inline styles (diterapkan langsung pada elemen HTML melalui atribut style) memiliki prioritas tertinggi.
  - ID selectors (#myID) lebih spesifik daripada class selectors (.myClass) atau type selectors (p, div).
  - Pseudo-classes dan pseudo-elements juga memiliki prioritas, namun umumnya lebih rendah dari ID selectors.
- Source Order (Urutan Sumber): Jika dua selector memiliki tingkat kekhususan yang sama, yang muncul terakhir dalam stylesheet akan digunakan.

- Important Declaration (!important): Properti yang ditandai dengan !important akan selalu mengesampingkan aturan lainnya kecuali ada aturan lain dengan !important yang lebih spesifik.

### **2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!** ###

Kita harus memastikan bahwa tampilan website dapat menyesuaikan dengan ukuran layar dan perangkat yang digunakan pengguna. Konsep ini penting karena pengguna web saat ini mengakses situs dari berbagai perangkat dengan ukuran layar yang berbeda, seperti desktop, tablet, dan smartphone.

**Contoh Aplikasi:**
- Sudah Menerapkan Responsive Design: Twitter, Facebook, dan Wikipedia adalah contoh situs yang menerapkan desain responsif dengan baik.
- Belum Menerapkan Responsive Design: Beberapa situs lokal seperti SIAKNG.

### **3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!** ###

**Margin:** Jarak antara elemen dengan elemen lain di sekitarnya. Margin adalah ruang luar elemen.
Contoh:
```
div {
  margin: 20px;
}
```

**Border:** Garis yang mengelilingi elemen. Border berada di antara margin dan padding.
```
div {
  border: 2px solid black;
}
```
**Padding:** Jarak antara konten elemen dengan batas (border) elemen tersebut. Padding adalah ruang dalam elemen.
```
div {
  padding: 10px;
}
```

### **4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!** ###

**Flexbox:**

Flexbox (Flexible Box Layout) adalah modul layout CSS yang dirancang untuk mengatur dan mendistribusikan ruang di sepanjang satu dimensi (baris atau kolom) dalam container. Flexbox sangat berguna untuk membuat layout yang fleksibel, di mana elemen di dalam container dapat dengan mudah diratakan (aligned), didistribusikan (distributed), dan diatur ulang (reordered).

Kegunaan:
- Membuat tata letak yang dinamis dan responsif.
- Memudahkan pembuatan elemen-elemen yang tersusun secara horisontal atau vertikal dengan fleksibilitas tinggi.

```
.container {
  display: flex;
  justify-content: center; /* Align items horizontally */
  align-items: center; /* Align items vertically */
}
```

**Grid Layout:**

- CSS Grid Layout adalah modul layout dua dimensi yang memungkinkan pembuatan grid yang lebih kompleks dan dapat dikustomisasi. Berbeda dengan flexbox yang hanya bekerja di satu dimensi, grid bekerja di dua dimensi (baris dan kolom).

Kegunaan:
- Membuat tata letak yang lebih kompleks seperti dashboard, galeri foto, atau grid layout pada aplikasi web.
- Lebih baik untuk struktur halaman yang presisi dan teratur, di mana elemen-elemen perlu diatur dalam grid.

```
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Membuat 3 kolom dengan lebar yang sama */
  gap: 10px;
}
```

### **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!** ###

- Menambahkan Tailwind ke Aplikasi
- menambahkan fungsi *mood* ke aplikasi
- menambahkan fitur hapus *mood* ke aplikasi
- menambahkan *navbar* ke aplikasi
- *styling* menggunakan Tailwind dan External CSS