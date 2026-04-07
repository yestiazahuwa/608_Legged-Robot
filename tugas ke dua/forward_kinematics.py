import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L = [50, 40, 30] 
fig, ax = plt.subplots(figsize=(6,6))
line, = ax.plot([], [], 'o-', lw=5, color='blue', markerfacecolor='orange')
ax.set_xlim(-130, 130); ax.set_ylim(-130, 130)
ax.grid(True)

def update(frame):
    # Sudut berubah seiring waktu (frame)
    t1 = 45 * np.sin(frame * 0.05)
    t2 = 60 * np.cos(frame * 0.08)
    t3 = 30 * np.sin(frame * 0.1)
    
    rad1, rad2, rad3 = np.radians([t1, t2, t3])
    
    x = [0, 
         L[0]*np.cos(rad1), 
         L[0]*np.cos(rad1) + L[1]*np.cos(rad1+rad2), 
         L[0]*np.cos(rad1) + L[1]*np.cos(rad1+rad2) + L[2]*np.cos(rad1+rad2+rad3)]
    y = [0, 
         L[0]*np.sin(rad1), 
         L[0]*np.sin(rad1) + L[1]*np.sin(rad1+rad2), 
         L[0]*np.sin(rad1) + L[1]*np.sin(rad1+rad2) + L[2]*np.sin(rad1+rad2+rad3)]
    
    line.set_data(x, y)
    ax.set_title(f"FK Bergerak: T1={t1:.1f}°, T2={t2:.1f}°")
    return line,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()