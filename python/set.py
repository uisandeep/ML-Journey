#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:07:55 2020

@author: sandeepthakur
"""
'''
A set is a collection which is unordered and unindexed. 
In Python sets are written with curly brackets.
No duplicates

'''

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)
print("banana" in thisset) #membership operator

'''Once a set is created you cannot change its items. But you
can add new items or remove'''

thisset.add("orange")
print(thisset)
#add multiple items
thisset = {"apple", "banana", "cherry"}
thisset.update(["grapes", "orange", "mango"])
print(thisset)
print(len(thisset))

thisset.remove("banana")
print(thisset)

#pop will remove last item but because set is unorderred you don't know which item
#got removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear will empty set.
#del will delete the set

#join 2 sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

