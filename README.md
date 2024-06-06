
# Capstone Project Grup 44
## Part of IBM Skillsbuild For AI & Cybersecurity 

## Judul Proyek: 

### Daftar Isi
1. [Deskripsi Proyek](#deskripsi-proyek)
2. [Anggota Kelompok](#anggota-kelompok)
3. [Latar Belakang](#latar-belakang)
4. [Tujuan](#tujuan)
5. [Metodologi](#metodologi)
6. [Data](#data)
7. [Pemrosesan Data](#pemrosesan-data)
8. [Model Pembelajaran Mesin](#model-pembelajaran-mesin)
9. [Hasil dan Analisis](#hasil-dan-analisis)
10. [Kesimpulan](#kesimpulan)
11. [Cara Menjalankan Proyek](#cara-menjalankan-proyek)
12. [Kontak](#kontak)

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan model machine learning yang akurat untuk menilai kelayakan kredit UMKM (Usaha Mikro, Kecil, dan Menengah). Dengan menggunakan data historis dari berbagai atribut UMKM, model ini diharapkan dapat meningkatkan akses pendanaan bagi UMKM yang membutuhkan pinjaman untuk pengembangan usaha mereka.

## Anggota Kelompok
- **Dhika Nusratul Janah** - Project Manager 
- **Natasha Dwi Pramudita** - Data Scientist
- **Alang Artha Iwana** - Fullstack
- **Nanggala Jalasena Pramana Putra** - BackEnd 
- **Rafly Gymnastiar** - DevOps Engineer 

## Latar Belakang


## Tujuan
1. Mengembangkan model machine learning yang akurat untuk menilai kelayakan kredit UMKM.
2. Meningkatkan akses pendanaan bagi UMKM dengan memberikan penilaian kredit yang lebih tepat.
3. Mengidentifikasi faktor-faktor penting yang mempengaruhi kelayakan kredit UMKM.

## Metodologi
1. **Pengumpulan Data**: Mengumpulkan data dari sumber-sumber terpercaya, dalam hal ini dataset dari Kaggle.
2. **Pemrosesan Data**: Membersihkan dan mempersiapkan data untuk analisis.
3. **Eksplorasi Data**: Analisis deskriptif untuk memahami data.
4. **Modeling**: Membangun model pembelajaran mesin untuk prediksi.
5. **Evaluasi**: Mengevaluasi model dan melakukan tuning untuk meningkatkan akurasi.

## Data
Data yang digunakan dalam proyek ini mencakup:
- Usia
- Jenis Kelamin
- Pendapatan
- Tingkat Pendidikan
- Status Pernikahan
- Jumlah Anak
- Status Kepemilikan Rumah
- Skor Kredit

Sumber data: Kaggle (https://www.kaggle.com/datasets/sujithmandala/credit-score-classification-dataset)

## Pemrosesan Data
Langkah-langkah pemrosesan data meliputi:
1. Mengatasi nilai yang hilang dengan metode imputasi. Setiap nilai yang hilang dalam dataset diatasi menggunakan teknik imputasi, seperti mean imputation untuk data numerik dan mode imputation untuk data kategorikal.
2. Encoding variabel kategorikal menggunakan Label Encoding. Variabel kategorikal, seperti jenis kelamin, status pernikahan, dan status kepemilikan rumah, diubah menjadi format numerik menggunakan Label Encoding agar dapat digunakan dalam model pembelajaran mesin.
3. Normalisasi dan standarisasi fitur. Fitur-fitur numerik dinormalisasi atau distandarisasi untuk memastikan bahwa mereka berada dalam skala yang sama, sehingga tidak ada fitur yang mendominasi yang lain dalam proses pelatihan model.

## Model Pembelajaran Mesin
Kami menggunakan beberapa model pembelajaran mesin untuk prediksi, termasuk:
- **Logistic Regression**
- **Random Forest**
- **XGBoost**
- **LGBM**

### Implementasi Model
Model dilatih menggunakan data historis dan divalidasi menggunakan teknik train-test split. Hyperparameter tuning dilakukan untuk mendapatkan performa terbaik.

## Hasil dan Analisis
Hasil evaluasi menunjukkan bahwa model Random Forest memiliki performa terbaik dengan akurasi mencapai 100%. Model ini menunjukkan kemampuan yang sangat baik dalam mengklasifikasikan kelayakan kredit UMKM.

### Logistic Regression
- Akurasi: 93.94%
- Precision, Recall, dan F1-score menunjukkan performa yang baik, terutama untuk kelas dengan jumlah data yang lebih besar.

### Random Forest
- Akurasi: 100%
- Model ini memberikan hasil yang sempurna pada data uji, menunjukkan performa yang sangat kuat dalam klasifikasi.

### XGBoost
- Akurasi: 90.91%
- Model ini juga menunjukkan performa yang baik, meskipun sedikit di bawah Random Forest.

### LGBM
- Akurasi: 69.70%
- Model ini menunjukkan performa yang kurang dibandingkan dengan model lainnya, kemungkinan karena parameter yang digunakan belum optimal.

## Kesimpulan
Penelitian ini berhasil mengembangkan model machine learning yang akurat untuk menilai kelayakan kredit UMKM. Model Random Forest menunjukkan performa terbaik dan akan digunakan dalam aplikasi UMKM Priority untuk memberikan rekomendasi kredit yang lebih akurat. Dengan demikian, diharapkan dapat meningkatkan akses pendanaan bagi UMKM dan mendukung pertumbuhan bisnis mereka.

## Cara Menjalankan Proyek
1. Clone repository ini: `git clone https://github.com/username/project.git`
2. Masuk ke direktori proyek: `cd project`
3. Instal dependensi: `pip install -r requirements.txt`
4. Jalankan script untuk melatih model: `python train_model.py`
5. Untuk melihat hasil prediksi: ``

## Kontak
Untuk informasi lebih lanjut, silakan hubungi kami:
- **Dhika Nusratul Janah** - dikanusratul011@gmail.com
- **Natasha Dwi Pramudita** - natashadwipramudita@gmail.com
- **Alang Artha Iwana** - f1d021075@student.unram.ac.id
- **Nanggala Jalasena Pramana Putra** - nanggalajalasena.21006@mhs.unesa.ac.id
- **Rafly Gymnastiar** - rafly.gymnastiar.zulmi-2021@fst.unair.ac.id

---
