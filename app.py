import pandas as pd

# df=pd.read_csv('C:\\Users\\Tanmay\\Desktop\\Panda\\sales_data_130_rows.csv')
# print(df)
df2=pd.read_excel("C:\\Users\\Tanmay\\Desktop\\Panda\\Sample_Superstore_125_Rows - Copy.xlsx")
df3=pd.read_json("C:\\Users\\Tanmay\\Desktop\\Panda\\sample_Data.json")

#print(df2)
#print(df3)

# df.to_csv("output.csv",index=False)

data={
    "name":['Ram','Shyam','Ghanshyam'],
    "age":[42,25,37],
    "city":['Mumbai','Agra','Delhi']
}

dfd=pd.DataFrame(data)
print(dfd)
print(dfd.info())