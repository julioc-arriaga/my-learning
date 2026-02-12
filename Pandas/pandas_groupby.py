import numpy as np
import pandas as pd

d = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(d)
print("DataFrame:")
print(df)
byComp = df.groupby('Company')['Sales']
print("GroupBy object:")
print(byComp)
print("Mean sales by company:")
print(byComp.mean())
print("Sum of sales by company:")
print(byComp.sum())
print("Standard deviation of sales by company:")
print(byComp.std())
print("Minimum sales by company:")
print(byComp.min())
print("Maximum sales by company:")
print(byComp.max())
print("Count of sales by company:")
print(byComp.count())
print("Describe sales by company:")
print(byComp.describe())
print("Group by company and person, then sum sales:")
print(df.groupby(['Company', 'Person']).sum())
