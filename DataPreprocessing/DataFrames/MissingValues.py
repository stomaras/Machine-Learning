# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:07:31 2020

@author: sptom
"""

import pandas as pd
import numpy as np 

df = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part1/tr.csv',delimiter=';')

# Get the rows that contains NULL (NaN)

df.isnull().sum()

# data without missing values with respect to columns 
data_without_missing_values_cols = df.dropna(axis=1)

#data without missing values with respect to rows
data_without_missing_values_rows = df.dropna(axis=0)

# IF we want to get the columns in a dataset with the missing value we will use the following approach 
cols_with_missing_values = [col for col in df.columns if df[col].isnull().any()]

# drop the columns that contains the missing values then we can follow the below approach
reduced_data = df.drop(cols_with_missing_values, axis=1)
