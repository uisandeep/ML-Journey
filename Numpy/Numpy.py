#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:33:42 2020

@author: sandeepthakur
"""


#Array Creation

import numpy as np

#from a regular Python list or tuple using the array function

a = np.array([2,3,4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
print("-------------------------------------------------")
'''
The function zeros creates an array full of zeros, the function ones creates 
an array full of ones, and the function empty creates an array whose 
initial content is random and depends on the state of the memory. 
By default, the dtype of the created array is float64.
'''

print(np.zeros((3,4)))
print(np.ones( (2,3,4), dtype=np.int16 ))
print("-------------------------------------------------")

#To create sequences of numbers, NumPy provides a function analogous to range 
#that returns arrays instead of lists.
print(np.arange( 10, 30, 5 ))

#linspace that receives as an argument the number of elements that we want.
print(np.linspace( 0, 2, 9 ))
print("-------------------------------------------------")

#printing Arrays
a = np.arange(6)  
print(a)

b = np.arange(12).reshape(4,3)
print(b)

c = np.arange(24).reshape(2,3,4)  
print(c)
print("-------------------------------------------------")

#Basic operations.
a = np.array([20,30,40,50])
b = np.arange(4)
print(b)
print("a-b", a-b)
print("a*b", a*b)
print("a+b", a+b)
print(10*np.sin(a))
print(a<35)
print("-------------------------------------------------")
# unary operations
a = np.array([20,30,40,50])
print(a.sum()) # 140
print(a.min()) # 20
print(a.max()) # 50
#By default, these operations apply to the array as though it were a list of numbers, 
#regardless of its shape.
print("-------------------------------------------------")
#by specifying the axis parameter you can apply an operation along the specified axis of an array:
b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))     # sum of each column [12 15 18 21]
print(b.min(axis=1))     # min of each row [0 4 8]
print(b.cumsum(axis=1)) # cumulative sum along each row
print("-------------------------------------------------")
# check universal functions like sqroot, 
print("-------------------------------------------------")
# Indexing, Slicing and Iterating¶
a = np.arange(10)**3   #[  0,   1,   8,  27,  64, 125, 216, 343, 512, 729] cube of each number
print(a)

print(a[2])
print(a[2:5]) #[ 8 27 64]
for i in a:
    print(i)
for i in a:
    print(i**(1/3.0))
print("-------------------------------------------------")
#Shape manipulateion
a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.shape)

print(a.ravel()) # returns a flat array one dimension  [9. 9. 7. 1. 0. 4. 7. 3. 0. 8. 7. 4.]
b = np.array([9., 9., 7., 1., 0., 4., 7., 3., 0. ,8., 7.,4.])
print(b.reshape(6,2))
print("-------------------------------------------------")

#File IO
#Read file data.txt which is in same directory as this file.
age, num_children,num_pets = np.loadtxt("numeric_data.txt", skiprows=1, unpack=True)
print(age)
print(num_children)
print(num_pets)
