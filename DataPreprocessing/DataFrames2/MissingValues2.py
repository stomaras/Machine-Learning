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
#-----------------------> Second Approach using Imputer 

# features are refer as Capital X
# Labels refer as y


import pandas as pd
import numpy as np 


df = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part1/Datapreprocessing.csv',delimiter=';')

features = df.iloc[:,:-1].values

labels = df.iloc[:,-1].values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)

# 2 step transformation
# Fit and transform
# Imputer will be apply only one numeric column in this case numeric column is the age and the salary 
# Imputer Object to handle the missing values
# This is the way that we deal with numeric missing values 
imputer.fit(features[:,[1,6]])

features[:,[1,6]] = imputer.fit_transform(features[:,[1,6]])

df1 = pd.DataFrame(features)

# Some other not null missing values are the columns occupation and Employment Type 

#---------------------------------------------------------------------------------------------------------------------------------------

# Columns with null but no numeric values 

# Imputation logic how to fill the missing values and also we can use the like for non numeric columns we can use different size like filling it with modal values 
cols = ['Occupation','Employment Status','Employement Type']

df[cols] = df[cols].fillna(df.mode().iloc[0])
