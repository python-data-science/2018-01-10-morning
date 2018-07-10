import pandas as pd
unemployment = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')
unemployment.head(5)

#first I split the Period into three columns, Year, Month and Day
unemployment['Year'] = unemployment['Period'].dt.year
unemployment['Month'] = unemployment['Period'].dt.month
unemployment['Day'] = unemployment['Period'].dt.day

#Now I Grouped the columns to answer the questions


#Question 1:
#In 2007, which gender (man, woman) had higher average unemployment?
only2007 = unemployment[unemployment.Year == 2007]
only2007.groupby(['Gender']).mean()

Answer:  In 2007, Men(100,845) had a higher average unemployment rate than Women(87,000)

#Question 2:
#What month, on average, has the lowest unemployment for women?
Ladiesonly = unemployment[unemployment.Gender == 'Women']
Answer = Ladiesonly.groupby(['Month'])['Unemployed'].agg(['mean']).nsmallest(1, 'mean')

Answer: February (02) is the month with the lowest mean unemployment for women (220,298)
