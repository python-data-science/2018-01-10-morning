import pandas as pd
import numpy as np

df = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')

# Question 1:
# In 2007, which gender (man, woman) had higher average unemployment?

# Selects the 2007 year period.
yr07 = df[(df['Period'] >= '2007-01-01') & (df['Period'] < '2008-01-01')]

# Group by 'Gender' and then take the mean.
unemployed_by_gender = yr07.groupby('Gender').agg('mean')

# Question 2:
# What month, on average, has the lowest unemployment for women?

# Filter 'Gender' for 'Women' and groupby the 'Period'.
# String format to datetime to return the month as a string.
# Apply the aggregate method to find the mean.
# Reset the index from 0-n and then sort it by Unemployed.
# Sorting by ascending returns the lowest value first.
# Set the index from 0-n to the 'Period' (or the month in this case).

low_unemp_month = df.loc[df['Gender']=='Women'].groupby(df['Period'].\
dt.strftime('%B')).agg('mean').reset_index().\
sort_values(by='Unemployed', ascending=True).set_index('Period')

# Use the idxmin to find the lowest value in the dataframe.
lowest_month = low_unemp_month.idxmin(axis=0)
