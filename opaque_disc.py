import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simulation Parameters ---

# Normalize intensity relative to background
wavelength = 632.8e-9    # Red He-Ne Laser (632.8 nm)
disk_radius = 1.0e-3     # Opaque disc radius (1.0 mm)
z = 1.0                  # Distance from obstacle to screen (1.0 meter)

N = 4096               # Grid resolution (2048x2048)
L = 10.0e-3              # Physical size of domain (10 mm x 10 mm)
dx = L / N               # Spatial step size

# --- 2. Coordinate Grid & Incident Field ---
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# Uniform plane wave incident on the opaque disc (1 where R > radius, 0 inside)
u_in = np.where(R > disk_radius, 1.0, 0.0)

# --- 3. Angular Spectrum Propagation (FFT) ---
# Spatial frequencies
fx = np.fft.fftfreq(N, d=dx)
fy = np.fft.fftfreq(N, d=dx)
FX, FY = np.meshgrid(fx, fy)

# Wavevector magnitude
k = 2 * np.pi / wavelength

# Free-space propagation transfer function H(fx, fy)
kz = np.sqrt(k**2 - (2*np.pi*FX)**2 - (2*np.pi*FY)**2 + 0j)
H = np.exp(1j * kz * z)

# Propagate via FFT
U_in = np.fft.fft2(u_in)
U_out = np.fft.ifft2(U_in * H)
intensity = np.abs(U_out)**2

#Normalize intensity relative to background
I_0 = 1.0  # Since u_in was 1.0 outside the disc
intensity_normalized = intensity / I_0

# --- 4. Plotting Results ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Intensity Map
im = ax1.imshow(intensity_normalized, extent=[-L*1e3/2, L*1e3/2, -L*1e3/2, L*1e3/2], cmap='inferno')
ax1.set_title('Diffraction Pattern (Arago Spot)')
ax1.set_xlabel('x (mm)')
ax1.set_ylabel('y (mm)')
plt.colorbar(im, ax=ax1, label='Normalized Intensity')

# 1D Cross-section
center_line = intensity_normalized[N // 2, :]
ax2.plot(x * 1e3, center_line, color='black', linewidth=1.5)
ax2.set_title('Central Intensity Profile')
ax2.set_xlabel('x (mm)')
ax2.set_ylabel('Intensity')
ax2.grid(True)

plt.tight_layout()
plt.show()