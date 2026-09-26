
import pandas as pd

data={
    "name":['Ram','Shyam',None,'Rahul','Tanmay'],
    "age":[42,25,37,44,25],
    "Salary":[50000,20000,None,30000,25000],
    "city":['Mumbai',None,'Delhi','Raipur','Merut'],
    "Performance score":[10,6,7,8,9]
}

df=pd.DataFrame(data)

# df.dropna(inplace=True)
# df.fillna(0, inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)