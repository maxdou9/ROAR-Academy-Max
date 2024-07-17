## This is course material for Introduction to Python Scientific Programming
## Example code: widget_lasso_cursor.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
from matplotlib.widgets import LassoSelector, Cursor

fig1 = plt.figure(0)           # Create Figure 0
ax1 = plt.gca()               # Get Current Axes function - gca stands for this
ax1.set_xlim([-10, 0])
ax1.set_ylim([-10, 10])

def onSelect(x):
	print(x) # retunrs the values of da poitns :3

lasso = LassoSelector(ax=ax1, onselect=onSelect) # creates lasso with axis 1, 

fig2 = plt.figure(1)           # Create another Figure 1
ax2 = plt.gca()                # Get Current Axes function
ax2.set_xlim([0, 10])
ax2.set_ylim([-10, 10])

cursor = Cursor(ax2,
				horizOn=True, # Controls the visibility of the horizontal line that moves w/ your cursor
				vertOn=True,  # Controls the visibility of the vertical line that moves w/your cursor
				color='green', # the lines are green
				linewidth=2.0 # the lines are 2 wide
				)

def onclick(event):
	[x1, y1] = [event.xdata, event.ydata]
	print(x1, y1) # returns x1 and y1
	plt.plot(x1,y1, 'ro') # plots
	fig2.canvas.draw_idle()
    
fig2.canvas.mpl_connect('button_press_event', onclick) # calls the onclick function during the 'button press even'

plt.show()