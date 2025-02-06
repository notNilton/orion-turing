import numpy as np
import matplotlib.pyplot as plt

# Define the range for n
n = np.arange(0, 21)  # 0 ≤ n ≤ 20

# Impulse sequence (delta function)
impulse_sequence = np.where(n == 0, 1, 0)  # 1 at n=0, 0 elsewhere

# Unit step sequence (Heaviside function)
unit_step_sequence = np.where(n >= 0, 1, 0)  # 1 for n ≥ 0, 0 otherwise

# Plotting the impulse sequence
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(n, impulse_sequence, basefmt=" ")  # Removed use_line_collection
plt.title('Impulse Sequence (δ[n])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotting the unit step sequence
plt.subplot(2, 1, 2)
plt.stem(n, unit_step_sequence, basefmt=" ")  # Removed use_line_collection
plt.title('Unit Step Sequence (u[n])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()