import pandas as pd

data={
    "name":['Ram','Shyam','Ghanshyam','Rahul','Tanmay'],
    "age":[42,25,37,44,25],
    "Salary":[10000,20000,50000,30000,25000],
    "city":['Mumbai','Agra','Delhi','Raipur','Merut'],
    "Performance score":[10,6,7,8,9]
}

df=pd.DataFrame(data)

#adding one column
df["Bonus"]=df["Salary"]*10
print(df)