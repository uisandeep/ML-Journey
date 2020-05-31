#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:14:30 2020

@author: sandeepthakur
"""

import re

str1 = "Python is awesome used for scientific data manipulations"
if(re.search("awesome", str1)):
    print("search found")
else:
    print("search not found")
    
str1 = "Python is awesome. Python also used for scientific data manipulations"
words = re.findall("Python", str1)
print(words)

#patterns
str2 = 'sat, hat, mat, pat'
matches = re.findall('[shmp]at', str2)
print(matches)

str3 = 'sat, hat, mat, pat'
matches = re.findall('[h-m]at', str2)#exclude sat, pat
print(matches)

str3 = 'sat, hat, mat, pat'
matches = re.findall('[^h-m]at', str2)#exclude hat, mat
print(matches)

#Replacing

str3 = 'hat, rat, mat, pat'
regex = re.compile('[r]at')#exclude sat, pat
str3 = regex.sub("tea", str3)
print(str3)

#Phone numbers
phonenumber = "123-234-4565"
if re.search("[0-9]{3}-[0-9]{3}-[0-9]{4}", phonenumber):
    print("valid phone number")
    


