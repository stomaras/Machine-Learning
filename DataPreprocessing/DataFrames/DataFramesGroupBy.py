
"""
Created on Wed Jan 22 12:13:29 2020

@author: sptom
"""

import pandas as pd 
import numpy as np 

df = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part1/tr.csv',delimiter = ';')

df.groupby('Sex').mean()

df.groupby('Sex')['Age'].mean()

df.groupby(['Sex','Survived'])['Age'].mean()


df.groupby(['Sex','Pclass','Survived'])['Age'].mean()
