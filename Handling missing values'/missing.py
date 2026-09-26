#NaN==not a number
#null

import pandas as pd

data={
    "name":['Ram','Shyam',None,'Rahul','Tanmay'],
    "age":[42,25,37,44,25],
    "Salary":[None,20000,50000,30000,25000],
    "city":['Mumbai',None,'Delhi','Raipur','Merut'],
    "Performance score":[10,6,7,8,9]
}

df=pd.DataFrame(data)
print(df.isnull())
#will return how many null values in each column
print(df.isnull().sum())

