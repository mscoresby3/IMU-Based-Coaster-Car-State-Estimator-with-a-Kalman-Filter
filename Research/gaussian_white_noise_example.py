import numpy as np
import matplotlib.pyplot as plt

# 1. Setup parameters
mean = 0
std_dev = 1
num_samples = 5000

# 2. Generate the noise (The "Random Picks")
noise_data = np.random.normal(mean, std_dev, num_samples)

# 3. Create a range of X values for our manual curve
x = np.linspace(-4, 4, 100)

# 4. Calculate the Bell Curve manually (The Gaussian formula)
# Standard math: 1 / (std * sqrt(2 * pi)) * exp(-0.5 * ((x - mean) / std)**2)
bell_curve = (1 / (std_dev * np.sqrt(2 * np.pi))) * \
             np.exp(-0.5 * ((x - mean) / std_dev)**2)

# 5. Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Time plot
ax1.plot(noise_data, color='dodgerblue', linewidth=0.3)
ax1.set_title('Gaussian White Noise (Individual Picks)')

# Histogram + Manual Curve
ax2.hist(noise_data, bins=50, density=True, alpha=0.6, color='gray')
ax2.plot(x, bell_curve, color='red', linewidth=2, label='Manual Gaussian Formula')
ax2.set_title('Distribution of Picks vs. Theoretical Bell Curve')
ax2.legend()

plt.tight_layout()
plt.show()
