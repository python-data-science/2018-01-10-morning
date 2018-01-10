import pandas as pd
df = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')
df['Period'] = pd.to_datetime(df.Period) # Convert period to datetime

#Question 1: Answer is Men
#In 2007, which gender (man, woman) had higher average unemployment?
df2 = df[(df.Period > '2007-01-01') & (df.Period < '2007-12-31')][['Gender','Unemployed']]
df2.groupby(['Gender'])['Unemployed'].agg(['mean'])
#                  mean
# Gender
# Men     101792.207792
# Women    87038.961039

#Question 2:  Lowest Period was 2006-10-01.  Haven't been able to determine month.
#What month, on average, has the lowest unemployment for women?
df3 = df[df.Gender == 'Women'][['Gender','Period', 'Unemployed']]
df3.Unemployed.describe()

# count       854.000000
# mean     228925.058548
# std      162409.051846
# min       21000.000000
# 25%      100000.000000
# 50%      173000.000000
# 75%      329000.000000
# max      713000.000000
# Name: Unemployed, dtype: float64
df3[df3.Unemployed == 21000].Period
# 301   2006-10-01
# Name: Period, dtype: datetime64[ns]
