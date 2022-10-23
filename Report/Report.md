# Laporan Proyek Machine Learning - Arieska Restu Harpian Dwika


## Project Overview

Buku adalah kumpulan atau himpunan kertas atau lembaran yang tertulis atau mengandung tulisan tentang informasi-informasi. Buku merupakan sumber informasi dari segala aspek bidang, seperti iptek, seni budaya, politik, ekonomi, sosial dan pertahanan keamanan, dan lain-lain. Membaca buku dapat membuka wawasan dunia intelek sehingga dapat mengubah masa depan dan dapat mencerdaskan akal, pikiran, dan iman. Dengan membaca buku, selain pengetahuan yang akan semakin bertambah, semakin menurun juga efek negatif, seperti kenakalan terhadap anak-anak. Anak-anak yang tidak memiliki minat baca sejak dini akan semakin kecil peluangnya untuk mengembangkan pengetahuan setingi-tingginya.

Berdasarkan laporan Bank Dunia, Indonesia merupakan negara yang memiliki minat baca yang sangat rendah. Hal tersebut sangat disayangkan karena sebagai negara yang besar, Indonesia memiliki potensi yang besar untuk menjadi negara yang unggul. Rendahnya minat baca di masyarakat menjadi masalah yang sangat penting di dunia pendidikan saat ini. Untuk mengatasi masalah tersebut, diperlukan suatu sistem yang dapat memudahkan para pembaca untuk mendapatkan informasi mengenai buku-buku yang akan dibaca selanjutnya.

Sistem rekomendasi adalah sistem yang bertujuan untuk memperkirakan informasi yang menarik bagi user dan juga membantu user dalam menentukan pilihannya. Terdapat dua pendekatan yang digunakan dalam sistem rekomendasi, yaitu *content based filtering* dan *collaborative filtering. Content based filtering* merupakan metode yang bekerja dengan mencari kedekatan suatu item yang akan direkomendasikan ke user dengan items yang telah diambil oleh pengguna sebelumnya berdasarkan kemiripan antar kontennya. Sedangkan metode *collaborative filtering* adalah metode yang digunakan untuk melakukan prediksi kegunaan item berdasarkan penilaian pengguna sebelumnya. Pada proyek ini akan membuat sistem rekomendasi buku dengan menggunakan metode *content based filtering*.

## Business Understanding

### **Problem Statements**

Berdasarkan pemaparan permasalahan pada bagian project overview tersebut, adapun pernyataan masalah yaitu bagaimana membuat sistem yang dapat merekomendasikan buku yang mirip dengan buku sesuai dengan input.

### **Goals**

Berdasarkan permasalahan pada bagian domain proyek di atas, tujuan yang ingin diperoleh dari proyek ini yaitu membuat sistem yang dapat merekomendasikan buku yang mirip dengan buku sesuai dengan input.

### Solution Statement

Untuk meraih *goals* yang telah disebutkan pada bagian *goals* di atas, yaitu dengan cara membuat sistem untuk mencari kemiripan dari buku sesuai dengan input dengan menggunakan derajat kesamaan (*similarity degree*).

## Data Understanding

Data yang digunakan dalam proyek ini adalah data ***************************Book Recommendation Dataset***************************. Dalam dataset ini terdapat data buku, data rating dari buku tersebut, dan data user yang memberi rating pada buku tersebut. Data ini diperoleh dari **************webiste************** Kaggle dengan link [https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) yang diakses pada tanggal 22 Oktober 2022. Untuk memahami data tersebut, dilakukan proses-proses seperti data loading dan deskripsi variabel.

### Data Loading

Proses data loading dilakukan dengan menggunakan fungsi read_csv() dari library pandas. Pada 

### Deskripsi Variabel

Berdasarkan data books yang digunakan dalam proyek ini, terdapat delapan variabel yaitu:

- ISBN : merupakan nomor International Standard Book Number dari buku.
- Book-Title : merupakan judul dari buku.
- Book-Author : merupakan penulis dari buku.
- Year-Of-Publication : merupakan tahun buku terbit.
- Publisher : merupakan penerbit dari buku.
- Image-URL-S : merupakan link yang berisikan gambar cover dari buku berukuran kecil.
- Image-URL-M : merupakan link yang berisikan gambar cover dari buku berukuran sedang.
- Image-URL-L : merupakan link yang berisikan gambar cover dari buku berukuran besar.

Pada data ratings yang digunakan pada proyek ini, terdapat tiga variabel yaitu:

- User-ID : merupakan id dari user yang memberi rating pada buku.
- ISBN : merupakan nomor International Standard Book Number dari buku.
- Book-Rating : merupakan rating dari buku.

Pada data users yang digunakan pada proyek ini terdapat tiga variabel yaitu:

- User-ID : merupakan id dari user yang memberi rating pada buku.
- Location : merupakan lokasi dari user yang memberi rating pada buku.
- Age : merupakan umur dari user yang memberi rating pada buku.

Setelah memahami deskripsi variabel pada tiap-tiap data, selanjutnya adalah mengecek informasi pada tiap-tiap data menggunakan fungsi info(). Informasi pada data ditunjukkan pada gambar 1, gambar 2, dan gambar 3 berikut.



![gambar 1](https://user-images.githubusercontent.com/89245500/197402084-ea2219fd-d27b-4e1c-b0a3-f3920d88aa88.png)

Gambar 1. Informasi pada data books


![gambar 2](https://user-images.githubusercontent.com/89245500/197402121-d82b0386-ee37-4a95-8226-75aafab55221.png)

Gambar 2. Informasi pada data ratings

![gambar 3](https://user-images.githubusercontent.com/89245500/197402129-3786b31d-fd3c-40c5-b95b-77cf28d5e453.png)

Gambar 3. Informasi pada data users

Berdasarkan gambar 1 di atas, dapat diketahui bahwa file Books.csv ****memiliki 271360 entri. Pada gambar 2, dapat diketahui bahwa file Ratings.csv memiliki 1149780 entri. Selain itu, pada gambar 3, dapat diketahui bahwa file Users memiliki 278858 entri.

Deskripsi statistik dari data dapat diketahui dengan menggunakan fungsi describe(). Deskripsi statistik dari tiap-tiap data dapat dilihat pada tabel 1, tabel 2, dan tabel 3 berikut ini.

Tabel 1. Deskirpsi statistik dari data books

| index | ISBN | Book-Title | Book-Author | Year-Of-Publication | Publisher | Image-URL-S | Image-URL-M | Image-URL-L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 271360 | 271360 | 271359 | 271360 | 271358 | 271360 | 271360 | 271357 |
| unique | 271360 | 242135 | 102023 | 202 | 16807 | 271044 | 271044 | 271041 |
| top | 0195153448 | Selected Poems | Agatha Christie | 2002 | Harlequin | http://images.amazon.com/images/P/185326119X.01.THUMBZZZ.jpg | http://images.amazon.com/images/P/185326119X.01.MZZZZZZZ.jpg | http://images.amazon.com/images/P/225307649X.01.LZZZZZZZ.jpg |
| freq | 1 | 27 | 632 | 13903 | 7535 | 2 | 2 | 2 |

Tabel 2. Deskirpsi statistik dari data ratings

| index | User-ID | Book-Rating |
| --- | --- | --- |
| count | 1149780.0 | 1149780.0 |
| mean | 140386.39512602412 | 2.8669501991685364 |
| std | 80562.27771851212 | 3.8541838592016537 |
| min | 2.0 | 0.0 |
| 25% | 70345.0 | 0.0 |
| 50% | 141010.0 | 0.0 |
| 75% | 211028.0 | 7.0 |
| max | 278854.0 | 10.0 |

Tabel 3. Deskirpsi statistik dari data ratings

| index | User-ID | Age |
| --- | --- | --- |
| count | 278858.0 | 168096.0 |
| mean | 139429.5 | 34.75143370454978 |
| std | 80499.51502027822 | 14.428097382455457 |
| min | 1.0 | 0.0 |
| 25% | 69715.25 | 24.0 |
| 50% | 139429.5 | 32.0 |
| 75% | 209143.75 | 44.0 |
| max | 278858.0 | 244.0 |

Fungsi describe() memberikan informasi statistik pada masing-masing kolom, antara lain:

- Count adalah jumlah sampel pada data.
- Mean adalah nilai rata-rata.
- Std adalah standar deviasi.
- Min yaitu nilai minimum setiap kolom.
- 25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama.
- 50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- 75% adalah kuartil ketiga.
- Max adalah nilai maksimum.

Setelah memahami tiap dataset yang akan digunakan dalam proyek ini, selanjutnya adalah mengecek jumlah data dan kolom pada tiap dataset, serta mengecek jumlah data yg kosong pada tiap dataset. Untuk mengecek jumlah dan kolom pada suatu dataset, dapat menggunakan fungsi .shape. Jumlah data dan kolom pada tiap dataset yaitu sebagai berikut.

- Books Shape 	:  (271360, 8)
- Ratings Shape :  (1149780, 3)
- Users Shape 	:  (278858, 3)

Sedangkan untuk mengecek jumlah data yg kosong pada tiap dataset, dapat dilakukan dengan menggunakan fungsi isnull() yang kemudian dijumlah dengan menggunakan fungsi sum(). Jumlah data yg kosong pada tiap dataset yaitu sebagai berikut.

Any null values in Books :
ISBN                   0
Book-Title             0
Book-Author            1
Year-Of-Publication    0
Publisher              2
Image-URL-S            0
Image-URL-M            0
Image-URL-L            3
dtype: int64

Any null values in Ratings :
User-ID        0
ISBN           0
Book-Rating    0
dtype: int64

Any null values in Users :
User-ID          0
Location         0
Age         110762
dtype: int64

## Data Preparation

Sebelum melakukan modeling, data perlu disiapkan terlebih dahulu. Proses ini biasa disebut sebagai data preparation. Data preparation merupakan tahap melakukan proses transformasi pada data sehingga data menjadi bentuk yang cocok untuk proses pemodelan. Pada proyek ini, proses-proses yang akan dilakukan di tahap data preparation yaitu menggabungkan data books dan data ratings berdasarkan ISBN, menghilangkan missing values, mereset index dan menghapus kolom index yg ada, menghapus kolom ISBN, Year-Of-Publication, Image-URL-S, Image-URL-M, menghapus sample yang memiliki nilai book rating sebesar 0, dan menghapus satu atau lebih karakter non-alfanumerik dalam kolom Book-Title.

Proses penggabungan data books dan data ratings berdasarkan ISBN dilakukan dengan menggunakan fungsi merge(). Tujuan dari proses penggabungan ini yaitu agar dapat mengetahui rating yang diberikan user kepada buku. Proses selanjutnya yaitu menghilangkan missing values. Proses ini dilakukan agar tidak ada data yang mengandung missing values. Proses ini dilakukan dengan menggunakan fungsi dropna(). 

Proses selanjutnya adalah mereset index dan menghapus kolom index yang ada. Proses ini dilakukan dengan menggunakan fungsi reset_index(). Kemudian menghapus kolom atau fitur yang sudah tidak digunakan, seperti ISBN, Year-Of-Publication, Image-URL-S, Image-URL-M dengan menggunakan fungsi drop().

Setelah itu, proses menghapus sample yang memiliki nilai book rating sebesar 0. Proses ini bertujuan untuk menghilangkan buku yang memiliki rating yang sangat buruk yakni 0. Pada proses ini juga dilakukan dengan menggunakan fungsi drop(). Selanjutnya adalah proses menghapus satu atau lebih karakter non-alfanumerik dalam kolom Book-Title. Proses ini dilakukan untuk memudahkan proses transformasi ke dalam bentuk matriks yang nantinya akan dilakukan.

## Modeling

Setelah melakukan tahap business understanding, data understanding, dan data preparation, maka langkah selanjutnya adalah modeling atau model development. Pada tahap ini akan dilakukan proses mengembangkan sistem rekomendasi buku dengan pendekatan content based filtering. Metode ini memiliki beberapa kelebihan yaitu sebagai berikut.

- Content based filtering tidak bergantung pada user lain. Content based filtering membangun profil dengan cara mengeksploitasi berdasarkan penilaian yang disediakan oleh pengguna aktif.
- Dalam content based filtering terdapat perincian cara kerja sistem rekomendasi dalam memunculkan item yang relevan berdasarkan fitur konten.
- Content based filtering mampu merekomendasikan item yang belum dinilai oleh setiap pengguna.

Namun, metode content based filtering tetap memiliki kekurangan. Kekurangan-kekurangan dari metode ini yaitu sebagai berikut.

- Content based filtering memiliki keterbatasan dalam jumlah, jenis fitur yang terkait, apakah secara otomatis atau manual, begitupula dengan item-item yang disarankan.
- Content based filtering tidak memiliki metode yang melekat untuk menemukan sesuatu yang tidak terduga. Sistem hanya akan menunjukkan item yang nilainya tinggi untuk dicocokkan dengan profil pengguna, maka pengguna akan selalu menemukan item serupa dengan yang sudah direkomendasikan sebelumnya.
- Sistem akan tidak dapat memberikan rekomendasi yang dapat diandalkan pada pengguna baru, karena membutuhkan penelusuran terlebih dahulu pada preferensi pengguna.

Pada proyek ini, proses yang akan dilakukan pada tahap modeling yaitu membuat fungsi yang dapat memberikan rekomendasi buku dari judul buku yang dimasukkan sebaga parameternya. Pada awal fungsi, tipe data pada parameter judul buku diubah menjadi string. Selanjutnya melakukan pengecekan apakah judul buku yang dimasukkan sebagai parameter terdapat dalam kolom Book-Title. Jika tidak ada, maka sistem tidak merekomendasikan buku apapun. Apabila ada, maka proses akan dilanjutkan.

Proses selanjutnya adalah menghitung jumlah rating pada setiap buku. Kemudian apabila jumlah rating pada buku kurang dari atau sama dengan 200, maka buku tersebut akan dimasukkan dalam kategori buku langka. Sedangkan yang jumlah ratingnya lebih dari 200, maka termasuk kategori buku umum.

Setelah itu, akan dilakukan pengecekan apakah judul buku yang dimasukkan sebagai parameter terdapat dalam buku rare atau tidak. Apabila ada, maka sistem tidak dapat merekomendasikan buku apapun. Akan tetapi, sistem akan menampilkan tiga buku yang sering muncul. Apabila tidak ada, maka proses akan tetap dilanjutkan.

Proses selanjutnya yaitu menghapus data duplicate dalam kolom Book-Title pada kategori buku umum dengan menggunakan fungsi drop_duplicates(). Kemudian mereset index dan menghapus kolom index yg ada, serta membuat kolom index baru sesuai dengan urutan data pada kategori buku umum. Selanjutnya membuat kolom all_features yg berisi nilai-nilai dari kolom target, dimana kolom target adalah Book-Title, Book-Author, Publisher.

Setelah itu, proses berikutnya adalah mengonversi teks pada kolom all_features menjadi matriks jumlah token. Kemudian dari matriks jumlah token tersebut dihitung derajat kesamaan cosinus. Selanjutnya membuat list bernomor dari buku-buku yang sama seperti judul buku yang dimasukkan sebaga parameter. Dari buku-buku yang sama tersebut diambil lima buah buku dimasukkan ke dalam sebuah list. Dari list tersebut akan ditampilkan dalam bentuk grafik. Pada grafik yang berisi buku-buku yang direkomendasikan, akan menampilkan gambar cover dari buku dan ratingnya.

## ****Evaluation****

Setelah membuat fungsi yang dapat memberikan rekomendasi buku, maka selanjutnya adalah mencobanya. Percobaan pertama yang akan dilakukan adalah mendapatkan rekomendasi buku yang mirip dengan buku yang berjudul The Five People You Meet in Heaven. Hasil rekomendasi yang diberikan oleh sistem yaitu sebagai berikut.

![gambar 4](https://user-images.githubusercontent.com/89245500/197402174-bcfe8bdc-dde6-4d58-a872-e25465a88f93.png)

Gambar 4. Hasil rekomendasi yang mirip dengan The Five People You Meet in Heaven

Untuk percobaan kedua yaitu mendapatkan rekomendasi buku yang mirip dengan buku yang berjudul The Angel Is Near. Hasil rekomendasi yang diberikan oleh sistem yaitu seperti yang ditunjukkan pada gambar 5 berikut.

![gambar 5](https://user-images.githubusercontent.com/89245500/197402177-784e40cb-f586-42a1-9d8b-cb8884681f22.png)

Gambar 5. Hasil rekomendasi yang mirip dengan The Angel Is Near

Untuk percobaan ketiga yaitu mendapatkan rekomendasi buku yang mirip dengan buku yang berjudul Tuesdays with Morrie An Old Man a Young Man and Life s Greatest Lesson. Hasil rekomendasi yang diberikan oleh sistem yaitu seperti yang ditunjukkan pada gambar 6 berikut ini.

![gambar 6](https://user-images.githubusercontent.com/89245500/197402178-756a7397-558f-4401-9378-09c5b77aea06.png)

Gambar 6. Hasil rekomendasi yang mirip dengan Tuesdays with Morrie An Old Man a Young Man and Life s Greatest Lesson

Untuk percobaan keempat yaitu mendapatkan rekomendasi buku yang mirip dengan buku yang berjudul A Soldier of the Great War. Hasil rekomendasi yang diberikan oleh sistem yaitu seperti yang ditunjukkan pada gambar 7 di bawah ini.

![gambar 7](https://user-images.githubusercontent.com/89245500/197402179-dab4694c-f0b8-4cce-abd2-f8b79a3578bd.png)

Gambar 7. Hasil rekomendasi yang mirip dengan A Soldier of the Great War

Untuk percobaan kelima yaitu mendapatkan rekomendasi buku yang mirip dengan buku yang berjudul Life of Pi. Hasil rekomendasi yang diberikan oleh sistem yaitu seperti yang ditunjukkan pada gambar 8 berikut.

![gambar 8](https://user-images.githubusercontent.com/89245500/197402181-da99cdc6-ec01-446e-ae02-3eb9f7acecae.png)

Gambar 8. Hasil rekomendasi yang mirip dengan Life of Pi
