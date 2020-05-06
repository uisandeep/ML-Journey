#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:39:50 2020

@author: sandeepthakur
"""


'''
By default, a function must be called with the correct number of arguments.
'''

'''
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly.
'''

def this_function(*cups):
    print("number of cups are: "+ cups[0])
    
this_function("one")

#You can also send arguments with the key = value syntax

def my_function(cup1, cup2, cup3):
    print("cup3 is: "+ cup3)
    print("cup2 is: "+ cup2)
    print("cup1 is: "+ cup1)
    
my_function(cup1="small", cup2="medium", cup3="big")

'''If you do not know how many keyword arguments that will be passed 
into your function, add two asterisk: ** before the parameter.
This way the function will receive a dictionary of arguments. '''

def my_function(**cups):
    print("big cup is: "+ cups["big"])

my_function(big = "cup1", medium = "cup2", small = "cup3")

'''
Default parameter value.
If we call the function without argument, it uses the default value
'''
def my_function(country = "Norway"):
  print("I am from " + country)
  
my_function("India")
my_function()

#passing list to functions
def my_function(food):
    for x in food:
        print(x)
        
my_function(["apple", "banana", "cherry"])

#Recursive functions
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
        