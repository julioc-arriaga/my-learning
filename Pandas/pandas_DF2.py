import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)
#create dataframe
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print(df>0) #conditional selection, returns a dataframe of booleans
booldf = df>0
print(booldf) 
print(df[booldf]) #passing the dataframe of booleans to the original dataframe, returns only the values that are true, rest are NaN
print(df[df>0]) #same as above in one line
print("returns all the rows where column Z is less than 0")
print(df[df['Z']<0]) #returns all the rows where column Z is less than 0
print("returns all the rows where column Z is less than 0, but only the Z column")   
print(df[df['Z']<0]['Z']) #returns all the rows where column Z is less than 0, but only the Z column
print(df)
print("multiple conditions")
print(df[(df['Y']>1) & (df['W']>0)])
df['State'] = ['CA', 'NY', 'WY', 'OR', 'CO']
print(df)
print("Setting index to State")
df.set_index('State', inplace=True)
print(df)
