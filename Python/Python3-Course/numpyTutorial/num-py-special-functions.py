#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:37:48 2018

@author: soza
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

y = np.cos(x)

plt.plot(x, y)
plt.show()

# you can use tan and other geometric functions

# ---------------------------------------------------------
# e**x exponential function and logx - logarithmic function
# ---------------------------------------------------------

ar = np.array([1, 2, 3])
print(np.exp(ar))
# [ 2.71828183  7.3890561  20.08553692] - the exponential for each element

print(np.log10(ar))
# [0.         0.30103    0.47712125]  - log 10 for each element

print(np.log(ar))
# [0.         0.69314718 1.09861229] - log to be base e


# ----------------------------------------------------------------------------
# Data Visualization - nothing be a graphical or a pictorial representation of
# the data.
# It is used to understand the trend better and present it to non technical
# users. It allows us to quickly interpret the data and adjust different
# variables to see its effect.
# Visualize --> Analyse --> Document Insights --> Transform Data set -->
# Visualize
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# MatPlotLib is a package for creating different types of plots/graphs - Bar,
# Histograms, Scatter Plots, Pie Plot, Hexagonal Bin Plot, Area Plot.
#
# ----------------------------------------------------------------------------

# ----------------------
# Line Graph basic plot
# ----------------------

x = [5, 8, 10]
y = [12, 16, 6]

plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")

plt.show()

# Above graph is pretty boring - use style from matplotlib to add grid, color
# etc.

style.use("ggplot")
x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.plot(x, y, 'g', label = "line 1", linewidth = 5)
plt.plot(x2, y2, 'c', label = "line 2", linewidth = 5)

plt.title("Better Line Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.legend()
plt.grid(True, color = 'k')
plt.show()

# --------------
# Bar Graph Plot
# --------------

plt.bar([1,3, 5, 7, 9], [5, 2, 7, 8, 2], label = "Bar 1", color = 'b')
plt.bar([2,4,6,8, 10], [8,6,2,5,6], label = "Bar 2", color = 'g')
plt.legend()
plt.title("Bar Graph")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.show()

# ---------
# Histogram
# ---------

pop_ages = [22, 55, 62, 45, 21, 34, 42, 4, 99, 102, 110, 120, 121, 130, 111, 
            112, 115, 80, 75, 65, 54, 44, 43, 42, 48 ]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(pop_ages, bins, histtype = 'bar', rwidth = 0.8, color = 'b')
plt.legend()
plt.title("HistoGram")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.show()

# ------------
# Scatter Plot
# ------------

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x,y, label = 'scitcat', color = 'g', s = 25, marker = "o")
plt.legend()
plt.title("Scatter Plot")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.show()

# -----------------------
# Area Plot or Stack Plot
# -----------------------

days = [1, 2, 3, 4, 5]
sleeping = [7,8,6,11,7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8,5, 7, 8, 13]

plt.plot([], [], label = "Sleeping", linewidth = 5, color = 'm')
plt.plot([], [], label = "Eating", linewidth = 5, color = 'c')
plt.plot([], [], label = "Working", linewidth = 5, color = 'r')
plt.plot([], [], label = "Playing", linewidth = 5, color = 'k')

plt.stackplot(days, sleeping, eating, working, playing, 
              colors = ['m', 'c', 'r', 'k'])


plt.title("Stack/Area Plot")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.legend()
plt.show()


# ---------
# Pie Chart
# ---------

slices = [7, 2, 2, 13]
activities = ["sleeping", "eating", "working", "playing" ]
cols = ['c', 'm', 'r','k']
plt.pie(slices, labels = activities, colors = cols, startangle = 90, 
        shadow = True, explode = (0, 0.1, 0, 0), 
        autopct = '%1.1f%%')
plt.title("Pie Chart")
plt.show()

# --------------
# Multiple plots
# --------------

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# 211 - 2 means we have 2 plots virtiacally and 1 plot horizontal, this is
# our first plot
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2* np.pi * t2))
plt.show()

# if sub plot is changed to 221 then you will see 2 plot next to each other
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(222)
plt.plot(t2, np.cos(2* np.pi * t2))
plt.show()


