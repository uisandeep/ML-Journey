#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 06:45:48 2020

@author: sandeepthakur
"""


#classes and objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunction(self):
        print("Hello myname is: "+ self.name)
        
p1 = Person("sandeep thakur", 40)
p1.myfunction();        

#self has to be the first parameter of any function

