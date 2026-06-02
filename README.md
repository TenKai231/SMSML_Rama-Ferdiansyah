# Credit Scoring Model with MLflow

Proyek ini bertujuan untuk membangun dan melacak model Machine Learning untuk klasifikasi **Credit Scoring** menggunakan `scikit-learn` dan `MLflow`.

## Struktur Proyek

- `modelling.py`: Script utama untuk melatih model Random Forest Classifier dengan MLflow tracking.
- `modellingopt.py`: Script untuk melakukan optimasi hyperparameter (Grid Search sederhana) dan mencatat hasilnya ke MLflow.
- `train_pca.csv` & `test_pca.csv`: Dataset yang digunakan (hasil dari proses PCA).
- `mlruns/`: Direktori tempat MLflow menyimpan hasil eksperimen, parameter, dan model (artifacts).
- `.gitignore`: Mengabaikan file yang tidak perlu seperti venv, cache, dan data MLflow.

## Persiapan Lingkungan

1. Pastikan Anda memiliki Python terinstal.
2. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   # venv\Scripts\activate     # Untuk Windows
   ```
3. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan

### 1. Pelatihan Model Standar
Jalankan perintah berikut untuk melatih model dengan parameter default atau berikan argumen sendiri:
```bash
python modelling.py [n_estimators] [max_depth]
```
Contoh:
```bash
python modelling.py 100 10
```

### 2. Optimasi Model
Jalankan perintah berikut untuk mencari hyperparameter terbaik:
```bash
python modellingopt.py
```

### 3. Melihat Hasil Eksperimen (MLflow UI)
Untuk melihat visualisasi dari hasil training dan perbandingan model, jalankan:
```bash
mlflow ui
```
Lalu buka browser dan akses `http://127.0.0.1:5000`.

## Catatan
Kode ini dikonfigurasi untuk menyimpan data secara lokal di folder `mlruns/`. Jika ingin menggunakan server MLflow terpusat, ubah `mlflow.set_tracking_uri()` pada file `.py` terkait.
# Belajar_MLops-
# SMSML_Rama-Ferdiansyah
