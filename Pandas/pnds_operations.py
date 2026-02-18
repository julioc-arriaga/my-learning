import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4], 
                   'col2': [444, 555, 666, 444], 
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

print(df)
# Finding unique values in a column
print("Unique values in col2: ", df['col2'].unique())
# Finding the number of unique values in a column
print("Number of unique values in col2: ", df['col2'].nunique())
# Finding the frequency of unique values in a column
print("Frequency of unique values in col2: ", df['col2'].value_counts())
# Selecting rows based on a condition
print("Rows where col2 is 444: \n", df[df['col2'] == 444])
# Selecting rows based on multiple conditions
print("Rows where col2 is 444 and col3 is 'abc': \n", df[(df['col2'] == 444) & (df['col3'] == 'abc')])
# Applying a function to a column
print("Applying a function to col1 (squaring the values): \n", df['col1'].apply(lambda x: x**2))
# Creating a new column based on existing columns
df['col4'] = df['col1'] + df['col2']
print("DataFrame with new column col4: \n", df)
# Dropping a column
df.drop('col4', axis=1, inplace=True)
print("DataFrame after dropping col4: \n", df)
# Renaming columns
df.rename(columns={'col1': 'Column1', 'col2': 'Column2', 'col3': 'Column3'}, inplace=True)
print("DataFrame with renamed columns: \n", df)
# Sorting the DataFrame by a column
print("DataFrame sorted by Column2: \n", df.sort_values(by='Column2'))
# Resetting the index after sorting
print("DataFrame sorted by Column2 with reset index: \n", df.sort_values(by='Column2').reset_index(drop=True))
# Grouping data by a column and calculating the mean
print("Mean of Column1 grouped by Column2: \n", df.groupby('Column2')['Column1'].mean())
# Pivoting the DataFrame
pivot_df = df.pivot_table(values='Column1', index='Column2', columns='Column3', aggfunc='mean')
print("Pivot table of Column1 with Column2 as index and Column3 as columns: \n", pivot_df)
# Finding null values in the DataFrame
print("Null values in the DataFrame: \n", df.isnull())