"""
File: pnd_mrgJoinConcat.py
Description: Examples demonstrating pandas merge, join, and concat operations.
Author: Julio Arriaga
Created: 2026-02-14
"""

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])
print(df1)
print(df2)
print(df3)
# Concatenate the DataFrames
print("Concatenating DataFrames")
concat = pd.concat([df1, df2, df3])
print(concat)

# Merge DataFrames
print("Merging DataFrames")
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
# Merge the DataFrames on the key column
merged = pd.merge(left, right, on='key') # by default it is an inner join
print(merged)
# Merge the DataFrames using an outer join
merged_outer = pd.merge(left, right, on='key', how='outer')
print(merged_outer)
left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
# Merge the DataFrames on multiple keys
print("Merging on multiple keys")
merged_multi = pd.merge(left, right, on=['key1', 'key2']) # by default it is an inner join
print(merged_multi)
# Merge the DataFrames using an outer join
print("Merging on multiple keys using outer join")
merged_multi_outer = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(merged_multi_outer)
# Join DataFrames
print("Joining DataFrames")
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                     index=['K0', 'K1', 'K2', 'K3'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                      index=['K0', 'K1', 'K2', 'K3'])
print("left")
print(left)
print("right")
print(right)
# Join the DataFrames on the index
joined = left.join(right)
print("Joined DataFrame")
print(joined)