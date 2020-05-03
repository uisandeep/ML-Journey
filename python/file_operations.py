#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:30:55 2020

@author: sandeepthakur
"""


f = open("testfile.rtf", "r") #open file in write mode
#print(f.read())
print(f.read(5))#read the first 5 characters
print(f.readline())#read one line of the file
#for x in f:
    #print(x)
    
f.close() #always close the file as a good practice

#writing to a file
f = open("testfile.rtf", "a")
f.write("Now the file has more content!")
f.close()
f = open("testfile.rtf", "r")
print(f.read())

'''file modes
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
'''

f = open("testfile.rtf", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("testfile.rtf", "r")
print(f.read())

#To delete a file
import os
if(os.path.exists("abc.txt")):
    os.remove("abc.txt")
else:
    print("file does not exits")
    
#delete a folder
import os
if(os.path.exists("myfolder")):
    os.rmdir("myfolder")
else:
    print("folder does not exits")

