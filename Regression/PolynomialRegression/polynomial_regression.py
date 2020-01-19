# Polynomial Regression 

# Now we are making new kind of regressors which are slightly more advanced regressors 

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# So we are a human resource team working for a big company and we are about to hire a new employee in this company , so this new employee seems to be great a good fit for the job and we are about 
# to make an offer to this potential new employee and now its time to negotiate on what is going to be the future salary of this new employee in the company and so at the beginning of the negotiation this new employee
# is telling that he's had 20 plus years of experience an eventually earns 160k annual salary in its previous company, so this employee is asking for at least more than 160 k, However is someone
# in the HRT that is kind of a control freak and always fantasised about being a detective so suddenly decides to call the previous employee to check that info.You know that info about the previous 160k
# annual salary of this fututre potential new employee. But unfortunately all the info that this person manages to get all these info here that is the symbol table of salaries for 10 different positions
# in the previous company so just the hr memeber of the team runs a simple analysis on Excel or a Google sheet and actually observes that there is no liner relationship between these position levels 
# and their associated salaries. However this H.R person could get another very relevant info . This other relevant info is that this new employee has been a region manager for two years now and usually 
# takes on average four years to jump from being a regional manager to partner . So this employee was kind of halfway between lenel 6 and level 7 and therefore we can say he was level 6.5. So now this H.R
# guy is excited because he's selling to the team that he can build a bluffing detector using regression models and predict if this new employee is bluffing about its salary . So at the beginning the team 
# finds it a little weird but it;s kind of curious to see what's going to happen and therefore here is the mission. This new employee is telling that it's annual salary was 160k lets's predict if it's 
# truth or bluf by building a bluffing detector using polynomila regression. So we want to predict the salaries based on the different levels that we have and then predict the salary of a 6.5 level here.
# so we just need last 2 columns because table is already encoding here and therefore we only need these two columns to build our machinery model .Remember the machine is the polynomial regression and this machine
# is going to learn the correlations between the levels and the salaries to predict if the employee is bluffing about its salary . In this case the only one independent variable will be the level of column
# and the dependent variable vector y will be salary column , contain all different salaries for the 10 different positions.

dataset = pd.read_csv('C:/Users/sptom/OneDrive/Υπολογιστής/P14-Machine-Learning-AZ-Template-Folder/Machine Learning A-Z Template Folder/Part 2 - Regression/Section 6 - Polynomial Regression/P14-Polynomial-Regression/Polynomial_Regression/Position_Salaries.csv')
# in order to specify that  X is a matrix and not a vector we use the follow condition.
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# we have a small number of observations so does not make sense to split our dataset to test set and train set because we simply 
# don't have enough information to train a model in one set and tests its performance to another set.I t would not make much sense and it would be a little ridiculous
# And the second reason is that you know we want to make a very accurate prediction because you know it's something real we are talking about here we are trying to predict the central elements 
# of the negotiation we are having there is the salary of this new employee seo we need not to miss the target here and therefore we need to make a very accurate prediction.


# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
# these poly_reg object that we created automatically created this column of ones here to include the constant be zaro and the multiple in our regression equation

# Visualizing the Linear Regression results 
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlablel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualizing the Polynomial Regression results 

# we can improve this plot indeed what's happening here is that our code is giving us the predictions of the model for each of the 10 levels from 1 to 10 but it's putting some straight lines 
# in between two predictions we can actually have the real continuous curve by instead of having only the predictions from 1 to 10 incremented by one we are going to have the predictions 
# from 1 to 10 incremented by a higher resolution like a 0.1 step. What wwe need is to create just a new X_grid here 
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlablel('Position level')
plt.ylabel('Salary')
plt.show()

# Now we just have one final step to do and that is the step that we are going to be able to say truth or bluff by predicting the previous salary of this new employee. That;s as 
# reminder told us that its previous salary was 160K and so we'll compare this value to our prediction and that's where we will be able to conclude if this employee was bluffing 
# So lets predict this result with the linear regression model

# Predicting a new result with Linear Regression
lin_reg.predict(6.5)


#Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))
