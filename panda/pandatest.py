#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:51:59 2020

@author: sandeepthakur
"""


import pandas as pd

#data frame
df = pd.read_csv('data.csv')
print(df)
print("-------------------------------------------------")
_dict = {'name': 'John' , "age": 23, "state": 'TX'}
people = pd.Series(_dict)
print(people)
print("-------------------------------------------------")
#creating a df using a series and array
_data = {'name': pd.Series(['John' ,'Mary', 'Peter']), "age": [23, 17, 67]}
df = pd.DataFrame(_data)
print(df)
print(df.shape)
print(df.size)
print("-------------------------------------------------")

print("to get data from first 2 rows.-----------------------------")
print(df.iloc[0:2])

print("to get age where age is greater than 19.-----------------------------")
_data = {'name': pd.Series(['John' ,'Mary', 'Peter']), "age": [23, 17, 67]}
df = pd.DataFrame(_data)

print(df[df['age']>19])

print("-------------------------To print a single value in iteration")
for row in df:
    print(df[row])
    
print("-------------------------sort by age")
print(df.sort_values(["age"]))
   
print("--------------------group by")
_data = {'name': pd.Series(['John' ,'Mary', 'Peter']),"state":['TX', 'TX','WA'], "age": [23, 17, 67]}
df = pd.DataFrame(_data)
df_state = df.groupby(df["state"])
print(df_state.groups.keys())

print("----printing data from Excel file")
movies_df = pd.read_excel("movies.xls")
print(movies_df)
print(movies_df.shape) # 1338 rows and 25 columns
print(movies_df.size)
print(movies_df.duplicated())
print(movies_df.drop_duplicates())

print("after dropping duplicates", movies_df.shape)

#Series
print("-------------------------------------------------")

people_ages = pd.Series([23, 78, 22, 19, 45, 33])
print(people_ages)

