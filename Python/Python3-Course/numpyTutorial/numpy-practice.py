#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:20:14 2018

@author: soza
"""
import numpy as np

# Print numpy version and configuration
print(np.__version__)
np.show_config()

# Create a null vector is size 10 set 5 element as 1
a = np.zeros(10)
a[4] = 1
print(a)

# Create a vector of values from 10 to 49
a = np.arange(10, 50)
print(a)

# Reverse a vector
a = a[::-1]
print(a)

# Create a 3x3 matrix with values ranging from 0 to 8
a = np.arange(9).reshape(3, 3)
print(a)

# Find non zero indicies in [1, 2, 0, 0, 4, 0, 5]
a = np.array([1, 2, 0, 0, 4, 0 , 5])
print(a.nonzero())

# Create a 3x3 matrix
a = np.eye(3)
print(a)