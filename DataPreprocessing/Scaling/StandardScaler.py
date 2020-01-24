# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:20:59 2020

@author: sptom
"""

from sklearn import preprocessing 
import numpy as np 

x = np.array([[-400],[-100],[0],[100],[400]])

standardscaler = preprocessing.StandardScaler()

x_scaler = standardscaler.fit_transform(x)

print(x_scaler)

''' 
-400 - np.mean(x)/np.std(x)

'''
#-----------------------------------------------------------------------------------

x1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

standardscaler1 = preprocessing.StandardScaler()

x_scaler1 = standardscaler1.fit_transform(x1)

'''
(1-4)/np.std(x1[:,0])

'''

#-----------------------------------------------------------------------------------

import pandas as pd

dataset = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part22/Age-Salary.csv')

features = dataset.iloc[:,[2,3]].values

standardscaler2 = preprocessing.StandardScaler()

x_scaler2 = standardscaler1.fit_transform(features)

print(x_scaler2)
