# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dengan reputasi yang sangat baik. Namun, mereka menghadapi masalah tingginya angka mahasiswa yang putus sekolah (dropout). Tingginya angka dropout ini dapat merugikan institusi secara finansial maupun reputasi.

### Permasalahan Bisnis
Permasalahan utama yang ingin diselesaikan adalah tingginya angka mahasiswa dropout. Jaya Jaya Institut ingin mendeteksi secepat mungkin mahasiswa yang berisiko dropout sehingga dapat memberikan intervensi dini, seperti bimbingan akademik khusus maupun dukungan finansial.

### Cakupan Proyek
Cakupan proyek ini meliputi:
1. Melakukan analisis eksplorasi data (EDA) untuk menemukan faktor-faktor utama penyebab mahasiswa dropout.
2. Membangun model machine learning untuk memprediksi probabilitas mahasiswa dropout berdasarkan data historis.
3. Membuat prototype aplikasi berbasis web (Streamlit) yang dapat digunakan institusi untuk memasukkan data mahasiswa dan mendapatkan prediksi risiko dropout secara real-time.
4. Membuat business dashboard untuk memonitor performa akademik dan faktor-faktor risiko mahasiswa.

### Persiapan

Sumber data: Dataset performa mahasiswa Jaya Jaya Institut (`data.csv`)

Setup environment:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Business Dashboard
Business Dashboard dibuat menggunakan Metabase. Dashboard ini mencakup metrik-metrik penting seperti distribusi status mahasiswa (Graduate, Dropout, Enrolled), serta korelasi performa akademik (misal persetujuan mata kuliah di semester 1 dan 2) terhadap tingkat dropout. Dashboard dirancang untuk memudahkan manajemen Jaya Jaya Institut dalam memonitor kesehatan performa akademik mahasiswa secara keseluruhan.
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
Dari analisis data dan pemodelan, didapatkan kesimpulan sebagai berikut:
1. **Performa Akademik adalah Kunci**: Mahasiswa yang gagal mendapatkan persetujuan pada mata kuliah (Curricular Units Approved) di semester 1 dan 2 memiliki tingkat dropout yang sangat tinggi.
2. **Kondisi Finansial Berpengaruh Besar**: Status hutang (Debtor) dan pembayaran uang kuliah (Tuition fees up to date) sangat berkorelasi dengan risiko putus sekolah. Mahasiswa yang telat membayar atau memiliki hutang lebih rentan dropout.
3. **Usia Pendaftar**: Mahasiswa yang mendaftar di usia yang lebih tua cenderung memiliki risiko dropout lebih tinggi dibandingkan lulusan sekolah menengah baru.
4. **Performa Model**: Model prediksi (Random Forest) dapat mendeteksi risiko dropout secara otomatis berdasarkan input user.

### Rekomendasi Action Items
Berdasarkan kesimpulan, berikut adalah rekomendasi action items yang harus dilakukan Jaya Jaya Institut:
- **Program Bimbingan Akademik Dini**: Wajibkan bimbingan dan kelas perbaikan intensif bagi mahasiswa yang gagal atau mendapat nilai buruk di paruh pertama Semester 1.
- **Bantuan dan Konseling Finansial Dini**: Berikan opsi cicilan pembayaran atau beasiswa ringan bagi mahasiswa yang terindikasi mulai menunggak uang kuliah sebelum mereka terpaksa dropout karena alasan biaya.
- **Monitoring Khusus untuk Mahasiswa Non-Reguler/Lebih Tua**: Sediakan program adaptasi dan dukungan penyusunan jadwal belajar khusus untuk mahasiswa yang mendaftar di usia yang lebih matang, mengingat mereka seringkali memiliki kesibukan ganda (misal bekerja).
