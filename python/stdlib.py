#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 07:46:30 2020

@author: sandeepthakur
"""


'''standard libraries'''

import math
print(dir(math))

#import individual libraries
from math import sqrt
from math import tan
print(sqrt(25))
print(tan(90))

from math import * #import all libraries
print(sqrt(25))
print(tan(90))



#sys module
import sys
print(sys.argv)
#print(sys.exit())

import sys
print(not sys)     # Returns False if module is imported, else True
print(sys.flags)   # Returns the struct sequence flags and exposes the status of command line flags
print(sys.prefix)  # Returns a string giving the site-specific directory prefix where the platform independent Python files are installed

for elem in sys.path:
    print(elem)  # This will print the paths where python searches the modules

# In case if you want to add any path to this list, you can use append function
sys.path.append("x")
for elem in sys.path:
    print(elem)
    
#print(sys.flags)
print(sys.prefix)

import os
print(os.name) # Returns the name of the operating system dependent module imported
#print(os.environ)
print(os.getppid()) # Return the parent’s process id

#Random Module
import random
print(random.randint(100, 500))
print(random.randrange(0,100, 5)) # Return a randomly selected element from range(start, stop, step)

print(random.uniform(6,2)) # Return a random integer N such that a <= N <= b

import datetime
from datetime import timedelta
now = datetime.datetime.today()
other = datetime.datetime(1995, 3, 12, 22, 10)
print(other)
print(now-other)

print(type(now))
print(str(now))
futuredate = now + timedelta(days=1095)
print(futuredate)

print(datetime.MAXYEAR)  # Returns the largest year number allowed in a date or datetime object. MAXYEAR is 9999

print(datetime.MINYEAR)  # Returns the smallest year number allowed in a date or datetime object. MINYEAR is1

print(datetime.time)    # Returns a time object with hour, minute, second and microsecond

print(datetime.timezone)  # Returns a timezone object

#JSON module
import json
data = {'name':'smith', 'age':30}
print(type(data))
json_str = json.dumps(data) #converting to json
print(json_str)
original = json.loads(json_str) #back to dict
print(original)
print(type(original))



