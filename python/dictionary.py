#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:20:53 2020

@author: sandeepthakur
"""


thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1980}

print(thisdict)

#access using key
print(thisdict["model"])
print(thisdict.get("model"))

thisdict["year"] = 2000
#print(thisdict)

for x in thisdict:
    print(x) # this will print keys
    print(thisdict.get(x))# this will print values
    
for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
  print(x, y)

print(len(thisdict))

#item manipulation
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("model") #definite item
print(thisdict)
thisdict.popitem() #random item
print(thisdict)
del thisdict["brand"]#removes the item with key color
print(thisdict)

#copy a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
copydict=thisdict.copy()
testdict=dict(thisdict)
print(copydict)
print(testdict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily.get("child1"))
print(myfamily.values())
print(myfamily.items())
print(myfamily.keys()) #returns keys as tuples
