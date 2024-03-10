"""
Puja Roy
DATA 602
3/8/24
"""

"""
1. What is pandas and why use it?

Pandas is a Python library that provides access to working with data structures
and data analysis tools. The reason we utilize it is because it's useful for
data manipulation and analysis tasks especially when working with tabular data
(CSV files and Excel sheets). To add on, pandas allows us to simply access,
read, write, filter, transform and analyze data.
"""

"""
2. Give an example of how to import a csv file using pandas

To import a CSV file using pandas, we use the read_csv() function. Below is an
example:

import pandas as pd

# An example of 'data.csv' as the CSV file
df = pd.read_csv('data.csv')

"""

"""
3. Show how to view the first 10 rows of a dataset using pandas

To view the first 10 rows of a dataset using pandas, we can use the head() function.
Below is an example:

import pandas as pd

# Assuming df is the dataset
first_10_rows = df.head(10)
print(first_10_rows)

"""

"""
4. Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

To compare the elements of two Pandas Series, we can directly compare the two series. Below is an example:

"""
import pandas as pd

# Sample Series
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])

comparison_result = series1 == series2
print(comparison_result)

"""
#5. Change the first character of each word to upper case in each word of df1
#df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])

To change the first character of each word to uppercase in each word of a pandas Series, we can use the str.capitalize() method
"""
import pandas as pd

df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])

# Capitalize the first character of each word
df1_capitalized = df1.str.capitalize()

print(df1_capitalized)


