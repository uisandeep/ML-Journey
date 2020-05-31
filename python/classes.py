#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 06:45:48 2020

@author: sandeepthakur
"""

#Classes
class Customer:
    def __init__(self,custId,custName):
        self.custId=custId
        self.custName=custName
    def display_details(self):
        print(self.custId)
        print(self.custName)
    def calculate_Amount(self,interest,year):
        pass
class Regular_Customer(Customer):
    def __init__(self,custId,custName,amount,custType):
        self.custId=custId
        self.custName=custName
        self.amount=amount
        self.custType=custType
    def calculate_Amount(self,interest,year):
        final_amount=self.amount+(self.amount*interest*year)/100.0
        if (self.custType=='Regular'):
            return final_amount
        elif(self.custType=='Privilege'):
            return final_amount-200
class Privilege_Customer(Customer):
    def __init__(self,custId,custName,amount,custType):
        self.custId=custId
        self.custName=custName
        self.amount=amount
        self.custType=custType
    def calculate_Amount(self,interest,year):
        final_amount=self.amount+(self.amount*interest*year)/100.0
        final_amount=final_amount-200  # Due to being priviledged customer
        if (self.custType=='Regular'):
            return final_amount
        elif(self.custType=='Privilege'):
            return final_amount-200
Regular_1=Regular_Customer(101,'Smith',5000,'Regular')
Privilege_1=Privilege_Customer(102,'Alan',5000,'Privilege')
print(Regular_1.calculate_Amount(10,2))
print(Privilege_1.calculate_Amount(10,2))
print("-------------------------------------------------")

#classes and objects 1. Variable scopes
global_var = 10
class Person:
    local_var = 20
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunction(self):
        print("Hello myname is: "+ self.name)
        self.local_var+=1
        print(self.local_var)
        print(global_var) #global variable so accessed anywhere.
p1 = Person("sandeep thakur", 40)
p1.myfunction();     
print(global_var) #global variable so accessed anywhere.  

#print(local_var) This cannot be accessed here as it is class local
#To access here you should instantiate the class.

print(p1.local_var) #prints 21 as it was modified by the p1 object.
print(Person.local_var) #prints 20

Person.local_var = 25
print(p1.local_var) #still prints 21
print(Person.local_var) # will print 25
print("-------------------------------------------------")


#classes and objects 2. (Important Concept Application)
class Edureka:
    x=10
    def method_1(self,x):
        x=20
        print(x) # This will print the local variable x which is local to method_1
        print(self.x) # This will print x which is local to class i.e. 10
        print(id(x)) # It will print the memory address of local x for method.
        print(id(self.x)) # It will print the memory address of local x for class
        x+=1
edureka = Edureka()
edureka.method_1(15)
print(edureka.x)
print(Edureka.x)
edureka.x=25
print(Edureka.x)
print(edureka.x)
print(id(Edureka.x))
print(id(edureka.x))
        
print("-------------------------------------------------")

#classes and objects 3. Public, Protected and Private Attributes
class Edureka:
    def __init__(self):
        self.__pri=("Iam private")
        self._pro=("Iam protected")
        self.pub=("Iam public")
ob=Edureka()
print(ob.pub)
print(ob._pro)
print("-------------------------------------------------") 
        
#classes and objects 3. Class Variable and Instance Variable
class Employee:
    domain="data" #Class Variable
    def __init__(self):
        self.empId = 100 #Instance Variable
obj1 = Employee()
obj1.domain="Big"
obj1.empId=101
obj2=Employee()
print(obj1.domain) #domain is a class variable, so it is not recommended to access by object
print(obj1.empId)
Employee.domain="small"
print(obj2.domain)
print(obj2.empId)
print(obj1.domain) #this will still be obj1's copy so Big
print(obj1.empId)

print("---Important---")
#Class variable should not be accessed using object, if we do that then it will become an instance variable for that object
print(obj1.__dict__)
print(obj2.__dict__) 

print("-------------------------------------------------") 

class Employee:
    _domain="Data"
    def __init__(self):
        self.empId=100
obj1=Employee()
obj1.domain="Big"
obj1.empId=101
obj2=Employee()
print(obj1._domain)
print(obj1.empId)
print(obj2._domain)
print(obj2.empId)

print("-------------------------------------------------") 

class Date:
    temp = 'data'
    def __init__(self, year, month, day): #year-month-day
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def dmy(cls, day, month, year): #day-month-year    
        cls.year = year   
        cls.month = month 
        cls.day = day 
        # #order of return should be same as init
        return cls(cls.year, cls.month, cls.day)  
a = Date(2016, 12, 11)
b = Date.dmy(9, 10, 2018)

print(a.year)
print(b.year)

print("-------------------------------------------------") 

































