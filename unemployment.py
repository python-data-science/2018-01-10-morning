import pandas as pd
df = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx') 


"""
Question 1:
In 2007, which gender (man, woman) had higher average unemployment?

ANSWER: MEN
"""

df['Period'] = pd.to_datetime(df.Period)
df2017 = df[(df.Period > '2006-12-31') & (df.Period < '2008-01-01')]
dfgender = df2017.groupby(['Gender']).mean()
dfgender.loc[dfgender['Unemployed'].idxmax()]

genderanswer = dfgender.index[0]
print(genderanswer, "have higher unemployment rates")

"""
Question 2:
What month, on average, has the lowest unemployment for women?

ANSWER: Month 2
"""

dfwomen = df[df.Gender == 'Women']
dfwomen['Month'] = dfwomen['Period'].dt.month

dfmonth = dfwomen.groupby(['Month']).mean()
dfmonth.loc[dfmonth['Unemployed'].idxmin()]

monthanswer = dfmonth.index[1]
print("Month", monthanswer, "has the lowest unemployment rate for women")
