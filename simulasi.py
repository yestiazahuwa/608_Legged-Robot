import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

# Memaksa jendela pop-up di Windows agar interaktif
matplotlib.use('TkAgg') 

# PARAMETER MEKANIK (Sesuai robot Tia)
C, F, T = 21.0, 70.0, 76.8 

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Inisialisasi Link dengan warna berbeda sesuai gambar referensi
# Coxa: Biru, Femur: Hijau, Tibia: Merah
line_coxa, = ax.plot([], [], [], '-', lw=8, color='blue', label='Coxa')
line_femur, = ax.plot([], [], [], '-', lw=8, color='green', label='Femur')
line_tibia, = ax.plot([], [], [], '-', lw=8, color='red', label='Tibia')
joint_markers, = ax.plot([], [], [], 'ko', markersize=10) # Sendi hitam besar

# Jejak lintasan (Trajectory)
trail, = ax.plot([], [], [], 'r--', lw=1, alpha=0.5)
x_hist, y_hist, z_hist = [], [], []

def get_leg_points(tc_deg, tf_deg, tt_deg):
    tc, tf, tt = np.radians([tc_deg, tf_deg, tt_deg])
    p0 = np.array([0, 0, 0])
    p1 = np.array([C * np.cos(tc), C * np.sin(tc), 0])
    Rf = C + F * np.cos(tf)
    p2 = np.array([Rf * np.cos(tc), Rf * np.sin(tc), F * np.sin(tf)])
    Rt = Rf + T * np.cos(tf + tt)
    p3 = np.array([Rt * np.cos(tc), Rt * np.sin(tc), F * np.sin(tf) + T * np.sin(tf + tt)])
    return np.array([p0, p1, p2, p3])

def update(frame):
    # Waktu simulasi
    t = frame * 0.15
    
    # Gerakan Coxa: Menentukan panjang langkah maju-mundur (sumbu X)
    tc_val = 35 * np.cos(t) 
    
    # LOGIKA GERAKAN MELANGKAH (Swing & Stance)
    if np.sin(t) > 0:
        # FASE SWING (Kaki diangkat untuk pindah posisi maju)
        status = "SWING (MELANGKAH)"
        # Femur naik, Tibia menekuk sedikit untuk clearance
        tf_val = 40 + 20 * np.sin(t) 
        tt_val = -40 - 20 * np.sin(t)
    else:
        # FASE STANCE (Kaki menapak datar di lantai untuk mendorong body)
        status = "STANCE (MENUMPU)"
        # Sudut dikunci agar ujung kaki sejajar di lantai
        tf_val = 32 
        tt_val = -32

    # PROSES FORWARD KINEMATICS (Menghitung koordinat dari sudut di atas)
    pts = get_leg_points(tc_val, tf_val, tt_val)
    
    # Update visualisasi garis kaki berwarna
    line_coxa.set_data(pts[0:2, 0], pts[0:2, 1])
    line_coxa.set_3d_properties(pts[0:2, 2])
    
    line_femur.set_data(pts[1:3, 0], pts[1:3, 1])
    line_femur.set_3d_properties(pts[1:3, 2])
    
    line_tibia.set_data(pts[2:4, 0], pts[2:4, 1])
    line_tibia.set_3d_properties(pts[2:4, 2])
    
    joint_markers.set_data(pts[:, 0], pts[:, 1])
    joint_markers.set_3d_properties(pts[:, 2])

    # Update jejak titik merah (Trajectory)
    x_hist.append(pts[3,0]); y_hist.append(pts[3,1]); z_hist.append(pts[3,2])
    if len(x_hist) > 40: x_hist.pop(0); y_hist.pop(0); z_hist.pop(0)
    trail.set_data(x_hist, y_hist)
    trail.set_3d_properties(z_hist)

    # Menampilkan hasil angka koordinat FK pada judul
    ax.set_title(f"Simulasi FK Kaki Tia (Bentuk Mekanik)\n{status} | X={pts[3,0]:.1f}, Z={pts[3,2]:.1f}")
    return line_coxa, line_femur, line_tibia, joint_markers, trail

# Atur tampilan agar tampak samping miring (perspektif)
ax.view_init(elev=20, azim=-60)
ax.set_xlim(-50, 180)
ax.set_ylim(-100, 100)
ax.set_zlim(-150, 50)
ax.legend()

ani = FuncAnimation(fig, update, frames=200, interval=150, blit=False)
plt.show()