# Backward Elimitation

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('C:/Users/sptom/OneDrive/Υπολογιστής/P14-Machine-Learning-AZ-Template-Folder/Machine Learning A-Z Template Folder/Part 2 - Regression/Section 5 - Multiple Linear Regression/P14-Multiple-Linear-Regression/Multiple_Linear_Regression/50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([('encoder', OneHotEncoder(), [3])], remainder='passthrough')

X = np.array(ct.fit_transform(X), dtype=np.float)

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

import statsmodels.regression.linear_model as sm
X = np.append(arr = np.ones((50,1)).astype(int),values = X, axis=1)
x_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog =x_opt).fit()
regressor_OLS.summary()
x_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog =x_opt).fit()
regressor_OLS.summary()
x_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog =x_opt).fit()
regressor_OLS.summary()

# So maybe the independent variables that is R&D spend and marketing spend compose the final team of our independent variables that make the best team to predict the profits
# So as we can see from the results the R&D spend has high statistical effect impact on the depenndent variable profit 
# But as far as the second independent variable is concerned that is the marketing spend we can see that the p-value is 0.06 that is 6 percent . Well it' s actually slightly above the 5 percent significance
# level that we set so we must remove the marketing spend accord we backward elimitation algorithm 
# So . . .
x_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog =x_opt).fit()
regressor_OLS.summary()

# So now we have the final table with p-value very very small which definetely makes the R&D spend a very powerful predictor of the profits 
# So if we follow the backward elimitation algorithm we will end up that the best team of independent variables that can predict a profit with the highest statistical significancne 
# the strongest impact is actually composed of only one independent variable and that happens to be the R&D spend and that's it.
x_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog = y, exog =x_opt).fit()
regressor_OLS.summary()
