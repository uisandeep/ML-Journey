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
print("--------------------------------------")

#You can also send arguments with the key = value syntax

def my_function(cup1, cup2, cup3):
    print("cup3 is: "+ cup3)
    print("cup2 is: "+ cup2)
    print("cup1 is: "+ cup1)
    
my_function(cup1="small", cup2="medium", cup3="big")
print("--------------------------------------")

'''If you do not know how many keyword arguments that will be passed 
into your function, add two asterisk: ** before the parameter.
This way the function will receive a dictionary of arguments. '''

def my_function(**cups):
    print("big cup is: "+ cups["big"])

my_function(big = "cup1", medium = "cup2", small = "cup3")
print("--------------------------------------")

'''
Default parameter value.
If we call the function without argument, it uses the default value
'''
def my_function(country = "Norway"):
  print("I am from " + country)
  
my_function("India")
my_function()
print("--------------------------------------")

#passing list to functions
def my_function(food):
    for x in food:
        print(x)
        
my_function(["apple", "banana", "cherry"])
print("--------------------------------------")
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
        
print("--------------------------------------")

# Default Argument 
# you can mention a default value for an argument while defining the function. 
# So, even though you don't pass the value for that particular argument
#  while calling the function, it takes the default value. But non-default argument can't be
# written after default argument. Please observe the same error in this code
# Example 9

'''def func_5(age=20,name):
    print('Your age is:', age)
    print('Your name is:', name)
user_age=input('Enter age')
user_name=input('Enter name')
func_5(name=user_name)'''

#To fix the above use this
def func_5(name, age=20):
    print('Your age is:', age)
    print('Your name is:', name)
user_age=30
user_name="sandeep"
func_5(name=user_name)

print("--------------------------------------")
#Variable Length Arguments
def func(arg1, arg2, *arg3):
    print(arg1)
    print(arg2)
    print(arg3)
func(10,20)
func(10,20,30)
func(10,20, 30, 40)
print("--------------------------------------")

# Example 12
# Please check the bug in this code. What is the problem? 
# The problem is that, you shouldn't write any mandatory argument after
# writing variable argument. You can write in one way. For that, 
# check the next code
'''def func_6(arg1,arg2,*arg3,arg4):  
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
func_6(10,20,30)
func_6(10,20,30)'''
print("--------------------------------------")

# Example 15
# Variable keyarguments stored as a dictionary
def func_7(arg1,arg2,*arg3,**keyargs):
    print(arg1)
    print(arg2)
    print(arg3)
    print(str(keyargs))
func_7(10,20,30,40,name='Abhijit',country='India')

print("--------------------------------------")


print("--------------------------------------")


