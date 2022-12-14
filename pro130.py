import pandas as pd
import csv

df = pd.read_csv("PRO130.csv")
print(df.columns)
#multi delete
df.drop(['Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'],axis = 1,inplace=True)
print(df.columns)#name
print(df.head())#top5
print(df.shape)#no.ofrowsandcolumns
print(df.describe())