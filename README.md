# Proyek Akhir: Prediksi Dropout Mahasiswa Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan dengan reputasi yang baik. Namun, institusi juga menghadapi permasalahan berupa adanya mahasiswa yang tidak menyelesaikan pendidikannya atau mengalami **dropout**.

Tingginya jumlah mahasiswa dropout menjadi perhatian bagi institusi karena dapat memengaruhi keberhasilan proses pendidikan. Oleh karena itu, Jaya Jaya Institut membutuhkan pendekatan berbasis data yang dapat membantu memahami kondisi mahasiswa serta mendeteksi mahasiswa yang berpotensi mengalami dropout sedini mungkin agar institusi dapat memberikan bimbingan atau intervensi yang sesuai.

### Permasalahan Bisnis

Permasalahan utama dalam proyek ini adalah bagaimana Jaya Jaya Institut dapat memanfaatkan data mahasiswa untuk:

1. Memahami karakteristik mahasiswa yang berkaitan dengan kondisi dropout.
2. Memonitor performa dan kondisi mahasiswa melalui dashboard yang mudah dipahami.
3. Mengidentifikasi mahasiswa yang berpotensi mengalami dropout lebih awal sehingga institusi dapat memberikan intervensi yang sesuai.

### Cakupan Proyek

Proyek ini mencakup beberapa tahapan utama, yaitu:

* melakukan pemahaman dan eksplorasi terhadap data mahasiswa;
* melakukan data preparation untuk kebutuhan machine learning;
* mengembangkan model klasifikasi untuk memprediksi potensi **Dropout** atau **Graduate**;
* mengevaluasi performa model machine learning;
* membuat dashboard menggunakan Metabase untuk memonitor kondisi dan performa mahasiswa;
* membuat prototype prediction system menggunakan Streamlit;
* melakukan deployment prototype menggunakan Streamlit Community Cloud;
* menyusun kesimpulan dan rekomendasi action items berdasarkan hasil analisis.

Untuk kebutuhan machine learning, hanya mahasiswa dengan status akhir **Graduate** dan **Dropout** yang digunakan dalam proses training. Target diubah menjadi klasifikasi biner:

* `0` = Graduate
* `1` = Dropout

Mahasiswa berstatus **Enrolled** tidak digunakan dalam proses training karena status akhirnya belum diketahui. Data tersebut dipisahkan untuk digunakan sebagai data prediksi di masa depan.

## Persiapan

### Sumber Data

Dataset dapat diakses melalui tautan berikut:

https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Dataset yang digunakan adalah **Students' Performance** yang disediakan oleh Dicoding. Dataset terdiri dari **4.424 observasi dan 37 kolom**, yang mencakup informasi demografis, latar belakang pendidikan, kondisi finansial, performa akademik semester pertama dan kedua, kondisi ekonomi, serta status mahasiswa.

Variabel `Status` memiliki tiga kategori:

* `Graduate`
* `Dropout`
* `Enrolled`

Untuk kebutuhan machine learning, target diubah menjadi klasifikasi biner:

* `1` = Dropout
* `0` = Graduate

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

* prediksi **Dropout** atau **Graduate**;
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

### Menjalankan Dashboard Metabase

Dashboard dibuat menggunakan **Metabase v0.62.4.5** dan dijalankan menggunakan Docker.

Pastikan **Docker Desktop** telah terinstal dan berjalan sebelum mengikuti tahapan berikut.

#### 1. Pull image Metabase

```bash
docker pull metabase/metabase:v0.62.4.5
```

#### 2. Membuat container Metabase

```bash
docker run -d -p 3000:3000 --name metabase metabase/metabase:v0.62.4.5
```

#### 3. Hentikan container Metabase

```bash
docker stop metabase
```

#### 4. Salin database Metabase ke dalam container

Pastikan file `metabase.db.mv.db` berada pada direktori tempat command dijalankan.

```bash
docker cp metabase.db.mv.db metabase:/metabase.db/metabase.db.mv.db
```

#### 5. Jalankan kembali container

```bash
docker start metabase
```

#### 6. Akses Dashboard

Setelah container berjalan, buka:

```text
http://localhost:3000
```

Kredensial Metabase:

```text
Email    : root@mail.com
Password : root123
```

Dashboard yang digunakan pada proyek ini bernama:

**Jaya Jaya Institut - Student Performance & Dropout Dashboard**

Dashboard menggunakan PostgreSQL pada Supabase sebagai sumber data mahasiswa sehingga koneksi internet diperlukan agar Metabase dapat mengakses sumber data.

## Modeling dan Evaluation

Model machine learning dikembangkan untuk membantu Jaya Jaya Institut memprediksi apakah mahasiswa yang sedang menempuh pendidikan memiliki kecenderungan menuju status **Dropout** atau **Graduate**.

### Persiapan Data untuk Modeling

Pada proses modeling, hanya data mahasiswa yang telah memiliki status akhir yang digunakan, yaitu:

* **Graduate:** 2.209 mahasiswa
* **Dropout:** 1.421 mahasiswa

Mahasiswa dengan status **Enrolled** sebanyak 794 mahasiswa **tidak digunakan dalam proses training**, karena mahasiswa tersebut masih menjalani pendidikan sehingga status akhirnya belum diketahui.

Data Enrolled dipisahkan dan dapat digunakan sebagai data untuk melakukan prediksi menggunakan model yang telah dilatih.

Target kemudian diubah menjadi klasifikasi biner:

* `0` = Graduate
* `1` = Dropout

Data modeling dibagi menjadi data training dan testing dengan proporsi **80:20** menggunakan stratified sampling agar proporsi kelas Graduate dan Dropout tetap terjaga.

### Preprocessing

Fitur dibagi menjadi fitur numerik dan kategorikal.

* Fitur numerik diproses menggunakan `StandardScaler`.
* Fitur kategorikal diproses menggunakan `OneHotEncoder`.

Seluruh proses preprocessing digabungkan dengan model menggunakan `Pipeline` agar proses transformasi data pada saat training dan prediction tetap konsisten.

### Model yang Digunakan

Dua algoritma klasifikasi digunakan sebagai perbandingan:

1. **Logistic Regression**
2. **Random Forest Classifier**

Kedua model dilatih menggunakan data yang sama dan dievaluasi menggunakan Accuracy, Precision, Recall, F1-Score, dan ROC-AUC.

### Hasil Evaluasi

| Model               | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |    93,4% |     91,0% |  92,3% |    91,6% |   97,6% |
| Random Forest       |    93,0% |     94,0% |  87,7% |    90,7% |   97,3% |

Berdasarkan hasil evaluasi, **Logistic Regression** memberikan performa terbaik secara keseluruhan. Model menghasilkan Accuracy sebesar **93,4%**, Recall sebesar **92,3%**, F1-Score sebesar **91,6%**, dan ROC-AUC sebesar **97,6%**.

Random Forest memiliki Precision yang lebih tinggi, yaitu **94,0%**, tetapi Logistic Regression memiliki Recall dan F1-Score yang lebih tinggi pada kelas Dropout.

Dalam konteks proyek ini, Recall menjadi metrik yang penting karena menunjukkan kemampuan model dalam mendeteksi mahasiswa yang benar-benar termasuk dalam kelas **Dropout**. Recall yang lebih tinggi dapat membantu mengurangi jumlah mahasiswa berisiko dropout yang tidak terdeteksi oleh sistem.

Oleh karena itu, **Logistic Regression dipilih sebagai model final** untuk memprediksi apakah mahasiswa memiliki kecenderungan menuju status Dropout atau Graduate.

Model final beserta preprocessing pipeline disimpan pada:

```text
model/dropout_prediction_model.joblib
```

Model tersebut kemudian digunakan pada prototype Streamlit untuk melakukan prediksi terhadap mahasiswa yang status akhirnya belum diketahui, seperti mahasiswa yang masih berstatus **Enrolled**.

## Conclusion

Berdasarkan hasil analisis terhadap data mahasiswa Jaya Jaya Institut, terdapat **4.424 mahasiswa** yang terdiri dari **2.209 Graduate**, **1.421 Dropout**, dan **794 Enrolled**. Mahasiswa dengan status Dropout mencakup sekitar **32,12%** dari keseluruhan data, sehingga permasalahan dropout menjadi hal yang penting untuk dimonitor oleh institusi.

Hasil analisis dashboard menunjukkan adanya beberapa karakteristik yang berkaitan dengan kondisi dropout.

Dari sisi finansial, mahasiswa dengan status pembayaran biaya kuliah **Not Up to Date** memiliki dropout rate sebesar **86,55%**, jauh lebih tinggi dibandingkan mahasiswa dengan pembayaran **Up to Date** yang memiliki dropout rate sebesar **24,74%**. Hal ini menunjukkan bahwa kondisi pembayaran biaya kuliah merupakan salah satu faktor penting yang perlu diperhatikan dalam proses monitoring mahasiswa.

Dari sisi akademik, mahasiswa Dropout memiliki rata-rata jumlah unit kurikuler yang berhasil diselesaikan sebesar **2,55 pada semester pertama** dan **1,94 pada semester kedua**. Nilai tersebut lebih rendah dibandingkan mahasiswa Graduate yang rata-rata berhasil menyelesaikan **6,23 unit pada semester pertama** dan **6,18 unit pada semester kedua**. Temuan ini menunjukkan bahwa performa akademik pada semester awal dapat menjadi indikator penting untuk mendeteksi risiko dropout.

Pada proses machine learning, hanya mahasiswa dengan status akhir **Graduate** dan **Dropout** yang digunakan sebagai data training. Mahasiswa berstatus **Enrolled** tidak dilibatkan dalam training karena status akhirnya belum diketahui dan dapat digunakan sebagai data untuk prediction di masa depan.

Dari dua model yang diuji, **Logistic Regression** dipilih sebagai model final dengan performa:

* Accuracy: **93,4%**
* Precision: **91,0%**
* Recall: **92,3%**
* F1-Score: **91,6%**
* ROC-AUC: **97,6%**

Recall sebesar **92,3%** menunjukkan bahwa model memiliki kemampuan yang baik dalam mendeteksi mahasiswa yang benar-benar termasuk dalam kelas Dropout.

Dengan menggabungkan **dashboard monitoring** dan **prototype machine learning**, Jaya Jaya Institut dapat melakukan monitoring kondisi mahasiswa secara lebih terstruktur serta menggunakan model sebagai **early warning system** untuk membantu mengidentifikasi mahasiswa yang berpotensi mengalami dropout lebih awal.

## Rekomendasi Action Items

Berdasarkan hasil analisis dan modeling, beberapa action items yang dapat diterapkan oleh Jaya Jaya Institut adalah:

1. **Memprioritaskan monitoring mahasiswa yang memiliki kendala pembayaran biaya kuliah.**
   Mahasiswa dengan status pembayaran **Not Up to Date** memiliki dropout rate sebesar **86,55%**. Institusi dapat melakukan monitoring pembayaran secara berkala serta menyediakan konsultasi, skema pembayaran, atau dukungan finansial bagi mahasiswa yang mengalami kesulitan.

2. **Melakukan monitoring performa akademik sejak semester awal.**
   Mahasiswa Dropout memiliki jumlah unit kurikuler yang berhasil diselesaikan lebih rendah dibandingkan mahasiswa Graduate. Institusi dapat menggunakan jumlah mata kuliah yang berhasil diselesaikan dan nilai akademik semester awal sebagai indikator untuk menentukan mahasiswa yang membutuhkan perhatian lebih lanjut.

3. **Memberikan intervensi akademik kepada mahasiswa berisiko.**
   Mahasiswa dengan performa akademik rendah dapat diberikan program pendampingan seperti bimbingan akademik, tutoring, konseling, atau evaluasi beban studi untuk membantu meningkatkan peluang mahasiswa menyelesaikan pendidikan.

4. **Menggunakan model Logistic Regression sebagai early warning system.**
   Model dapat diterapkan pada mahasiswa yang masih berstatus **Enrolled** untuk memperkirakan kecenderungan menuju **Dropout** atau **Graduate**. Mahasiswa dengan probabilitas dropout yang tinggi dapat diprioritaskan untuk proses monitoring dan intervensi lebih lanjut.

5. **Menggabungkan hasil prediksi dengan evaluasi dari pihak institusi.**
   Hasil prediksi machine learning sebaiknya digunakan sebagai alat bantu dan tidak dijadikan satu-satunya dasar pengambilan keputusan. Pihak akademik tetap perlu mempertimbangkan kondisi individual mahasiswa sebelum menentukan bentuk intervensi.

6. **Melakukan evaluasi dan pembaruan model secara berkala.**
   Model sebaiknya dievaluasi kembali ketika tersedia data mahasiswa baru yang telah memiliki status akhir Graduate atau Dropout. Dengan demikian, model dapat terus menyesuaikan diri dengan karakteristik mahasiswa terbaru dan mempertahankan performa prediksi yang baik.
