#import packages 
import pandas as pd
import numpy 
import uuid
import datetime

#load in data
dataset = pd.read_csv('data/School_Learning_Modalities.csv')

#print columns and rows
print (dataset.shape)

#print column names 
print (dataset.columns)

#clean column names
dataset.columns = dataset.columns.str.replace('[^A-Za-z0-9]+', '_')

#clean strings that exist in each column
dataset['District_Name'] = dataset['District_Name'].str.replace('[^A-Za-z0-9]+', '_')
dataset['Learning_Modality'] = dataset['Learning_Modality'].str.replace('[^A-Za-z0-9]+', '_')
dataset['City'] = dataset['City'].str.replace('[^A-Za-z0-9]+', '_')
dataset['State'] = dataset['State'].str.replace('[^A-Za-z0-9]+', '_')

#assess white space or special characters?

#convert column type 
dataset['Week'] = pd.to_datetime(dataset['Week'])

#look for/remove duplicate rows 
dataset.duplicated()
dataset.drop_duplicates()

#assess missingness
dataset.isnull().sum()

#replace empty/cells with whitespace 
dataset.replace(to_replace='', value=numpy.nan, inplace=True)
dataset.replace(to_replace=' ', value=numpy.nan, inplace=True)

#new data 
dataset['modality_inperson'] = (dataset['Learning_Modality'].apply(
    lambda x: 'True' if x == 'in-person' else False))
