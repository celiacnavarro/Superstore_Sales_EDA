# Import libraries
import pandas as pd
import datetime

# Load the dataset
df = pd.read_csv('data/sales_data.csv')

# Data cleaning
df.drop('Row ID',axis = 1, inplace = True)
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

df.sort_values(by=['Order Date'], inplace=True, ascending=True)
df.set_index("Order Date", inplace = True)

df['Postal Code'] = df['Postal Code'].fillna(5401)

# Save data 

df.to_csv('data/data_cleaned_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv')

