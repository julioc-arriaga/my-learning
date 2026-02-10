"""
================================================================================
Program: pandas_DF3.py
================================================================================

Purpose:
    Exercises for using Pandas DataFrames, focusing on 

Inputs:
    [Describe the expected inputs]

Outputs:
    [Describe the expected outputs]

Author:
    Julio Arriaga

Date Created:
    Feb 9, 2025

Version:
    1.0

================================================================================
"""
from matplotlib.pylab import randn
import numpy as np
import pandas as pd

#Index levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
print(hier_index)
print(type(hier_index))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(randn(6,2), hier_index, ['A', 'B'])
print(df)
# Print the data for group G1
print(df.loc['G1'])
# Print the data for group G2, row 1
print(df.loc['G2'].loc[1])
# Print the data for group G2, row 1, column B
print(df.loc['G2'].loc[1]['B'])
# Setting index names
df.index.names = ['Groups', 'Num']
print(df)
# Retrieve data for group G1, row 2, column A
print(df.loc['G1'].loc[2]['A'])
# Cross-section method, retrieves data for all groups, row 2, column A
print(df.xs(2, level='Num')['A'])