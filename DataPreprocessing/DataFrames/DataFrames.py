"""
Topics to be covered:
    1. How to create a Dataframe
    2. How to Describe a DataFrame
    3. How to Navigate the Dataframe
    4. How to select the rows of a pandas Dataframe based on conditions
    5. How to replace a value
    6. How to rename a column 
"""
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

# How to navigate the DataFrame
# loc and iloc 

trains.iloc[0]

trains.iloc[0][4]

trains.iloc[1:5]

trains.iloc[2:5]


#############################################################

# how to set the index of a dataset 

df = df.set_index(df['Name'])

# how to show the row based on the name
df.loc['Virat Kohli']


# How to select the rows of a pandas Dataframe based on conditions 

trains[trains['Pclass'] == 3].head(2)

# Get the data based on conditions on more than 1 columns

trains[(trains['Sex'] == 'male') & (trains['Age'] > 40)]

# How to replace a value?

trains['Sex'].replace("male", 'Men')

trains['col1'] = trains['Sex'].replace("male",'Men')


# How to rename a column 

trains = trains.rename(columns={'col1':'col2'})
