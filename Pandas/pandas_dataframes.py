import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)
#create dataframe
#df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df['X'])
print(type(df['W']))
print(df[['W', 'Z']])
print(df.W)
#print(df.W[0])
#print(df['W'][0])
df['new'] = df['W'] + df['Y']
print(df)
df.drop('new', axis=1, inplace=True)
print(df)
df.drop('E', axis=0, inplace=True)
print(df)
print(df.shape)
print(df.loc['A'])
print(df.iloc[0])
print(df.loc['B', 'Y'])
print(df.loc[['A', 'B'], ['W', 'Y']])
