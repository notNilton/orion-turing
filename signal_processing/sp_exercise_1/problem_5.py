import numpy as np
import matplotlib.pyplot as plt

# Define the impulse response h[n]
h = np.array([1, 0.5, 0.25])  # h[n] = δ[n] + 0.5δ[n-1] + 0.25δ[n-2]
h_n = np.arange(0, 3)  # n values for h[n]

# Define the input x[n]
x = np.array([3, 0, 4, 0, 0, -2])  # x[n] = 3δ[n+2] + 4δ[n] - 2δ[n-3]
x_n = np.arange(-2, 4)  # n values for x[n]

# Compute the convolution y[n] = x[n] * h[n]
y = np.convolve(x, h, mode='full')  # Full convolution
y_n = np.arange(x_n[0] + h_n[0], x_n[-1] + h_n[-1] + 1)  # n values for y[n]

# Plotting
plt.figure(figsize=(14, 10))

# Plot h[n]
plt.subplot(3, 1, 1)
plt.stem(h_n, h, basefmt=" ", linefmt='b-', markerfmt='bo')
plt.title('Impulse Response $h[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot x[n]
plt.subplot(3, 1, 2)
plt.stem(x_n, x, basefmt=" ", linefmt='g-', markerfmt='go')
plt.title('Input $x[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot y[n]
plt.subplot(3, 1, 3)
plt.stem(y_n, y, basefmt=" ", linefmt='r-', markerfmt='ro')
plt.title('Output $y[n] = x[n] * h[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()