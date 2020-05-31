#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:57:34 2020

@author: sandeepthakur
"""


# Example 1   
# Although x and y are two different variables, it will have same memory addess
x=20
y=20
print(id(x))
print(id(y))
print("-----------------------------------------------------")

# Example 2
# The address is not going to be same for lists.
list1=[1,2,3]
list2=[1,2,3]
tuple1=(1,2,3)
list3=list(tuple1)
print(id(list1))
print(id(list2))
print(id(list3))
print(id(tuple1))

print("-----------------------------------------------------")
# Example 3
# Local vs Global Variable

a=100  # This is global variable a
def func_8():
    a=200   # This is local variable a
    print(a)
    print(id(a))  # This is the memory address of local variable a
func_8()
print(a)
print(id(a)) # This is the memory address of global variable a
print("-----------------------------------------------------")

# Example 4
# Local vs Global Variable
# I want to modify the gloabl variable inside a function. What should I do?
a=100  # This is global variable a
def func_8():
    global a
    a=200   # This is now global variable a
    print(a)
    print(id(a))  # This is the memory address of global variable a
func_8()
print(a)
print(id(a)) # This is the memory address of global variable a
print("-----------------------------------------------------")

# Example 5
# In this code, by writing global a before the value assignment line, we have made the behaviour of a to be global. So it is
# accessible outside
def func_9():
    global a
    a=199
func_9()
print(a)
print("-----------------------------------------------------")

c=100
def func_10():
    c=200
    print(c) #prints local
    global d
    d = 100
    print(id(d))
func_10()
print(c) #prints global  
print(id(c)) 

print("-----------------------------------------------------")


print("-----------------------------------------------------")