import pandas as pd

# df = pd.read_csv(r'C:\Users\Tanmay\Desktop\Panda\sales_data_130_rows.csv')

# print("First 5 rows")
# print(df.head())

# print("last 5 rows")
# print(df.tail())

# print(df.info())


data={
    "name":['Ram','Shyam','Ghanshyam','Rahul','Tanmay'],
    "age":[42,25,37,44,25],
    "city":['Mumbai','Agra','Delhi','Raipur','Merut'],
    "Performance score":[10,6,7,8,9]
}

df=pd.DataFrame(data)
# print(df.describe())
# print(f'Shape:{df.shape}')
# print(f'Column name: {df.columns}')

#how to select single and multiple columns

print(df["name"])
print(df[["name", "age"]])

#condition or filtyering data

high_age=df[df["age"]>30]
print(high_age)

new=df[(df["age"]>30 ) & (df["Performance score"]>7)]
print(new)