# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dengan reputasi yang sangat baik. Namun, mereka menghadapi masalah tingginya angka mahasiswa yang putus sekolah (dropout). Tingginya angka dropout ini dapat merugikan institusi secara finansial maupun reputasi.

### Permasalahan Bisnis
Permasalahan utama yang ingin diselesaikan adalah tingginya angka mahasiswa dropout. Jaya Jaya Institut ingin mendeteksi secepat mungkin mahasiswa yang berisiko dropout sehingga dapat memberikan intervensi dini, seperti bimbingan akademik khusus maupun dukungan finansial.

### Cakupan Proyek
Cakupan proyek ini meliputi:
1. Melakukan analisis eksplorasi data (EDA) yang mendalam (Univariate dan Multivariate) untuk menemukan faktor-faktor utama, pola, dan tren penyebab mahasiswa dropout.
2. Membangun model machine learning untuk memprediksi probabilitas mahasiswa dropout berdasarkan data historis dan mengekstrak Feature Importance.
3. Membuat prototype aplikasi berbasis web (Streamlit) yang dapat digunakan institusi untuk memasukkan data mahasiswa dan mendapatkan prediksi risiko dropout secara real-time.
4. Membuat business dashboard untuk memonitor performa akademik dan faktor-faktor risiko mahasiswa.

### Persiapan

Sumber data: [students_performance.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv)

Setup environment:
**Python Version: Python 3.13** (Disarankan menggunakan Python versi 3.13 ke atas agar tidak ada isu kompatibilitas).

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Business Dashboard
Business Dashboard dibuat menggunakan Metabase. Dashboard ini mencakup visualisasi dari metrik-metrik penting seperti distribusi status mahasiswa, tingkat dropout berdasarkan status hutang, rata-rata usia pendaftar, dan pengaruh uang kuliah terhadap status kelulusan mahasiswa. 
(Berkas database metabase disertakan dalam proyek: `metabase.db.mv.db`)
Kredensial Metabase:
Email: root@mail.com
Password: root123

## Menjalankan Sistem Machine Learning
Prototype sistem machine learning dikembangkan menggunakan Streamlit. Sistem ini akan meminta user memasukkan data-data akademik dan latar belakang mahasiswa, lalu model akan mengembalikan prediksi apakah mahasiswa tersebut berpotensi Lulus (Graduate) atau Putus Sekolah (Dropout).

Tautan prototype (Streamlit Community Cloud): [https://belajar-penerapan-data-science-tugas-akhir-fikriars.streamlit.app/](https://belajar-penerapan-data-science-tugas-akhir-fikriars.streamlit.app/)

Cara menjalankan prototype secara lokal:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Conclusion

Berdasarkan analisis dan pemodelan data yang telah dilakukan, terdapat dua kesimpulan utama:

**1. Kesimpulan Analisis Karakteristik Dropout (Berdasarkan EDA)**
Dari Exploratory Data Analysis, pola utama yang membedakan mahasiswa berpotensi lulus dan dropout sangat dipengaruhi oleh aspek akademik dan finansial. Mahasiswa yang akhirnya dropout secara umum memiliki karakteristik:
- **Performa Akademik (Faktor Dominan):** Gagal meluluskan banyak mata kuliah di semester 1 dan semester 2. Rata-rata unit mata kuliah yang disetujui (approved) pada mahasiswa dropout sangat rendah mendekati 0.
- **Kondisi Finansial:** Status hutang (Debtor = 1) dan tunggakan uang kuliah (Tuition fees up to date = 0) sangat kuat berkaitan dengan tingginya rasio dropout.
- **Usia saat Mendaftar:** Rata-rata mahasiswa yang mendaftar di usia yang lebih tua memiliki rasio dropout yang lebih tinggi dibandingkan lulusan siswa tingkat menengah reguler.

**2. Kesimpulan Kuantitatif Performa Model Machine Learning**
Model machine learning berbasis **Random Forest Classifier** telah dibangun dan diuji pada set pengujian dengan performa kuantitatif sebagai berikut:
- **Accuracy**: ~87.7%
- **F1-Score**: ~88.5%
Model ini dinilai sangat baik dalam mendeteksi dan memisahkan kelas Dropout dan Graduate.

Berdasarkan grafik **Feature Importance**, fitur yang paling berpengaruh secara berurutan dalam memprediksi dropout adalah:
1. `Curricular_units_2nd_sem_approved`
2. `Curricular_units_2nd_sem_grade`
3. `Curricular_units_1st_sem_approved`
4. `Curricular_units_1st_sem_grade`
5. `Tuition_fees_up_to_date`

### Rekomendasi Action Items
Berdasarkan kesimpulan, berikut adalah rekomendasi action items yang harus dilakukan Jaya Jaya Institut:
- **Program Bimbingan Akademik Dini**: Wajibkan bimbingan dan kelas perbaikan intensif bagi mahasiswa yang gagal atau mendapat nilai buruk di paruh pertama Semester 1, mengingat unit mata kuliah semester 1 adalah fitur prediktor terpenting.
- **Bantuan dan Konseling Finansial Dini**: Berikan opsi cicilan pembayaran atau beasiswa ringan bagi mahasiswa yang terindikasi mulai menunggak uang kuliah sebelum mereka terpaksa dropout karena alasan biaya.
- **Monitoring Khusus untuk Mahasiswa Non-Reguler/Lebih Tua**: Sediakan program adaptasi dan dukungan penyusunan jadwal belajar khusus untuk mahasiswa yang mendaftar di usia yang lebih matang, mengingat mereka seringkali memiliki kesibukan ganda (misal bekerja).
