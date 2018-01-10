"""
Question 1:
In 2007, which gender (man, woman) had higher average unemployment?

Question 2:
What month, on average, has the lowest unemployment for women?
"""

import pandas as pd

df = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')

df['Period'] = pd.to_datetime(df.Period)

df.info()

# filter to 2007
df2007 = df[(df.Period >= '2007-01') & (df.Period <= '2007-12')]

# group by Gender and find mean
bygender = df2007.groupby(['Gender'])['Unemployed'].agg(['mean'])

# Question 1:
# In 2007, which gender (man, woman) had higher average unemployment?
# Answer: Men
bygender


# filter to Women
dfwomen = df[(df.Gender == 'Women')]

# create a new column for just the month
dfwomen['month'] = dfwomen.Period.dt.month

# group by Month and find mean
bymonth = dfwomen.groupby('month')['Unemployed'].agg(['mean'])

# Question 2:
# What month, on average, has the lowest unemployment for women?
# Answer: February
bymonth.sort_values('mean', ascending=True)


