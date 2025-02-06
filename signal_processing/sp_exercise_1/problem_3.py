import numpy as np
import matplotlib.pyplot as plt

# Define the range for n (2 cycles)
n = np.arange(0, 32)  # 0 ≤ n ≤ 31 (2 cycles for the slowest frequency)

# Define the sinusoidal sequences
x_a = 2 * np.cos((np.pi / 8) * n)              # x[n] = 2 * cos(π/8 * n)
x_b = 2 * np.cos((np.pi / 8) * n - np.pi / 2)    # x[n] = 2 * cos(π/8 * n - π/2)
x_c = 2 * np.sin((np.pi / 8) * n)                # x[n] = 2 * sin(π/8 * n)
x_d = 2 * np.cos((np.pi / 8) * n + np.pi / 2)    # x[n] = 2 * cos(π/8 * n + π/2)
x_e = 2 * np.cos((np.pi / 4) * n)                # x[n] = 2 * cos(π/4 * n)
x_f = 2 * np.cos(np.pi * n)                      # x[n] = 2 * cos(π * n)
x_g = 2 * np.cos((7 * np.pi / 4) * n)            # x[n] = 2 * cos(7π/4 * n)
x_h = 2 * np.cos((15 * np.pi / 4) * n)           # x[n] = 2 * cos(15π/4 * n)
x_i = 2 * np.cos(2 * np.pi * n)                  # x[n] = 2 * cos(2π * n)

# ---------------------------
# Page 1: First 5 Sequences
# ---------------------------
fig1 = plt.figure(figsize=(18, 18))
fig1.suptitle('Sinusoidal Sequences - Page 1', fontsize=20)

# Plot for x[n] = 2 * cos(π/8 * n)
ax1 = fig1.add_subplot(3, 2, 1)
ax1.stem(n, x_a, basefmt=" ")
ax1.set_title(r'$x[n] = 2 \cdot \cos\left(\frac{\pi}{8} n\right)$')
ax1.set_xlabel('n')
ax1.set_ylabel('Amplitude')
ax1.grid(True)

# Plot for x[n] = 2 * cos(π/8 * n - π/2)
ax2 = fig1.add_subplot(3, 2, 2)
ax2.stem(n, x_b, basefmt=" ")
ax2.set_title(r'$x[n] = 2 \cdot \cos\left(\frac{\pi}{8} n - \frac{\pi}{2}\right)$')
ax2.set_xlabel('n')
ax2.set_ylabel('Amplitude')
ax2.grid(True)

# Plot for x[n] = 2 * sin(π/8 * n)
ax3 = fig1.add_subplot(3, 2, 3)
ax3.stem(n, x_c, basefmt=" ")
ax3.set_title(r'$x[n] = 2 \cdot \sin\left(\frac{\pi}{8} n\right)$')
ax3.set_xlabel('n')
ax3.set_ylabel('Amplitude')
ax3.grid(True)

# Plot for x[n] = 2 * cos(π/8 * n + π/2)
ax4 = fig1.add_subplot(3, 2, 4)
ax4.stem(n, x_d, basefmt=" ")
ax4.set_title(r'$x[n] = 2 \cdot \cos\left(\frac{\pi}{8} n + \frac{\pi}{2}\right)$')
ax4.set_xlabel('n')
ax4.set_ylabel('Amplitude')
ax4.grid(True)

# Plot for x[n] = 2 * cos(π/4 * n)
ax5 = fig1.add_subplot(3, 2, 5)
ax5.stem(n, x_e, basefmt=" ")
ax5.set_title(r'$x[n] = 2 \cdot \cos\left(\frac{\pi}{4} n\right)$')
ax5.set_xlabel('n')
ax5.set_ylabel('Amplitude')
ax5.grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# ---------------------------
# Page 2: Remaining 4 Sequences
# ---------------------------
fig2 = plt.figure(figsize=(18, 18))
fig2.suptitle('Sinusoidal Sequences - Page 2', fontsize=20)

# Plot for x[n] = 2 * cos(π * n)
ax6 = fig2.add_subplot(2, 2, 1)
ax6.stem(n, x_f, basefmt=" ")
ax6.set_title(r'$x[n] = 2 \cdot \cos\left(\pi n\right)$')
ax6.set_xlabel('n')
ax6.set_ylabel('Amplitude')
ax6.grid(True)

# Plot for x[n] = 2 * cos(7π/4 * n)
ax7 = fig2.add_subplot(2, 2, 2)
ax7.stem(n, x_g, basefmt=" ")
ax7.set_title(r'$x[n] = 2 \cdot \cos\left(\frac{7\pi}{4} n\right)$')
ax7.set_xlabel('n')
ax7.set_ylabel('Amplitude')
ax7.grid(True)

# Plot for x[n] = 2 * cos(15π/4 * n)
ax8 = fig2.add_subplot(2, 2, 3)
ax8.stem(n, x_h, basefmt=" ")
ax8.set_title(r'$x[n] = 2 \cdot \cos\left(\frac{15\pi}{4} n\right)$')
ax8.set_xlabel('n')
ax8.set_ylabel('Amplitude')
ax8.grid(True)

# Plot for x[n] = 2 * cos(2π * n)
ax9 = fig2.add_subplot(2, 2, 4)
ax9.stem(n, x_i, basefmt=" ")
ax9.set_title(r'$x[n] = 2 \cdot \cos\left(2\pi n\right)$')
ax9.set_xlabel('n')
ax9.set_ylabel('Amplitude')
ax9.grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()