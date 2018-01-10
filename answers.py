import pandas as pd
import numpy as np

df = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')

# Question 1:
# In 2007, which gender (man, woman) had higher average unemployment?

yr07 = df[(df['Period'] >= '2007-01-01') & (df['Period'] < '2008-01-01')]
unemployed_by_gender = yr07.groupby('Gender').agg('mean')

# Question 2:
# What month, on average, has the lowest unemployment for women?

low_unemp_month = df.loc[df['Gender']=='Women'].groupby(df['Period'].\
dt.strftime('%B')).agg('mean').reset_index().\
sort_values(by='Unemployed', ascending=True).set_index('Period').idxmin(axis=0)
