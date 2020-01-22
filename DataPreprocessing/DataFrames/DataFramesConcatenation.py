
"""
Created on Wed Jan 22 13:27:03 2020

@author: sptom
"""

import pandas as pd
import numpy as np 

df1 = pd.DataFrame()
ID = [1001,1002,1003,1004]
Name = ['Virat Kohli','Susan Whistler','Michael Scoefield','Sarah Wilson']
Gender = ['Male','Male','Male','Female']
Country = ['India','Australia','England','Canada']


df1['ID'] = ID
df1['Name'] = Name
df1['Gender'] = Gender
df1['Country'] = Country

df2 = pd.DataFrame()
ID = [2001,2002,2003,2004]
Name = ['Ramos Djavedi','Sanjeev Walia','Sneha Chowdhurry','Lincoln Burrows']
Gender = ['Male','Male','Female','Male']
Country = ['US','India','Qatar','Canada']


df2['ID'] = ID
df2['Name'] = Name
df2['Gender'] = Gender
df2['Country'] = Country


######################### Concatenation #######################################

df3 = pd.concat([df1,df2],axis=0)

df4 = pd.concat([df1,df2],axis=1)

new_record = pd.Series([3001,'Steve Waugh','Male','Australia'],index=['ID','Name','Gender','Country'])


# Append 
df5 = df3.append(new_record,ignore_index=True)
