## This is course material for Introduction to Python Scientific Programming
## Example code: plot_3D.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

z_line = np.linspace(0, 15, 1000) # z acts as the radius - it goes from small to big and produces a spiral
x_line = np.cos(z_line)*z_line
y_line = np.sin(z_line)*z_line
ax.plot3D(x_line, y_line, z_line, 'gray')

z_points = 15 * np.random.random(100)
x_points = np.cos(z_points)*z_points + 1 * np.random.randn(100) # adds random noise around the line
y_points = np.sin(z_points)*z_points + 1 * np.random.randn(100)
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv') # color values are using the z as colors

plt.show()