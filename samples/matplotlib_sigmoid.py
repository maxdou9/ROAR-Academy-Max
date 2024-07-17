## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_sigmoid.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x) # by passing x into the sigmoid function, it gives a rnage of all values of x

fig = plt.figure() # empty n goes to next new one
ax1 = fig.add_subplot(1, 3, 1) # (h,w, kth subplot)
# Plot without customization
plt.plot(x,sig, linewidth = 3)

ax2 = fig.add_subplot(1, 3, 2)
# Move left y-axis and bottim x-axis to centre
ax2.spines['left'].set_position('center') # moves left axis to center
ax2.spines['bottom'].set_position('center') #moves bottom axis to center
# Eliminate upper and right axes
ax2.spines['right'].set_color('none') # removes right 'axis'
ax2.spines['top'].set_color('none') #removes top 'axis'
# Plot the customized (x-y) axes
plt.plot(x,sig, linewidth = 3)

ax3 = fig.add_subplot(1,3,3)
# Move left y-axis to centre
ax3.spines['left'].set_position('center')
ax3.spines['bottom'].set_position(('data',0)) # sets position respective to data
# Eliminate upper and right axes
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
# Plot the customized (x-y) axes
plt.plot(x,sig,  linewidth = 3)

plt.show()