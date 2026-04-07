import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L1, L2, L3 = 50, 40, 30
fig, ax = plt.subplots(figsize=(6,6))
line, = ax.plot([], [], 'o-', lw=5, color='red', markerfacecolor='black')
trail, = ax.plot([], [], 'r--', alpha=0.3)
ax.set_xlim(-130, 130); ax.set_ylim(-130, 130)
ax.grid(True)

hx, hy = [], [] # Untuk jejak lintasan

def solve_ik(tx, ty, phi_deg):
    phi = np.radians(phi_deg)
    x2 = tx - L3 * np.cos(phi)
    y2 = ty - L3 * np.sin(phi)
    dist_sq = x2**2 + y2**2
    c2 = (dist_sq - L1**2 - L2**2) / (2 * L1 * L2)
    c2 = np.clip(c2, -1, 1)
    s2 = np.sqrt(1 - c2**2) # Elbow up
    t2 = np.arctan2(s2, c2)
    t1 = np.arctan2(y2, x2) - np.arctan2(L2*s2, L1 + L2*c2)
    t3 = phi - t1 - t2
    return t1, t2, t3

def update(frame):
    # Target bergerak melingkar
    t = frame * 0.05
    target_x = 60 + 30 * np.cos(t)
    target_y = 40 + 30 * np.sin(t)
    
    try:
        t1, t2, t3 = solve_ik(target_x, target_y, 0)
        
        x = [0, L1*np.cos(t1), L1*np.cos(t1)+L2*np.cos(t1+t2), L1*np.cos(t1)+L2*np.cos(t1+t2)+L3*np.cos(t1+t2+t3)]
        y = [0, L1*np.sin(t1), L1*np.sin(t1)+L2*np.sin(t1+t2), L1*np.sin(t1)+L2*np.sin(t1+t2)+L3*np.sin(t1+t2+t3)]
        
        line.set_data(x, y)
        hx.append(x[-1]); hy.append(y[-1])
        trail.set_data(hx[-50:], hy[-50:]) # Simpan 50 jejak terakhir
        ax.set_title(f"IK Bergerak ke Target: [{target_x:.1f}, {target_y:.1f}]")
    except:
        pass
    return line, trail

ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)
plt.show()