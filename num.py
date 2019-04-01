#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created On: 2019-04-01 14:32:54

@Author: Hodonou SOUNTON (drxos), MSc IR

Description: Learning numpy
"""


import numpy as np

#  Create a rank 1 array
# a = np.array([0, 1, 2])
# print(type(a))

# print(a.shape)
# print(a[0])
# print(a[1])
# print(a[2])

# #  a[0] <-- 5
# a[0] = 5
# print(a)

# Create a rank 2 array
# b = np.array([
#     [0, 1, 2], 
#     [3, 4, 5]
# ])
# print(b.shape)
# print(b)
# print(b[1, 2])

# # Create a 3x3 array of all zeros
# a = np.zeros((3,3))
# print(a)

# # Create a 3x3 array of all ones
# a = np.ones((3,3))
# print(a)

# # Create a 3x3 constant array
# a = np.full((3,3), 7)
# print(a)

# # Create a 3x3 array filled with random values
# a = np.random.random((20,4))
# print(a)

# # Create a 3x3 identy matrix
# a = np.eye(3)
# print(a)

# Convert list to array
a = [1, 2, 3, 4, 5]
print(a)
a = np.array(a)
print(a)

a = np.arange(20)
print(a)