#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 06:48:04 2020

@author: sandeepthakur
"""


a="sandeeP is good"
b="ready for split"
c=42
d="sandeep"
if(a.startswith("j")):
    print("yes")
print(a[2:5])

#replace whitespaces at begining and end
print(a.strip())
print(a.lower())
print(a.upper())

#-1 suggests replace all occurence
print(a.replace("e", "a", -1))
print(b.split(" "))

#does only one split
print(b.split(" ", 1))

print("eeP" in a)
print("eep" not in a)

print(a+b)
print(a+ " *** "+b)

toConcatenate = "my name is {}. I am {} yr old"
print(toConcatenate.format(d, c))

a="hello12"
a=a.capitalize()
print(a.capitalize())
print(a)
print(a.isnumeric())
print(a.replace("e", "o"))