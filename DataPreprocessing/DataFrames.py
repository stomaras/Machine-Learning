# DataFrames

import pandas as pd 
import numpy as np 
#'PCLASS','NAME','SEX','AGE','SIBSP','PARCH','TICKET','FARE','CABIN','EMBARKED']
#dataset = pd.read_csv('C:/PythonForMachineLearning-master/Part1/train.csv')
#fields = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
trains = pd.read_csv('C:/Users/sptom/Music/PythonForMachineLearning-master/Part1/tr.csv',delimiter=';')

df = pd.DataFrame()

df['Name'] = ['Steven Smith','Virat Kohli']
df['Age'] = [26,25]

df['Country'] = ['Aus','Ind']

# How to add the rows at the bottom 
# Create a new row
new_row = pd.Series(['Angelo Mathes', 28, 'Sri'])
df.append(new_row,ignore_index=True)

# How to describe a dataset

# Head
trains.head()

# Tail 
trains.tail()

# display the first 3 rows of dataset
trains.head(3)

# Shape of a dataset
trains.shape
