import numpy as np
import matplotlib.pyplot as plt

# Define the range for n
n = np.arange(0, 21)  # 0 ≤ n ≤ 20

# Define the sequences
x_a = 5 * (0.5) ** n * np.cos((np.pi / 8) * n)  # x[n] = 5 * 0.5^n * cos(π/8 * n)
x_b = 5 * (1.5) ** n * np.cos((np.pi / 8) * n)  # x[n] = 5 * 1.5^n * cos(π/8 * n)

# Plotting the sequences
plt.figure(figsize=(12, 6))

# Plot for x[n] = 5 * 0.5^n * cos(π/8 * n)
plt.subplot(2, 1, 1)
plt.stem(n, x_a, basefmt=" ")
plt.title(r'$x[n] = 5 \cdot 0.5^n \cdot \cos\left(\frac{\pi}{8} n\right)$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot for x[n] = 5 * 1.5^n * cos(π/8 * n)
plt.subplot(2, 1, 2)
plt.stem(n, x_b, basefmt=" ")
plt.title(r'$x[n] = 5 \cdot 1.5^n \cdot \cos\left(\frac{\pi}{8} n\right)$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()