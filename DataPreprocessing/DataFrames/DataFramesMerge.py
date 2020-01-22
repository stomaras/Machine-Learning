# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:30:25 2020

@author: sptom
"""

import pandas as pd
import numpy as np 

df1 = pd.DataFrame()
ID = [1001,1002,1003,1004]
Name = ['Virat Kohli','Susan Whistler','Michael Scofield','Sarah Wilson']
Country = ['India','Australia','England','Canada']

df1['ID'] = ID
df1['Name'] = Name
df1['Country'] = Country

df2 = pd.DataFrame()
ID = [1003,1004,2003,2004]
Salary = [20000,15000,25000,18000]

df2['ID'] = ID
df2['Salary'] = Salary


# ON which particular column we want to merge ... So only the records which is common in both this is our like inner join will be displayed 1003 is common in both datasets

df3 = pd.merge(df1,df2,on='ID')

# Now a left outer join how will be execute 



# Full outer join 
df4 = pd.merge(df1,df2,on='ID',how='outer')


# Now if you want to do a left outer join 

df_left = pd.merge(df1,df2,on='ID',how='left')

# Now if you want to do a right outer join 

df_right = pd.merge(df1,df2,on='ID',how='right')


#it is a kind of inner join only 
df5 = pd.merge(df1,df2,left_on='ID',right_on='ID')

