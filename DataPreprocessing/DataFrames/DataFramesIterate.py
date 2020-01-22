# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:07:44 2020

@author: sptom
"""

import pandas as pd 
import numpy as np 

df = pd.DataFrame()

Name = ['Mr Virat Kohli','Mrs Susan Whisler','Mr Michael Scofield','Mrs Sarah Wilson']
Sex = ['Male','Female','Male','Female']
ID = [1001,1002,1003,1004]
Country = ['India','Australia','England','Canada']


df['Name'] = Name
df['ID'] = ID
df['Sex'] = Sex
df['Country'] = Country

for name in df['Name']:
    print(name)
    
# Print Name Column with uppercase
    
for name in df['Name']:
    print(name.upper())
    
    
for name in df['Name'][0:3]:
    print(name.upper())    
    
    
# Now if we want to add the Column with the Uppercase we do the follow steps
    
df['Upper_case'] = df['Name'].apply(lambda x: x.upper())

# Now if we want to print all columns one by one we do the follow steps

for column in df:
    print(df[column])
