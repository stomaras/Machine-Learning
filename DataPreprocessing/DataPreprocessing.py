# Data Preprocessing

#Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the dataset

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values



# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(y)

#Encoding categorical data


Country_dummies = pd.get_dummies(dataset, columns=['Country'])
Purchased_dummies = pd.get_dummies(dataset, columns=['Purchased'])
print(Country_dummies)
print(Purchased_dummies)

# Splitting the dataset into the training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
