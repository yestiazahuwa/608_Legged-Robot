"# 608_Legged-Robot" 
TENTANG FORWARD KINEMATIC

LINK VIDEO NYA : https://drive.google.com/file/d/1432yO2Vf-sxcNc2wNYx6MlIYj9GvFJHY/view?usp=drive_link


## Cara Menjalankan Simulasi
1. Pastikan sudah menginstal Python.
2. Instal library yang dibutuhkan: `pip install numpy matplotlib`
3. Jalankan kode: `python simulasi.py`





## TUGAS MINGGU KE DUA 

Planar Kinematics: 3-Link Manipulator 🦾
Repositori ini berisi simulasi robot lengan dengan 3 sendi (3-Join Planar) menggunakan bahasa pemrograman Python. Project ini mencakup implementasi Forward Kinematics dan Inverse Kinematics berdasarkan prinsip trigonometri dan aturan cosinus.

📝 Konsep DasarSistem ini terdiri dari tiga lengan (link) dengan panjang $L_1, L_2,$ dan $L_3$. Posisi ujung lengan (end-effector) ditentukan oleh sudut dari masing-masing sendi ($\theta_1, \theta_2, \theta_3$).

1. Forward Kinematics (FK) ➡️Forward Kinematics adalah proses menghitung koordinat $(x, y)$ dari ujung lengan jika sudut setiap sendi diketahui.Rumus Matematis:Posisi $x$ dan $y$ dihitung dengan menjumlahkan proyeksi setiap link:1. Forward Kinematics (FK) ➡️Forward Kinematics adalah proses menghitung koordinat $(x, y)$ dari ujung lengan jika sudut setiap sendi diketahui.Rumus Matematis:Posisi $x$ dan $y$ dihitung dengan menjumlahkan proyeksi setiap link:
   
               $$x = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2) + L_3 \cos(\theta_1 + \theta_2 + \theta_3)$$$$y = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2) + L_3 \sin(\theta_1 + \theta_2 + \theta_3)$$


2. Inverse Kinematics (IK) ⬅️Inverse Kinematics adalah proses mencari besar sudut $(\theta_1, \theta_2, \theta_3)$ yang diperlukan agar ujung lengan mencapai titik target $(x, y)$ tertentu.Metode Perhitungan (Aturan Cosinus):Dalam project ini, digunakan Aturan Cosinus untuk memecahkan sudut pada segitiga yang terbentuk antar link (seperti yang terdapat pada catatan teknis):Menentukan Posisi Joint 2: Jika sudut orientasi akhir ($\phi$) ditentukan, kita cari titik sebelum link terakhir.
Mencari $\theta_2$:$$\cos(\theta_2) = \frac{x^2 + y^2 - L_1^2 - L_2^2}{2 L_1 L_2}$$Mencari $\theta_1$: Menggunakan fungsi atan2 untuk mendapatkan sudut terhadap sumbu horizontal.
