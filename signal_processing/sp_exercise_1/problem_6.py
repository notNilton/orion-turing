import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Define the input sequence x[n]
# x[n] = 3δ[n+2] + 4δ[n] - 2δ[n-3]
# Nonzero values occur at n = -2, 0, and 3.
# We define x[n] over n from -2 to 3.
# ---------------------------
n_x = np.arange(-2, 4)  # n from -2 to 3 (inclusive)
x = np.zeros(len(n_x))
x[0] = 3    # δ[n+2]: when n = -2, value = 3
x[2] = 4    # δ[n]: when n = 0, value = 4 (n = 0 corresponds to index 2)
x[5] = -2   # δ[n-3]: when n = 3, value = -2 (n = 3 corresponds to index 5)

# ---------------------------
# Define the impulse response h[n]
# h[n] = δ[n] + 0.5δ[n-1] + 0.25δ[n-2]
# Nonzero values occur at n = 0, 1, and 2.
# ---------------------------
n_h = np.arange(0, 3)  # n = 0, 1, 2
h = np.array([1, 0.5, 0.25])

# ---------------------------
# Evaluate the convolution y[n] = x[n] * h[n]
# The convolution result will be defined from:
#   n_min = min(n_x) + min(n_h) = -2 + 0 = -2
#   n_max = max(n_x) + max(n_h) = 3 + 2 = 5
# ---------------------------
y = np.convolve(x, h)
n_y = np.arange(n_x[0] + n_h[0], n_x[-1] + n_h[-1] + 1)  # n from -2 to 5

# ---------------------------
# Plot the sequences
# ---------------------------
plt.figure(figsize=(12, 10))

# Plot x[n]
plt.subplot(3, 1, 1)
plt.stem(n_x, x, basefmt=" ")
plt.title('Input Sequence x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot h[n]
plt.subplot(3, 1, 2)
plt.stem(n_h, h, basefmt=" ")
plt.title('Impulse Response h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot y[n]
plt.subplot(3, 1, 3)
plt.stem(n_y, y, basefmt=" ")
plt.title('Output Sequence y[n] = x[n] * h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
