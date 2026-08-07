import pandas as pd 
data = {
    "item" : ["Computer", "Car", "Phone"],
    "price" : ["3000", "1000", "25000"],
    "in_stock" : [1, 0, 1]
}

df = pd.DataFrame(data)
print(df.dtypes)

df["price"] = df["price"].astype(int)
df["in_stock"] = df["in_stock"].astype(bool)

print(df.dtypes)

df = df.rename(columns={"item": "product_name", "price" : "price_in_euro"})
print(df)
