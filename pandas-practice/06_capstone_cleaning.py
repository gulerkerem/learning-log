import pandas as pd

df = pd.read_csv("/Users/keremguler/learning-log/pandas-practice/messy_inventory.csv")
print(df.info())
print(df.head())
print(df)

df["Item Name"] = df["Item Name"].str.strip()
df["In Stock"] = df["In Stock"].str.lower()

print(df)
print(df.isna().sum())

df = df.fillna(0)
print(df)

df["Price"] = df["Price"].astype(int)
print(df)
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df)

df = df.rename(columns={"Item Name" : "item_name", "In Stock" : "in_stock"})
print(df)

df.to_csv("/Users/keremguler/learning-log/pandas-practice/cleaned_inventory.csv", index=False)