#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:18:32 2020

@author: sandeepthakur
"""


x = "Hello1"
y = 15

''' This will return true most of times.
but only for empty or 0 it will return a false
for list tuples if empty then false
'''
print(bool(x))
print(bool(y))

print(bool(""))
print(bool(0))
bool(())
bool([])
bool({})




