# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:50:24 2020

@author: sptom
"""

'''
Topics to be covered

Feature Scaling
1. Min Max Scaler
2. Standard Scaler
3. Normalize
4. Binarize
'''

# Why we require feature scaling? 
# Beacause there is a lot of disparity between the extreme values in a data which means the data is not normalized 
# and not scaled then we will not get the desired result and the output will be misleading also the data lies between the different mean values resulting in two different standard deviation and
# variance


from sklearn import preprocessing
import numpy as np 

x = np.array([[-400],[-100],[0],[100],[400]])

# Creating the Scaler 
minmaxscaler = preprocessing.MinMaxScaler(feature_range=(0,1))

x_scaler = minmaxscaler.fit_transform(x)

print(x_scaler)

''' (Xi - Xmin) / (Xmax - Xmin)
(-100 - (-400))/(400 -(-400))
(-100 + 400) / (400 + 400)
300/800 = 0.375'''

################################## Applying it to 3X3 Matrix

x1 = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])


# Creating the Scaler 
minmaxscaler1 = preprocessing.MinMaxScaler(feature_range=(0,1))

x_scaler1 = minmaxscaler1.fit_transform(x1)
print(x_scaler1)

############################################################################################################# Applying it to a Pandas DataSet

# This is like a simple approach but in the reality like when we are dealing with a dataset  how do we achieve that how do we transform the columns
 
# of a dataset using the same procedure 

import pandas as pd

dataset = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part22/Age-Salary.csv')

# We need to do extract to column Age and column Salary 

features = dataset.iloc[:,[2,3]].values

# Now we create a min max scaler
 
minmaxscaler = preprocessing.MinMaxScaler(feature_range=(0,1))

features_scale = minmaxscaler.fit_transform(features)
