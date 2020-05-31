#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:52:30 2020

@author: sandeepthakur
"""

thislist = ["apple", "banana", "cherry"]
mylist = thislist.reverse() 
print(thislist)

'''
List is ordered and changeable. square brackets
'''

'''list constructor'''
thislist = list(("apple1", "banana1", "cherry1")) # note the double round-brackets
print(thislist)

'''copying list'''
'''You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, and changes 
made in list1 will automatically also be made in list2.'''

'''thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist, thislist)
#another way
newlist = list(thislist)
print(mylist, newlist)'''

'''Joining list'''
'''list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list1:
    list2.append(x)
print(list2)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
'''


'''thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("yes in the list")
thislist.append("grapes")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("orange")
print(thislist)

#this will remove the last element if no index specified
thislist.pop()
print(thislist)

#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist

#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #this will print []
'''

# Example 8 --- any()
# If any of the element of a sequence is True, it will return True
list4=[10,0,None,False]  # Here, one element is True
print(any(list4))
list5=[0,0,None,False]
print(any(list5))   # Here, all the elements are False

print("--------------------------------------------")
# Example 10 ---- enumerate()
# Return an enumerate object. The Iterable must be a sequence, an iterator, or some other object which supports iteration
# Enumerate returns the list of tuples. Tuples consists index values and items from the list

animals = ['tiger', 'lion', 'deer']
enumerateAnimals = enumerate(animals)
print(type(enumerateAnimals))
# converting to list
print(list(enumerateAnimals))
# changing the default counter
enumerateAnimals = enumerate(animals, 10)
print(list(enumerateAnimals))




'''thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[1])

#-1 refers to last item, -2 second last
print(thislist[-1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#this is bring items from 0 to orange (item no. 3 starting from 0)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#similarly for negatvie indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

newlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon"]
newlist[4] = "sandeep"
print(newlist)

#loops & other operations on list

currentlist = ["new", "item", "in", "list"]
for x in currentlist:
    print(x)
for x in range(0, len(currentlist)):
    print(currentlist[x])'''
    
