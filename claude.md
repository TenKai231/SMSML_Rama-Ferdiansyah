Setiap kriteria dapat bernilai 0 sampai 4 _points_ (pts). Untuk lulus dari submission ini, Anda **harus mendapatkan 2 points dari setiap kriteria**. Submission akan **ditolak** jika masih terdapat kriteria dengan 0 points. 

|   |
|---|
|**_WAJIB DIPERHATIKAN!_**<br><br>Mohon periksa tab “Lainnya” untuk memeriksa ketentuan pengiriman submission lebih lanjut.|

  

### Kriteria 1: Melakukan Eksperimen terhadap Dataset Pelatihan

Kriteria pertama merupakan senjata utama untuk menyelesaikan submission kelas ini. Hal ini sangat berguna sebagai eksplorasi dan eksperimen awal sebelum Anda melakukan otomatisasi pada kriteria berikutnya.

Pada tahap ini, Anda **wajib** menggunakan [**Template Eksperimen MSML**](https://colab.research.google.com/drive/1vSTQWWgGqPGBGHvv8lbeGdoa5N92D_UC?usp=sharing) sebagai panduan awal sebelum membuat file untuk melakukan otomatisasi data preprocessing. Pastikan template tersebut diikuti dengan benar untuk memastikan proses berjalan sesuai standar yang ditetapkan. 

Setelah melakukan eksplorasi, Anda telah memiliki panduan utama untuk membuat file yang dapat melakukan preprocessing data secara otomatis. Selanjutnya, silakan konversi langkah-langkah yang ada pada notebook eksperimen untuk membuat file otomatisasi tersebut.

Pada akhirnya agar dapat memenuhi kriteria ini, Anda harus membuat sebuah repository (GitHub dan lokal) dengan struktur seperti ini.

Eksperimen_SML_Nama-siswa
├── .workflow (jika menerapkan advance)
├── namadataset_raw (bisa berupa file atau folder)
├── preprocessing
    └── Eksperimen_Nama-siswa.ipynb
    └── automate_Nama-siswa.py (jika menerapkan skilled)
    └── namadataset_preprocessing (bisa berupa file atau folder)

Berikut adalah penilaian lengkap untuk kriteria 1:

- **Reject (0 pts)**
    
    - Tidak melakukan seluruh tahapan experimentation yang ada pada template secara manual. 
        
    - Tidak melakukan data loading pada notebook. 
        
    - Tidak melakukan EDA pada notebook.
        
    - Tidak melakukan preprocessing pada notebook.
        
- **Basic (2 pts)**
    
    - Melakukan tahapan experimentation secara manual.
        
    - Melakukan data loading pada notebook.
        
    - Melakukan EDA pada notebook.
        
    - Melakukan preprocessing pada notebook.
        
- **Skilled (3 pts)**
    
    - Tahap _basic_ terpenuhi.
        
    - Membuat sebuah file automate_Nama-siswa.py yang berisikan fungsi untuk melakukan preprocessing secara otomatis sehingga mengembalikan data yang siap dilatih.
        
        - Pada tahap ini Anda harus melakukan konversi dari proses eksperimen sebelumnya, sehingga tahapannya harus sama tetapi memiliki struktur yang berbeda.
            
- **Advance (4 pts)**
    
    - Tahap _skilled_ terpenuhi.
        
    - Membuat sebuah workflow pada GitHub Actions agar dapat melakukan preprocessing setiap kali trigger terpantik.
        
        - Anda harus membuat sebuah repository dengan nama Eksperimen_SML_Nama-siswa berisi seluruh file yang sama dengan rekomendasi struktur folder pada kriteria 1.
            
        - Pastikan Actions yang dibuat mengembalikan sebuah dataset terbaru yang sudah diproses sedemikian rupa.
            

  

### Kriteria 2: Membangun Model Machine Learning

Setelah selesai melalui tahapan preprocessing, Anda harus melatih model menggunakan dataset yang sudah siap digunakan (bukan raw). Nantinya Anda harus membuat sebuah folder yang berisikan file **modelling.py** beserta _dependencies_ nya dengan struktur seperti berikut.

Membangun_model
├── modelling.py
├── modelling_tuning.py (jika menerapkan skilled/advanced)
├── namadataset_preprocessing (bisa berupa file atau folder)
├── screenshoot_dashboard.jpg
├── screenshoot_artifak.jpg
├── requirements.txt
├── DagsHub.txt (berisikan tautan DagsHub jika menerapkan advanced)

Sebagai informasi, tahapan ini dapat Anda jalankan pada lokal environment sebagai jembatan penghubung ke kriteria tiga.

Berikut adalah penilaian lengkap untuk kriteria 2:

- **Reject (0 pts)**
    
    - Tidak membuat model machine learning/deep learning menggunakan MLflow dan menyimpan artefak di MLflow Tracking UI.
        
    - Tidak menyimpan informasi apa pun pada logging.
        
- **Basic (2 pts)**
    
    - Melatih model machine learning (Scikit-Learn) menggunakan MLflow Tracking UI yang disimpan secara lokal tanpa menggunakan hyperparameter tuning.
        
    - Menggunakan autolog dari MLflow pada file modelling.py.
        
    - Mengirimkan screenshot yang valid.
        
- **Skilled (3 pts)**
    
    - Kriteria Basic wajib terpenuhi.
        
    - Melatih model machine learning/deep learning menggunakan MLflow Tracking UI yang disimpan secara lokal dengan menerapkan hyperparameter tuning.
        
    - Alih-alih menggunakan autolog, Anda diharapkan menggunakan manual logging dengan metriks yang sama dengan autolog.
        
        - Pastikan kamu melakukan checklist ini pada file modelling_tuning (bukan pada modelling.py)
            
- **Advance (4 pts)**
    
    - Melatih model machine learning/deep learning menggunakan MLflow Tracking UI yang disimpan secara online dengan DagsHub.
        
    - Alih-alih menggunakan autolog, siswa diharapkan menggunakan manual logging dengan metriks yang tidak hanya tercover pada autolog (autolog + minimal 2 artefak tambahan).
        

  

### Kriteria 3: Membuat Workflow CI

Setelah membuat dan memastikan file **modelling.py** berjalan dengan baik, selanjutnya Anda harus membuat workflow CI menggunakan MLflow Project agar dapat melakukan re-training model secara otomatis ketika trigger dipantik. 

Silakan Anda buat sebuah project repository baru di GitHub dengan struktur seperti berikut ini.

Workflow-CI
├── .workflow
├── MLProject (folder)
    └── modelling.py
    └── conda.yaml
    └── MLProject
    └── namadataset_preprocessing (bisa berupa file atau folder)
    └── Tautan ke Docker Hub
    └── (file tambahan jika diperlukan)

Anda dapat menggunakan file **modelling.py****, conda.yaml** serta dataset yang sudah siap dilatih dari hasil eksperimen sebelumnya. Pada tahap ini, Anda hanya perlu membuat struktur yang diminta beserta file MLProjectnya saja. Namun, tidak menutup kemungkinan Anda harus menyesuaikan file modelling.py ketika masuk ke tahap ini.

Berikut adalah penilaian lengkap untuk kriteria 3:

- **Reject (0 pts)**
    
    - Tidak membuat folder MLProject.
        
    - Tidak membuat workflow CI menggunakan GitHub Actions.
        
- **Basic (2 pts)**
    
    - Membuat folder MLProject.
        
    - Membuat Worflow CI yang dapat membuat model machine learning ketika trigger terpantik.
        
- **Skilled (3 pts)**
    
    - Membuat workflow CI dan menyimpan artefak ke suatu repositori (GitHub yang sama atau Google Drive).
        
- **Advance (4 pts)**
    
    - Membuat workflow CI dan menyimpan artefak ke suatu repositori (GitHub yang sama atau Google Drive) serta membuat Docker Images ke Docker Hub menggunakan fungsi mlflow build-docker.
        

  

### Kriteria 4: Membuat Sistem Monitoring dan Logging

Monitoring dan Logging merupakan tahapan yang tidak bisa berdiri sendiri karena membutuhkan artefak yang dihasilkan oleh kriteria tiga. Nantinya, Anda hanya akan mengumpulkan tangkapan layar mengenai skill yang diampu dengan struktur seperti berikut ini.

Monitoring dan Logging
├── 1.bukti_serving
├── 2.prometheus.yml
├── 3.prometheus_exporter.py
├── 4.bukti monitoring Prometheus (folder)
    └── 1.monitoring_<metriks>
    └── 2.monitoring_<metriks>
    └── dst (sesuaikan dengan poin yang diraih)
├── 5.bukti monitoring Grafana (folder)
    └── 1.monitoring_<metriks>
    └── 2.monitoring_<metriks>
    └── dst (sesuaikan dengan poin yang diraih)
├── 6.bukti alerting Grafana (folder)
    └── 1.rules_<metriks>
    └── 2.notifikasi_<metriks>
    └── 3.rules_<metriks>
    └── 4.notifikasi_<metriks>
    └── dst (sesuaikan dengan poin yang diraih)
├── 7.inference.py
├── folder/file tambahan

**Penting**, pastikan untuk membuat dashboard dengan nama **username akun Dicoding** sehingga tangkapan layar yang Anda kirimkan akan berisikan kredensial.

Berikut adalah penilaian lengkap untuk kriteria 4:

- Reject (0 pts)
    
    - Tidak melakukan serving model pada environment local.
        
    - Tidak melakukan monitoring performa sistem machine learning menggunakan Prometheus
        
    - Tidak menggunakan Grafana sebagai tools visualisasi dan alerting sistem machine learning
        
- Basic (2 pts)
    
    - Melakukan serving model baik itu melalui artefak yang sudah dibuat atau pull Images (jika menerapkan kriteria CI untuk melakukan push ke Docker Hub)
        
        - Bisa melalui mlflow model serve, mlflow deployments, atau pull images jika memenuhi kriteria 3 advanced.
            
    - Melakukan monitoring menggunakan Prometheus minimal dengan tiga metriks yang berbeda.
        
    - Melakukan monitoring menggunakan Grafana dengan metriks yang sama dengan Prometheus.
        
- Skilled (3 pts)
    
    - Melakukan monitoring menggunakan Grafana dengan minimal 5 metriks yang berbeda.
        
    - Membuat satu alerting menggunakan Grafana.
        
- Advance (4 pts)
    
    - Melakukan monitoring menggunakan Grafana dengan minimal 10 metriks yang berbeda.
        
    - Membuat tiga alerting menggunakan Grafana.


### Perhitungan Nilai

Nilai akhir yang Anda dapatkan diperoleh melalui perhitungan formula berikut.

![[Pasted image 20260603014303.png]]

|   |
|---|
|**Catatan:**<br><br>Perhitungan nilai akhir di atas digunakan apabila setiap kriteria mendapatkan nilai 2 pts atau tidak ada kriteria yang ditolak.|

  

### Tabel Penilaian

Adapun untuk penilaian submission dapat dilihat pada tabel berikut.

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|**Ketentuan Penilaian**|   |   |   |   |   |
|**Nilai Akhir**|**Nilai Dicoding**|**Nilai Huruf**|**Level of Mastery**|**Makna Nilai**|**Keterangan**|
|<1|Rejected|E|-|Tidak Lulus|Anda sudah mencoba, tetapi belum memenuhi kompetensi minimal.|
|1 — <2|Bintang 2|D|Below Basic|Kurang|Anda sudah memenuhi semua kompetensi minimal, tetapi terdapat area yang masih bisa ditingkatkan.|
|2 — <3|Bintang 3|C|Basic|Cukup|Anda sudah memenuhi semua kompetensi minimal dari _learning objective_.|
|3 — <4|Bintang 4|B|Skilled|Mahir|Anda sudah memenuhi semua kompetensi dengan baik atau mahir.|
|4|Bintang 5|A|Advanced|Tingkat Lanjut|Anda sudah memenuhi semua kompetensi dengan sangat baik atau tingkat lanjut.|

### Ketentuan Pengiriman Berkas Submission

- Berkas submission yang dikirimkan merupakan folder berisi kumpulan berkas yang diminta **dalam bentuk ZIP** seperti contoh berikut.
    
    SMSML_Nama-siswa.zip
    ├── Eksperimen_SML_Nama-siswa.txt
    ├── Membangun_model
        ├── modelling.py
        ├── modelling_tuning.py (skilled/advanced)
        ├── namadataset_preprocessing (bisa berupa file atau folder)
        ├── screenshoot_dashboard.jpg
        ├── screenshoot_artifak.jpg
        ├── requirements.txt
        ├── DagsHub.txt (berisikan tautan DagsHub jika menerapkan advanced)
    ├── Workflow-CI.txt
    ├── Monitoring dan Logging
        ├── 1.bukti_serving
        ├── 2.prometheus.yml
        ├── 3.prometheus_exporter.py
        ├── 4.bukti monitoring Prometheus (folder)
            └── 1.monitoring_<metriks>
            └── 2.monitoring_<metriks>
            └── dst (sesuaikan dengan poin yang diraih)
        ├── 5.bukti monitoring Grafana (folder)
            └── 1.monitoring_<metriks>
            └── 2.monitoring_<metriks>
            └── dst (sesuaikan dengan poin yang diraih)
        ├── 6.bukti alerting Grafana (folder)
            └── 1.rules_<metriks>
            └── 2.notifikasi_<metriks>
            └── 3.rules_<metriks>
            └── 4.notifikasi_<metriks>
            └── dst (sesuaikan dengan poin yang diraih)
        ├── 7.Inference.py
        ├── folder/file tambahan
    
    Pastikan Anda **tidak melakukan ZIP dalam ZIP**.

  

### Ketentuan Submission Ditolak

Submission Anda akan ditolak bila

- Setiap kriteria submission tidak terpenuhi
    
    - Kriteria 1
        
        - Tidak menggunakan template sebagai struktur dasar notebook.
            
        - Tidak melakukan tahapan experimentation secara manual. 
            
        - Tidak melakukan data loading pada notebook.
            
        - Tidak melakukan EDA pada notebook.
            
        - Tidak melakukan preprocessing pada notebook.
            
    - Kriteria 2
        
        - Tidak membuat model machine learning menggunakan MLflow dan menyimpan artefak di MLflow Tracking UI.
            
        - Tidak menyimpan informasi apa pun pada logging.
            
    - Kriteria 3
        
        - Tidak membuat folder MLProject.
            
        - Tidak membuat workflow CI menggunakan GitHub Actions.
            
    - Kriteria 4
        
        - Tidak melakukan serving model pada environment local.
            
        - Tidak menggunakan username dicoding sebagai nama dashboard.
            
        - Tidak melakukan monitoring performa sistem machine learning menggunakan Prometheus.
            
        - Tidak menggunakan Grafana sebagai tools visualisasi dan alerting sistem machine learning.
            
- Mengirimkan tautan kriteria 1 dan 3 tetapi dengan visibilitas **Private** pada pengaturan GitHub.
    
- Ketentuan berkas submission tidak terpenuhi.
    
- Melakukan kecurangan, seperti tindakan plagiasi.
    

  

### Ketentuan Proses Review

Beberapa hal yang perlu Anda ketahui mengenai proses review:

- Tim Reviewer akan mengulas submission Anda dalam waktu **selambatnya 3 (tiga) hari kerja** (tidak termasuk Sabtu, Minggu, dan hari libur nasional).
- Tidak disarankan untuk melakukan submit berkali-kali karena akan memperlama proses penilaian




Kalau cuma **2 hari**, lupakan dulu target **Advanced**. Fokus **lulus dengan aman** atau maksimal **Skilled di beberapa bagian**.

Dari requirement yang kamu upload, yang paling penting adalah **jangan ada kriteria yang dapat 0**.

## Strategi 2 Hari

### Hari 1 (8–12 jam)

#### Kriteria 1 (Eksperimen)

Target: 3 poin

- Selesaikan notebook EDA
    
- Data loading
    
- Missing value
    
- Encoding
    
- Scaling
    
- Simpan dataset preprocessing
    
- Buat `automate_rama.py`
    

Output:

```text
Eksperimen_Rama.ipynb
automate_Rama.py
dataset_clean.csv
```

---

#### Kriteria 2 (Model)

Target: 2 poin

Karena waktu mepet.

Buat:

```text
modelling.py
requirements.txt
```

Pakai:

```python
mlflow.autolog()
```

Train model.

Ambil screenshot:

- Dashboard MLflow
    
- Artifacts
    

Kalau sempat baru buat:

```text
modelling_tuning.py
```

untuk naik ke 3 poin.

---

### Hari 2 (8–12 jam)

#### Kriteria 3 (CI)

Target: 2 poin

Buat:

```text
MLProject
conda.yaml
GitHub Actions
```

Workflow sederhana:

```text
push
↓
install requirements
↓
python modelling.py
```

Tidak perlu Docker Hub dulu.

---

#### Kriteria 4 (Monitoring)

Target: 2 poin

Ini yang paling penting.

##### 1. Serve model

Kamu sudah berhasil:

```bash
mlflow models serve ...
```

dan sudah dapat:

```json
{"predictions":[2]}
```

Berarti langkah ini hampir selesai.

---

##### 2. Prometheus

Buat 3 metric saja:

```python
request_count
latency
prediction_count
```

---

##### 3. Grafana

Dashboard:

```text
request_count
latency
prediction_count
```

Screenshot.

---

##### 4. Alert

Buat 1 alert sederhana:

```text
Latency > 1 detik
```

Screenshot rule.

---

# Prioritas Super Penting

Kalau waktunya benar-benar mepet:

## Wajib Selesai

✅ Notebook EDA

✅ automate.py

✅ modelling.py + MLflow

✅ MLProject

✅ GitHub Actions

✅ Serve model

✅ Prometheus

✅ Grafana

---

## Boleh Dikorbankan

❌ DagsHub

❌ Docker Hub otomatis

❌ 10 metrics monitoring

❌ 3 alerting

❌ Workflow preprocessing otomatis GitHub Actions

❌ Advanced CI/CD

---

Menurutku, dengan kemampuanmu sekarang (sudah bisa MLflow, serving model, curl, Linux, Git), **2 hari masih sangat mungkin untuk lulus submission ini**. Yang perlu dijaga adalah jangan terlalu lama ngulik tool baru. Fokus checklist requirement satu per satu. Jangan salah paham ya! Aku bukan khawatir kamu gagal atau apa... aku cuma tidak mau kamu membuang waktu di bagian yang tidak menambah poin. (￣ヘ￣)