import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import sys

sys.path.append("../..")

# Point this to where XYC data is being stored
file_path = "data/XYC_z0z1_0.8_0.npy"

# Extract just the base name (e.g., "XYC_z0z1_0.8_0") to prevent .npy.pdf outputs
base_name = os.path.splitext(os.path.basename(file_path))[0]

# Use the variable directly instead of hardcoding the string twice
X, Y, C = np.load(file_path)

original_size = np.asarray([7 / 3, 1.5])
scale = 3.5 / 2

plt.rcParams.update(
    {
        "font.family": "sans-serif",  # Change to "serif" if Computer Modern isn't rendering
        "font.serif": ["Computer Modern Serif"],
    }
)

# Plotting the landscape
fig = plt.figure()
fig.set_size_inches(original_size[0] * scale, original_size[1] * scale)
ax = plt.axes(projection="3d")

ax.plot_surface(X, Y, C, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.yaxis.set_tick_params(labelsize=9)
ax.xaxis.set_tick_params(labelsize=9)
ax.set_zticks([1, 0, -1, -2])
# ax.view_init(30, -60, 0) # Uncomment and adjust these to change the camera angle

output_filename = f"landscape_{base_name}.pdf"
plt.savefig(output_filename, transparent=True, dpi=500)
plt.close(fig)  # Prevent memory leaks

print(f"Successfully saved {output_filename}")
