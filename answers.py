import pandas as pd 

df = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')

# Question 1:
# In 2007, which gender (man, woman) had higher average unemployment?

df2 = df[(df.Period < '2008-01-01') & (df.Period > '2006-12-01')]

df2.groupby(['Gender']).mean()

# Men had the highest avg. unemployment  
#           Unemployed  
# Gender
# Men     100845.238095  
# Women    87000.000000  


# Question 2:
# What month, on average, has the lowest unemployment for women?

women = df[(df.Gender == 'Women')]  
women['month'] = women.Period.dt.month  
bymonth = women.groupby('month')['Unemployed'].agg(['mean'])  
bymonth.sort_values('mean', ascending=True)  
