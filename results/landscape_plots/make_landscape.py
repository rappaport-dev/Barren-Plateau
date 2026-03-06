import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

filename = "XYC_z0z1_0.8_0.npy"

X,Y,C = np.load("XYC_z0z1_0.8_0.npy")

original_size = np.asarray([7/3,1.5])
scale = 3.5/2

plt.rcParams.update({"font.family":"sans-serif",
                 "font.serif": ["Computer Modern Serif"]})

# Plotting no measurements 
fig = plt.figure()
fig.set_size_inches(original_size[0]*scale,original_size[1]*scale)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, C, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.yaxis.set_tick_params(labelsize=9)
ax.xaxis.set_tick_params(labelsize=9)
ax.set_zticks([1,0,-1, -2])
#ax.view_init(30, -60, 0)
plt.savefig(f'landscape_{filename}.pdf',transparent=True, dpi=500)  