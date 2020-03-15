import pandas as pd
import numpy as np
#cRecreate random DataFrame with Nan values
df = pd.DataFrame(index = pd.date_range('2017-01-01', '2017-01-10', freq='1d'))

print("****************************** DATA FRAME CREATED ************************")
print(df)

# Creating a new column with random values. Using the numpy package for this
df['A'] = np.random.randint(low = 180, high = 200, size = len(df))
#df['A'] = np.random.randint(low=198, high=205, size=len(df.index))
df['B'] = np.random.random(size = len(df))*2
print(df.head())

#Create dummy NaN value on 2 cells
df.iloc[5,0]=None

print(df)

#removing the NULL value
df = df.dropna(axis =0, how = "any")

print(df)