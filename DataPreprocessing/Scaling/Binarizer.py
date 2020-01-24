# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:46:46 2020

@author: sptom
"""

from sklearn import preprocessing 
import numpy as np 

x = np.array([[1,2],
              [2,5],
              [3,6],
              [4,9],
              [5,8]])

binarizer = preprocessing.Binarizer(4)

binarizer_scaled = binarizer.fit_transform(x)

print(binarizer_scaled)

#------------------------------------------------------------------------------

x1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

binarizer1 = preprocessing.Binarizer(4)

binarizer_scaled1 = binarizer1.fit_transform(x1)

print(binarizer_scaled1)


#------------------------------------------------------------------------------

import pandas as pd

dataset = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part22/Age-Salary.csv')

features = dataset.iloc[:,[2]].values


binarizer2 = preprocessing.Binarizer(33)

binarizer_scaled2 = binarizer2.fit_transform(features)

dataset['bin_col'] = binarizer_scaled2

print(binarizer_scaled2)

