
"""
Created on Tue Jan 21 16:25:48 2020

@author: sptom
"""

import pandas as pd 
import numpy as np 

trains = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part1/tr.csv',delimiter=';')

# Get the Maximum Value of column Age
print('Maximum value of column Age: ', trains['Age'].max())

# Get the Minimum Value of column Age
print('Maximum value of column Age: ', trains['Age'].min())

# Find the sum of the rows in the column Age
print('Maximum value of column Age: ', trains['Age'].sum())

#Get the count of the number of rows in column Age
print('Maximum value of column Age: ', trains['Age'].count())

# Get the Average/mean of the column Age
print('The Average Age is :', trains['Age'].mean())


#Nan - No a Number

# How to find the unique values and its count 

trains['Age'].count()

trains['Sex'].count()

trains['Sex'].unique()

trains['Sex'].value_count()
