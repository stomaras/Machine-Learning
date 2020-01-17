# Simple Linear Regression


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('C:/Users/sptom/OneDrive/Υπολογιστής/P14-Machine-Learning-AZ-Template-Folder/Machine Learning A-Z Template Folder/Part 2 - Regression/Section 4 - Simple Linear Regression/P14-Simple-Linear-Regression/Simple_Linear_Regression/Salary_Data.csv')
X = dataset.iloc[:, :-1].values # Independent Variable YearsExperience
y = dataset.iloc[:, 1].values # Dependent Variable Salary

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
#These lines of codes fit your regressors object which is an object of the linear Regression class to train
#set X_train and y_train, this will not only create our simple linear regressor but also it will fit this regressor to our training data that means that 
#executing this code section here our model will already learn the correlations of our training set to learn how it can predict the dependent variable which is 
#salary based on the information of the independent variable that is the number of years of experience
# Fitting Simple Linear Regression to the Training set
#learning is the fact that this simple linear regression machine learns on the training set composed of x and y train
#That is what machine learning is .We created a machine which is a regress or here the simple regressor and we made this machine learn on the training set to understand
#the correlations between the experience and the salary so that this machine based on its learning experience can then predict the salary with respect to the experience.
# This is the most simple Machine Learning Model and i just create it.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results 

# This vector will contain the predicted salaries for all the observations of our test sets
y_pred = regressor.predict(X_test)
