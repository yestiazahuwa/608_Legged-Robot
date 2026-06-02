# 🦾 Inverse Kinematics Planar Robot 3-DOF menggunakan Pendekatan ML & DL

Repositori ini berisi implementasi penyelesaian masalah **Inverse Kinematics (IK)** pada robot planar 3-DOF (*Degree of Freedom*) menggunakan pendekatan **Machine Learning (Supervised)** dan **Deep Learning (PyTorch MLP)**. Proyek ini dikembangkan untuk memenuhi Tugas Praktikum Kinematika dan Kontrol Robot.

---

## 📌 Deskripsi Tugas Praktikum
1. **Pembaruan Dimensi Robot:** Mengubah panjang link robot menjadi konfigurasi baru:  
   $$L_1 = 0.5\text{ m}, \quad L_2 = 0.4\text{ m}, \quad L_3 = 0.3\text{ m}$$
   
   Sehingga jangkauan maksimum baru robot adalah **$\text{MAX\_REACH} = 1.2\text{ m}$**.
3. **Optimasi Metode Machine Learning:** Mengganti dan mengoptimalkan model bawaan standar (KNN & Random Forest) dengan metode regresi non-linear modern (**SVR** & **Gradient Boosting**).

---

## 🗺️ Visualisasi Workspace & Geometri Robot

Setelah dimensi link diperbarui, ruang kerja (*workspace*) robot melebar menjadi radius lingkaran maksimal 1.2 meter. Fungsi keselamatan dinamis juga disematkan untuk membedakan area yang dapat dijangkau (*reachable*) dan area luar yang mustahil digapai.

<p align="center">
  <img src="image/Workspace Robot Planar 3-DOF.png" width="31%" alt="Workspace Robot">
  <img src="image/Fungsi Reachability Check.png" width="31%" alt="Reachability Check">
  <img src="image/Demo Visualisasi Robot.png" width="31%" alt="Visualisasi Postur Lengan">
</p>
<p align="center"><em>Gambar 1: Analisis Geometri Robot (Kiri: Jangkauan Workspace, Tengah: Batas Uji Reachability, Kanan: Postur Lengan Robot 3-DOF)</em></p>

---

## 🧠 Metode & Arsitektur Optimasi

### 1. Support Vector Regression (SVR)
Menggunakan **SVR dengan RBF Kernel** dalam `MultiOutputRegressor`. Model ini sangat unggul dalam memetakan fungsi trigonometri kontinu pada sendi tanpa mengalami lompatan nilai (*discrete jumps*).

### 2. Gradient Boosting (HistGradientBoosting)
Algoritma *boosting* modern berbasis histogram yang sangat cepat dan efisien. Mampu mempelajari data non-linear dengan waktu komputasi hitungan detik.

### 3. Deep Learning (IKNet MLP via PyTorch)
Membentuk jaringan saraf tiruan *Multi-Layer Perceptron* (MLP) dengan fungsi loss khusus di ruang Cartesian (**Differentiable FK**). Konvergensi model terpantau turun secara stabil melalui kurva latihan berikut:

<p align="center">
  <img src="image/Training Curve — Deep Learning (IKNet).png" width="65%" alt="Training Curve IKNet">
</p>
<p align="center"><em>Gambar 2: Kurva Penurunan MSE Loss pada Model Deep Learning</em></p>

---

## 📊 Hasil Evaluasi & Perbandingan Metode

Berikut adalah grafik komparasi performa error antara model Machine Learning baru (SVR vs HistGB) serta grafik batang dan histogram distribusi sebaran error dari seluruh metode setelah diuji menggunakan *test set*:

<p align="center">
  <img src="image/Perbandingan Error End-Effector — Metode ML Baru.png" width="31%" alt="Error Model ML Baru">
  <img src="image/Perbandingan Akurasi IK Baru — ML vs DL.png" width="31%" alt="Bar Chart Perbandingan">
  <img src="image/Analisis Distribusi Error End-Effector — Semua Metode Baru.png" width="31%" alt="Histogram Distribusi Error">
</p>
<p align="center"><em>Gambar 3: Analisis Komparasi Akurasi Akhir (Kiri: Scatter Error ML, Tengah: Batang Rata-rata Error, Kanan: Histogram Distribusi Frekuensi Error)</em></p>

### Ringkasan Karakteristik Metode
| Kondisi Target | Rekomendasi Metode | Karakteristik Utama |
| :--- | :--- | :--- |
| Dataset besar tersedia, butuh training instan | **Gradient Boosting (HistGB)** | Waktu training tercepat (hitungan detik), sangat ringan. |
| Butuh prediksi sudut yang halus & kontinu | **SVR (Support Vector Regression)** | Prediksi transisi pergerakan sendi sangat halus. |
| Butuh akurasi fisis tertinggi di ruang koordinat | **Deep Learning (IKNet MLP)** | Meminimalkan error *End-Effector* hingga skala milimeter. |
| Kontrol *real-time* di hardware rendah | **SVR / Gradient Boosting** | Inferensi instan, cocok untuk Jetson Nano / Raspberry Pi. |

---

## 🎬 Animasi Gerakan Robot (Trajectory Tracking)

Ketika diuji untuk mengikuti lintasan melingkar (*circular trajectory*), model berhasil memprediksi perubahan sudut secara harmonis dan presisi mengejar target titik merah secara real-time:

[[video src="Animasi Gerakan Robot.mp4"]]

<p align="center"><em>Gambar 4: Animasi Gerakan Model Deep Learning Mengikuti Lintasan Target</em></p>
