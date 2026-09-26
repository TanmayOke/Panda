import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,40,50]
}

df=pd.DataFrame(data)
df["Value"]=df["Value"].interpolate(method="linear",axis=0,inplace=True)
print(df)