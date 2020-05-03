#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:22:11 2020

@author: sandeepthakur
"""

"""
A tuple is a collection which is ordered and unchangeable. 
In Python tuples are written with round brackets.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry","kiwi", "melon", "mango")
print(thistuple[1])  #
print(thistuple[-1])  #Print the last item of the tuple
print(thistuple[2:5]) #Return the third, fourth, and fifth item
print(thistuple[-4:-1]) #
print(thistuple[1]) #Print the second item in the tuple:
for x in thistuple:
    print(x)
for x in range(0, len(thistuple)):
    print(thistuple[x])
if "apple" in thistuple: #exists
    print("yes1")
print(len(thistuple))

#You cannot add items to a tuple

"""To create a tuple with only one item, you have to add a comma after 
the item, otherwise Python will not recognize it as a tuple."""

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry")
del thistuple #deleted the tuple

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#tuple constructor
thistuple = tuple(("apple", "banana", "cherry1")) # note the double round-brackets
print(thistuple)
