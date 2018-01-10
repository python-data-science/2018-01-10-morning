""" 
    This is the answer to the question
"""
# Answer #1
import pandas as pd
import numpy as np

df = pd.read_excel('Long-Term-Unemployment-Statistics.xlsx')
df['Year']=df.Period.dt.year
df_year = df[df.Year ==  2007]
df_year_gender = df_year.groupby(['Gender','Year'])['Unemployed'].sum()
"""
Answer = Gender  Year
         Men     2007    8471000
"""

# Answer #2
df['Month']=df.Period.dt.month
df_women = df[df.Gender == 'Women']
df_women_month = df_women.groupby(['Month'])['Unemployed'].sum()

"""
Answer in March
3     15485000



"""


