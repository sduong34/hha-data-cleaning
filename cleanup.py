#import packages 
import pandas as pd
import numpy 
import datetime

#load in data
df = pd.read_csv('data/School_Learning_Modalities.csv')
#print columns and rows
print (df.shape)
#print column names 
print (list(df))

#clean column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
