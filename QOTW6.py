"""
Puja Roy
DATA 602
3/2/24
"""

"""
1. What are the similarities and differences between pandas and numpy?   Include some type of example with code.
Both pandas and numpy are utilized for data manipulation such as indexing, slicing, and mathematical operations and analysis in Python.
To add on, they are based on handling data structures to handle multi-dimensional arrays.

The differences are that numpy mostly deals with numerical data and mathematical operations.
Whereas, pandas provides more functionality for data cleaning and wrangling including data alignment, handling missing data, and database-like operations.

"""
# Below is an example:

import numpy as np
import pandas as pd

# NumPy array
np_array = np.array([2, 4, 6, 8, 10])

# Pandas Series
pd_series = pd.Series([2, 4, 6, 8, 10])


"""
2. What is the ndarray in numPy?

ndarray stands for n-dimensional array in NumPy. It is the most common data structure in NumPy, which represents a multi-dimensional, homogeneous array of fixed size.
ndarray provides storage and operations on large arrays of data.

"""

"""
3. Create a 1D array of numbers from 0 to 9 

Desired Output: 

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
"""
array1d = np.arange(10)
print(array1d)
# OUTPUT: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 4. Extract all odd numbers from array1 

array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

odd_numbers = array1[array1 % 2 != 0]
print(odd_numbers)
# OUTPUT: array([1, 3, 5, 7, 9])

# 5. Get the common items between a and b  

#input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

common_items = np.intersect1d(a, b)
print(common_items)

#Desired Output:

#array([2, 4])


# 6. From array a remove all items present in array b 

#Input:

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

result = np.setdiff1d(a, b)
print(result)


#Desired Output:

# array([1,2,3,4])


# 7. Find out if iris has any missing values. 

# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# Check for missing values
has_missing_values = np.isnan(iris).any()
print("Does iris have missing values?", has_missing_values)

# OUTPUT: Does iris have missing values? False







