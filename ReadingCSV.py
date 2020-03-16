#Importing the required packages
import csv
import pandas as pd
import numpy as np
#the reading of csv file without pandas package is done using a three step process
#first it is opened using the open() function used along with the WITH clause
#then using a loop, a reader() reads each line in the csv.
NameAgeCsv = '/Users/aakarsh.rajagopalan/Personal documents/Python projects/ReadingCSVwithoutPandas/NameAge.csv'

with open(file=NameAgeCsv) as file:
    reader = csv.reader(file, delimiter=',')
    df = pd.DataFrame(reader)
    print(df.head())
    for records in reader:
        print(records)

#Removing the record with the NULL value
df_without_blank_age = df.dropna(axis=0,how="any")

print(df_without_blank_age)