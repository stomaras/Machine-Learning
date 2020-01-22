
"""
Created on Wed Jan 22 12:21:24 2020

@author: sptom
"""

import pandas as pd 
import numpy as np 

ts_index = pd.date_range('01/01/2017',periods=200000,freq='60S')

df = pd.DataFrame(index=ts_index)

# Using the random function will create randomly how many cars vehicles will pass through the traffic signal every minute so if we give we add the column 
# df['numberofvehicles'] = np.random.randint(1,10,) we will see it in frequency of every car like maximum car will for every minute the number of cars which vary will from 1 to 10 and 
# for how many distribution  like what we have period mention is to lactate so will give 2 lahks and we'll execute it 

df['No_of_Vehicles'] = np.random.randint(1,10,200000)

# On a weekly basis how many vehicles are passing then we give this 

df.resample('W').sum()


# On bi-weekly basis how many vehicles are passing through we give this 

df.resample('2W').sum()

# On a monthly basis how many vehicles are passing through

df.resample('M').sum()

df.resample('M',label='left').sum()


ts_value = pd.date_range('01/01/2017',periods=200000,freq='15S')

df1 = pd.DataFrame()

df1['Datetime'] = ts_value

df1['Year'] = df1.Datetime.dt.year

df1['Month'] = df1.Datetime.dt.month

df1['Day'] = df1.Datetime.dt.day

df1['Weekday_name'] = df1.Datetime.dt.weekday_name

df1['Hour'] = df1.Datetime.dt.hour

df1['Minutes'] = df1.Datetime.dt.minute

df1['Second'] = df1.Datetime.dt.second

df1['Microsecond'] = df1.Datetime.dt.microsecond
