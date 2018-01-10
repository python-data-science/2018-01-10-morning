import pandas as pd


# Question 1
# In 2007, which gender (man, woman) had higher average unemployment

# Question 2
# What month, on average, has the lowest unemployment for women?

df = pd.read_excel('unemp.xlsx')

# Period is a datetime

# Create a new column for year

df['Year'] = df['Period'].map(lambda x: x.year)

# Below 'where' clause for year 2007
df[(df['Year'] == 2007)]

# Below, groupby Gender giving mean of Unemployed
df.groupby(['Gender'])['Unemployed'].agg(['mean'])

# Combined both, in 2007, groupyb Gender and display average Unemployed
gender_unemp = df[(df['Year'] == 2007)].groupby(['Gender'])['Unemployed'].agg(['mean'])

'''                 mean
Gender
Men     100845.238095
Women    87000.000000
'''
# Men had the higher avg unemployment, but how to return the max of above?

higher_gender = gender_unemp.idxmax()['mean']

print(higher_gender + ' had the highest average unemployment in 2007')

# Question 2

# Create a new column for Month
df['Month'] = df['Period'].map(lambda x: x.month)

# Below 'where' clause for Women
df[(df['Gender'] == 'Women')]

# Below, groupby Month giving mean of Unemployed
df.groupby(['Month'])['Unemployed'].agg(['mean'])

# Combined both, in 2007, groupyb Gender and display average Unemployed
df[(df['Gender'] == 'Women')].groupby(['Month'])['Unemployed'].agg(['mean'])

month_unemp = df[(df['Gender'] == 'Women')].groupby(['Month'])['Unemployed'].agg(['mean'])

import calendar

new_month_unemp = month_unemp.reset_index()

new_month_unemp['Month'] = new_month_unemp['Month'].apply(lambda x: calendar.month_abbr[x])

best_month = month_unemp.idxmin()['mean']

print(str(best_month) + ' is the month in which women have the lowest average unemployment')
