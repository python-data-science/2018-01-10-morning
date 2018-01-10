import pandas as pd

df = pd.read_excel("Long-Term-Unemployment-Statistics.xlsx")

 #df["Period"] = pd.to_datetime(df["Period"])
question1 = df[(df["Period"] > "2006-12-31") & (df["Period"] < "2008-01-01")].groupby(["Gender"]).sum()
print("QUESTION ONE")
print(question1)
print()

df["month"] = df["Period"].dt.month
question2 = df[df["Gender"] == "Women"].groupby("month").sum().sort_values(by = ["Unemployed"], ascending = False).head(1)
print("QUESTION TWO")
print(question2)
