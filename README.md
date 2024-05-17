# Proyek-LabMl-Kelompok4
## Text Classification


### ANGGOTA KELOMPOK
  - Siti Nurrahmasita (2108107010015)
  - Dhaifina Alifa Putri (2108107010018)
  - Rahmatul Idami (2108107010071)
  - Faiza Sabila (2108107010083)
  - Hadija Humaira (2108107010084)
  
### LATAR BELAKANG
Text Classification adalah proses mengkategorikan teks ke dalam kelas atau label tertentu menggunakan model deep learning. Pada dataset ini, terdapat dua kolom: `comment` sebagai variabel X dan `Emotion` sebagai variabel Y dengan tiga kelas emosi yaitu joy, anger, dan fear. Dataset yang berjumlah 5934 baris ini biasanya berformat .csv dan digunakan untuk berbagai kasus seperti analisis sentimen, klasifikasi emosi, analisis umpan balik pelanggan, pemantauan sentimen media sosial, serta pelatihan chatbot dan asisten virtual. 

Implementasi umumnya melibatkan preprocessing teks, tokenisasi, representasi teks dalam bentuk numerik, dan pelatihan model deep learning menggunakan arsitektur sederhana dengan Embedding Layer untuk mempelajari representasi vektor kata, diikuti oleh lapisan-lapisan yang mengurangi dimensi dan lapisan-lapisan Dense untuk memproses representasi tersebut dalam klasifikasi emosi.

Berikut link datasetnya : https://www.kaggle.com/datasets/abdallahwagih/emotion-dataset/data

### Cara Menjalankan Proyek

Ikuti langkah-langkah berikut untuk mengaktifkan lingkungan, menginstal dependensi, dan menjalankan aplikasi Flask.

##### 1. Mengaktifkan Lingkungan Anaconda
Aktifkan lingkungan yang ingin digunakan dengan perintah berikut:
```bash
conda activate namaenv
```
##### 2. Menginstal Library yang Dibutuhkan
Instal library yang dibutuhkan dari file requirements.txt dengan perintah berikut:
```bash
pip install -r requirements.txt
```
##### 3. Menjalankan Aplikasi Flask
Untuk menjalankan aplikasi Flask, jalankan perintah berikut di terminal:
```bash
python app.py
```
