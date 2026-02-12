"""
================================================================================
File: pandas_missingdata.py
Purpose: Demonstrate handling missing data in Pandas DataFrames using various
         techniques including dropna(), fillna(), and conditional operations.
Created: 2026-02-11
Author: Julio Arriaga
================================================================================
"""

import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)
# drop any row that has NaN values
print(df.dropna())
# drop any column that has NaN values
print(df.dropna(axis=1))
# drop any row that has less than 2 non-NaN values
print(df.dropna(thresh=2))
# fill NaN values with a specific value
print(df.fillna(value='FILL VALUE'))
# fill NaN values with the mean of the column
print(df['A'].fillna(value=df['A'].mean()))
