# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:14:20 2020

@author: sptom
"""

# No we will learn about measures of central tendency so what is central tendency 
# A central tendency in statistics on the measures of central tendency is a central or typical value for a propability distribution 
# it may also be called a center or location of the distribution so in this session we 'll mean median mode standard deviation variance 
# quartiles like lower quartile q1 upper quartile inter quartile and semi interquartile range so 


import statistics as st
from scipy import stats
import numpy as np 

x = [0,1,2,3,4,5,6,7,8,9]

st.mean(x)

st.median(x)

st.median_low(x)

st.median_high(x)

x1 = [0,1,2,3,4,4,5,6,7,8,9]

st.mode(x1)

st.stdev(x) # Standard deviation is a measure that is used to quantify the amount of variation or dispersion of a set of data value

st.variance(x)

Q1 = np.percentile(x,np.arange(0,100,25))

Q3 = np.percentile(x,np.arange(0,100,75))

matrix = np.array([[1,2,4],
                   [3,5,2],
                   [2,1,9]])

np.mean(matrix)

1 2 4 3 5 2 2 1 9

1 1 2 2 2 3 4 5 9 # Sorted numbers 

1 2 3 4 5 6 7 8 9

np.std(matrix)

np.var(matrix)


# Q1 or lower quartile
np.percentile(matrix,25) #2
#Q3
np.percentile(matrix,75) #4

np.percentile(matrix,25,axis=0)

np.percentile(matrix,25,axis=1)



#=--------------------------------------------#
# Mode

stats.mode(matrix)

# Default like matrix
stats.mode(matrix,axis=0)

stats.mode(matrix,axis=1)
