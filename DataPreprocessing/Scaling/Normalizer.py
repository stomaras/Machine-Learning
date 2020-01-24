# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:34:53 2020

@author: sptom

Xi/sqrt(sum of all the squares of that row)


"""

from sklearn import preprocessing
import numpy as np

x = np.array([[1,2],
              [2,5],
              [3,6],
              [4,9],
              [5,8]])

normalizer = preprocessing.Normalizer()

normal = normalizer.fit_transform(x)

print(normal)

#---------------------------------------------------
'''
1/(np.sqrt(1+4+9))


'''
x1 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])


normalizer = preprocessing.Normalizer()

normal = normalizer.fit_transform(x1)

print(normal)

#-------------------------------------------------

import pandas as pd
dataset = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part22/Age-Salary.csv')

features = dataset.iloc[:,[2,3]].values

normalizer2 = preprocessing.Normalizer()

normal = normalizer2.fit_transform(features)

print(normal)
