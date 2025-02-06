import numpy as np
import matplotlib.pyplot as plt

# Define the range for n
n = np.arange(0, 21)  # 0 ≤ n ≤ 20

# Define the exponential sequences
x_a = 2 * (0.5) ** n  # x[n] = 2 * 0.5^n
x_b = 2 * (1.5) ** n  # x[n] = 2 * 1.5^n
x_c = 2 * (-0.5) ** n  # x[n] = 2 * (-0.5)^n
x_d = 2 * (-1.5) ** n  # x[n] = 2 * (-1.5)^n

# Plotting the sequences
plt.figure(figsize=(14, 10))

# Plot for x[n] = 2 * 0.5^n
plt.subplot(2, 2, 1)
plt.stem(n, x_a, basefmt=" ")
plt.title(r'$x[n] = 2 \cdot 0.5^n$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot for x[n] = 2 * 1.5^n
plt.subplot(2, 2, 2)
plt.stem(n, x_b, basefmt=" ")
plt.title(r'$x[n] = 2 \cdot 1.5^n$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot for x[n] = 2 * (-0.5)^n
plt.subplot(2, 2, 3)
plt.stem(n, x_c, basefmt=" ")
plt.title(r'$x[n] = 2 \cdot (-0.5)^n$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot for x[n] = 2 * (-1.5)^n
plt.subplot(2, 2, 4)
plt.stem(n, x_d, basefmt=" ")
plt.title(r'$x[n] = 2 \cdot (-1.5)^n$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()