import pandas as pd
import to_datetime

df=pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')
#Question 1:
#In 2007, which gender (man, woman) had higher average unemployment?

df['Period1']=pd.to_datetime(df.Period)
df2007= df[(df.Period1 >= '2007-01-01') & (df.Period1 <= '2007-12-31') ]
gender=df2007.groupby(['Gender']).mean()
hi_unemploy = gender.idxmax()['Unemployed']



#Question 2:
#What month, on average, has the lowest unemployment for women?
dfwomen=df[(df.Gender == 'Women')]
dfwomen['month']=dfwomen['Period1'].dt.month
monthgrp=dfwomen.groupby(['month']).mean()
lo_unemploy = monthgrp.idxmin()['Unemployed']
