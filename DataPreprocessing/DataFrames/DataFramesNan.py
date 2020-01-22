
"""
Created on Wed Jan 22 11:29:43 2020

@author: sptom
"""

import pandas as pd
import numpy as np

Series1 = pd.Series([7,6.8,'Avengers',np.nan,'Apple'])

#isnull() and not null()

# Both the above functions return boolean (True or False)

Series1.isnull().sum()

Series1.notnull().sum()

####################################


dataset = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part1/tr.csv',delimiter = ';')

dataset[dataset['Age'].isnull()].head()

dataset[dataset['Age'].notnull()].head()

##########################################################################

# what happen of we try to replace some value with nan?

dataset['Sex'] = dataset['Sex'].replace('female',np.nan)
