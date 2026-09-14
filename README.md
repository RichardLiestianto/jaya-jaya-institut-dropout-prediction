# Proyek Akhir: Prediksi Dropout Mahasiswa Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan dengan reputasi yang baik. Namun, institusi menghadapi permasalahan berupa tingginya jumlah mahasiswa yang tidak menyelesaikan pendidikan atau mengalami **dropout**.

Berdasarkan dataset yang digunakan dalam proyek ini, terdapat **4.424 mahasiswa**, dengan **1.421 mahasiswa atau sekitar 32,12%** berstatus Dropout. Kondisi tersebut menunjukkan bahwa dropout merupakan permasalahan yang cukup signifikan dan perlu ditangani secara lebih proaktif.

Untuk membantu Jaya Jaya Institut, proyek ini mengembangkan analisis data, dashboard monitoring, serta model machine learning yang dapat digunakan sebagai **early warning system** untuk membantu mengidentifikasi mahasiswa yang berisiko dropout.

### Permasalahan Bisnis

Permasalahan utama yang dihadapi Jaya Jaya Institut adalah tingginya jumlah mahasiswa yang mengalami dropout. Institusi membutuhkan pendekatan berbasis data untuk:

1. Memahami karakteristik dan faktor yang berkaitan dengan mahasiswa yang mengalami dropout.
2. Memonitor kondisi mahasiswa melalui dashboard yang mudah dipahami.
3. Mengidentifikasi mahasiswa yang berisiko dropout lebih awal agar institusi dapat memberikan intervensi atau bimbingan yang sesuai.

### Cakupan Proyek

Proyek ini mencakup beberapa tahapan utama, yaitu:

* melakukan eksplorasi dan pemahaman terhadap data mahasiswa;
* melakukan data preparation untuk kebutuhan machine learning;
* mengembangkan dan mengevaluasi model klasifikasi untuk mendeteksi risiko dropout;
* membuat dashboard menggunakan Metabase untuk memonitor status dan performa mahasiswa;
* membuat prototype machine learning menggunakan Streamlit;
* melakukan deployment prototype ke Streamlit Community Cloud;
* menyusun kesimpulan serta rekomendasi action items berdasarkan hasil analisis.

Model machine learning pada proyek ini difokuskan pada klasifikasi biner, yaitu membedakan mahasiswa menjadi kategori **Dropout** dan **Not Dropout**, sehingga hasil prediksi dapat digunakan sebagai alat bantu early warning bagi institusi.

## Persiapan

### Sumber Data

Dataset yang digunakan adalah **Students' Performance** yang disediakan oleh Dicoding. Dataset terdiri dari **4.424 observasi dan 37 kolom**, yang mencakup informasi demografis, latar belakang pendidikan, kondisi finansial, performa akademik semester pertama dan kedua, kondisi ekonomi, serta status mahasiswa.

Variabel `Status` memiliki tiga kategori:

* `Graduate`
* `Dropout`
* `Enrolled`

Untuk kebutuhan machine learning, target diubah menjadi klasifikasi biner:

* `1` = Dropout
* `0` = Not Dropout

### Setup Environment

Library utama yang digunakan pada proyek ini tercantum pada file `requirements.txt`.

Untuk menginstal seluruh dependency, jalankan:

```bash
pip install -r requirements.txt
```

Isi utama `requirements.txt` adalah:

```text
joblib==1.5.1
matplotlib==3.10.3
numpy==2.2.6
pandas==2.2.3
scikit-learn==1.6.1
seaborn==0.13.2
streamlit==1.56.0
```

### Menjalankan Prototype Machine Learning

Prototype machine learning dibuat menggunakan Streamlit. Untuk menjalankannya secara lokal, jalankan:

```bash
streamlit run app.py
```

Aplikasi umumnya dapat diakses melalui:

```text
http://localhost:8501
```

Prototype juga telah di-deploy menggunakan **Streamlit Community Cloud** dan dapat diakses melalui:

https://jaya-jaya-institut-dropout-prediction-test.streamlit.app/

Prototype menerima informasi mahasiswa sebagai input dan menghasilkan:

* prediksi **Dropout** atau **Not Dropout**;
* probabilitas risiko dropout;
* informasi early warning sebagai pendukung tindak lanjut dari pihak institusi.

Hasil prediksi digunakan sebagai alat bantu dan tidak dimaksudkan sebagai satu-satunya dasar dalam pengambilan keputusan terhadap mahasiswa.

## Business Dashboard

Dashboard dibuat menggunakan **Metabase** untuk membantu Jaya Jaya Institut dalam memahami kondisi mahasiswa serta memonitor faktor-faktor penting yang berkaitan dengan dropout.

Dashboard yang dibuat bernama:

**Jaya Jaya Institut - Student Performance & Dropout Dashboard**

Dashboard terdiri dari beberapa visualisasi utama:

1. **Total Students**
   Menampilkan jumlah keseluruhan mahasiswa dalam dataset, yaitu **4.424 mahasiswa**.

2. **Dropout Rate**
   Menampilkan persentase mahasiswa yang mengalami dropout, yaitu **32,12%** atau sebanyak **1.421 mahasiswa**.

3. **Student Status Distribution**
   Menampilkan distribusi mahasiswa berdasarkan status:

   * Graduate: **2.209 mahasiswa**
   * Dropout: **1.421 mahasiswa**
   * Enrolled: **794 mahasiswa**

4. **Dropout Rate by Tuition Fee Status**
   Visualisasi ini menunjukkan perbedaan dropout rate berdasarkan status pembayaran biaya kuliah:

   * Tuition Fees Up to Date: **24,74%**
   * Tuition Fees Not Up to Date: **86,55%**

   Hasil tersebut menunjukkan bahwa mahasiswa dengan pembayaran biaya kuliah yang tidak up to date memiliki tingkat dropout yang jauh lebih tinggi.

5. **Average Approved Curricular Units by Student Status**
   Visualisasi ini membandingkan rata-rata jumlah unit kurikuler yang berhasil diselesaikan mahasiswa pada semester pertama dan kedua.

   * Dropout:

     * Semester 1: **2,55**
     * Semester 2: **1,94**
   * Enrolled:

     * Semester 1: **4,32**
     * Semester 2: **4,06**
   * Graduate:

     * Semester 1: **6,23**
     * Semester 2: **6,18**

   Hasil tersebut menunjukkan bahwa mahasiswa yang mengalami dropout memiliki performa akademik yang lebih rendah dibandingkan mahasiswa Enrolled maupun Graduate.

### Akses Metabase

Metabase dijalankan secara lokal menggunakan Docker.

Akses Metabase:

```text
http://localhost:3000
```

Kredensial:

```text
Email    : root@mail.com
Password : root123
```

File database internal Metabase yang berisi konfigurasi dashboard disertakan dalam submission dengan nama:

```text
metabase.db.mv.db
```

Screenshot dashboard juga disertakan dalam folder submission dengan format:

```text
username_dicoding-dashboard.png
```

## Modeling dan Evaluation

Model machine learning dikembangkan sebagai solusi untuk membantu mengidentifikasi mahasiswa yang berisiko dropout.

Dua algoritma klasifikasi digunakan sebagai perbandingan:

* **Logistic Regression**
* **Random Forest Classifier**

Kedua model menggunakan preprocessing pipeline yang sama. Fitur numerik diproses menggunakan `StandardScaler`, sedangkan fitur kategorikal diproses menggunakan `OneHotEncoder`.

Data dibagi menjadi data training dan testing dengan proporsi **80:20** menggunakan stratified sampling agar distribusi target tetap terjaga.

### Hasil Evaluasi Model

| Model               | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |    0.889 |     0.878 |  0.761 |    0.815 |   0.932 |
| Random Forest       |    0.882 |     0.902 |  0.711 |    0.795 |   0.925 |

Berdasarkan hasil evaluasi, **Logistic Regression dipilih sebagai model final** karena memberikan performa yang lebih seimbang, terutama pada Recall dan F1-Score.

Recall sebesar **76,1%** menunjukkan bahwa model mampu mendeteksi sekitar tiga dari empat mahasiswa yang benar-benar mengalami dropout pada data testing.

Dari **284 mahasiswa Dropout** pada data testing, model berhasil mendeteksi sekitar **216 mahasiswa**, sedangkan sekitar **68 mahasiswa Dropout** belum berhasil terdeteksi.

Model final kemudian disimpan dalam bentuk pipeline pada:

```text
model/dropout_prediction_model.joblib
```

Pipeline tersebut digunakan langsung oleh aplikasi Streamlit sehingga proses preprocessing dan prediksi tetap konsisten dengan proses training.

## Conclusion

Berdasarkan hasil analisis, dropout merupakan permasalahan yang cukup signifikan di Jaya Jaya Institut. Dari total **4.424 mahasiswa**, sebanyak **1.421 mahasiswa atau 32,12%** mengalami dropout.

Hasil dashboard menunjukkan bahwa faktor finansial dan performa akademik memiliki pola yang kuat terhadap status mahasiswa. Mahasiswa dengan status pembayaran biaya kuliah **Not Up to Date** memiliki dropout rate sebesar **86,55%**, jauh lebih tinggi dibandingkan mahasiswa dengan pembayaran **Up to Date** sebesar **24,74%**.

Perbedaan juga terlihat pada performa akademik. Mahasiswa Dropout rata-rata hanya berhasil menyelesaikan **2,55 unit kurikuler pada semester pertama** dan **1,94 unit pada semester kedua**, sedangkan mahasiswa Graduate masing-masing berhasil menyelesaikan rata-rata **6,23** dan **6,18 unit**.

Solusi machine learning menggunakan **Logistic Regression** menghasilkan Accuracy sebesar **88,9%**, Recall sebesar **76,1%**, F1-Score sebesar **81,5%**, dan ROC-AUC sebesar **93,2%**. Model tersebut dapat digunakan sebagai alat bantu early warning untuk membantu institusi mengidentifikasi mahasiswa yang berisiko dropout lebih awal.

Dengan menggabungkan dashboard monitoring dan sistem prediksi, Jaya Jaya Institut dapat melakukan pemantauan mahasiswa secara lebih terstruktur dan memberikan intervensi yang lebih cepat terhadap mahasiswa yang membutuhkan perhatian.

## Rekomendasi Action Items

Berdasarkan hasil analisis dan modeling, beberapa action items yang dapat dilakukan oleh Jaya Jaya Institut adalah:

1. **Memprioritaskan mahasiswa dengan kendala pembayaran biaya kuliah.**
   Mahasiswa dengan status pembayaran biaya kuliah yang tidak up to date memiliki dropout rate sebesar **86,55%**. Institusi dapat melakukan monitoring pembayaran lebih dini serta menawarkan konsultasi, skema pembayaran, atau dukungan finansial kepada mahasiswa yang mengalami kendala.

2. **Melakukan monitoring performa akademik sejak semester awal.**
   Mahasiswa yang mengalami dropout memiliki rata-rata jumlah unit kurikuler yang berhasil diselesaikan jauh lebih rendah dibandingkan mahasiswa Graduate. Institusi dapat menetapkan indikator early warning berdasarkan jumlah mata kuliah yang berhasil diselesaikan dan nilai akademik pada semester pertama maupun kedua.

3. **Memberikan pendampingan akademik kepada mahasiswa berisiko.**
   Mahasiswa dengan performa akademik rendah dapat diarahkan untuk mendapatkan bimbingan akademik, tutoring, konseling, atau evaluasi beban studi sebelum kondisi tersebut berkembang menjadi risiko dropout yang lebih tinggi.

4. **Menggunakan model machine learning sebagai early warning system.**
   Prototype yang telah dikembangkan dapat digunakan untuk membantu mengidentifikasi mahasiswa dengan probabilitas dropout yang tinggi. Hasil prediksi sebaiknya digunakan sebagai pendukung proses monitoring, bukan sebagai satu-satunya dasar pengambilan keputusan.

5. **Melakukan evaluasi berkala terhadap dashboard dan model.**
   Data mahasiswa baru perlu ditambahkan secara berkala sehingga dashboard tetap mencerminkan kondisi terkini. Model machine learning juga perlu dievaluasi dan diperbarui secara periodik agar performanya tetap relevan terhadap karakteristik mahasiswa terbaru.
