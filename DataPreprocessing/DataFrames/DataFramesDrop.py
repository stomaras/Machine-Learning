"""
Created on Wed Jan 22 11:43:16 2020

@author: sptom

Topics to be covered:
    1. Dropping a Single Column of a dataset
    2. Dropping multiple Column of a dataset
    3. Dropping the column of a dataset based on the Column Index
    4. Dropping the Multiple Column of a dataset based on the Column Index
    5. Deleting rows of a Dataset and copying the resultant dataset to a new dataframe
    6. Deleting rows based on index
    7. Drop the Duplicate Values
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part1/tr.csv',delimiter = ';')

# 1.Dropping a Single Column of a dataset based on the column name
df1 = dataset.drop('Name',axis=1)
print(df1.head())


# 2.Dropping multiple Column of a dataset based on the column name 
df1 = df1.drop(['Pclass','Cabin'],axis=1)
print(df1.head())


# 3. Dropping the Column of a Dataset based on the Column Index
df1 = df1.drop(df1.columns[1],axis=1)
print(df1.head())


# 4. Dropping the Multiple Column of a dataset based on the Column Index
df2 = df1.drop(df1.columns[[1,3]],axis=1)
print(df2.head())
