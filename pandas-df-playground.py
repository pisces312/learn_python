import numpy as np
import pandas as pd

'''
The following code is to help you play with the concept of Dataframe in Pandas.

You can think of a Dataframe as something with rows and columns. It is
similar to a spreadsheet, a database table, or R's data.frame object.

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''

'''
To create a dataframe, you can pass a dictionary of lists to the Dataframe constructor:
1) The key of the dictionary will be the column name
2) The associating list will be the values within that column.
'''
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data)
#Also print the index of row which starts with 0
print football

'''
Pandas also has various functions that will help you understand some basic
information about your data frame. Some of these functions are:
1) dtypes: to get the datatype for each column
2) describe: useful for seeing basic statistics of the dataframe's numerical columns
3) head: displays the first five rows of the dataset
4) tail: displays the last five rows of the dataset
'''
print football.dtypes
print ""
print football.describe()
print ""
print football.head()
print ""
print football.tail()


'''
You can think of a DataFrame as a group of Series that share an index.
This makes it easy to select specific columns that you want from the DataFrame. 

Also a couple pointers:
1) Selecting a single column from the DataFrame will return a Series
2) Selecting multiple columns from the DataFrame will return a DataFrame

'''
print football['year'] # return a Series
print ''
print football.year  # use dot '.', shorthand for football['year']
print ''
print football[['year', 'wins', 'losses']] # return a DataFrame


'''
Row selection can be done through multiple ways.

Some of the basic and common methods are:
   1) Slicing
   2) An individual index (through the functions iloc or loc)
   3) Boolean indexing

You can also combine multiple selection requirements through boolean
operators like & (and) or | (or)
'''

print football.iloc[[0]] # first row
print ""
print football.loc[[0]] # first row
print ""
print football[3:5] # [3,5) -> 3,4
print ""
print football[football.wins > 10]
print ""
print football[(football.wins > 10) & (football.team == "Packers")]
