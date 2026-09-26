import pandas as pd

data={
    "name":['Ram','Shyam','Ghanshyam','Rahul','Tanmay'],
    "age":[42,25,37,44,25],
    "Salary":[10000,20000,50000,30000,25000],
    "city":['Mumbai','Agra','Delhi','Raipur','Merut'],
    "Performance score":[10,6,7,8,9]
}

df=pd.DataFrame(data)
print(df)

#df.loc[row_index,"Column name"]=new data
df.loc[3,"Salary"]=55000
print(df)

df["Salary"]=df["Salary"]*1.5
print(df)

#how to change values of multiple columns