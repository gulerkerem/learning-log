import pandas as pd
import numpy as np

# Ham ve kirli veri
raw_data = {
    "Product Name": [" Laptop ", "Mouse", "Keyboard", "Laptop", "Monitor ", "Mouse", "Tablet", "Phone"],
    "Price": ["1500", "50", "100", "1500", np.nan, "50", "300", "800"],
    "Stock Status": ["yes", "no", "yes", "yes", "yes", "no", np.nan, "no"],
    "Discount": [10, 5, np.nan, 10, 15, 5, 20, np.nan]
}

df = pd.DataFrame(raw_data)

df["Product Name"] = df["Product Name"].str.strip()
df = df.drop_duplicates()
df["Price"] = pd.to_numeric(df["Price"])
df["Price"] = df["Price"].fillna(df["Price"].median())
df["Stock Status"] = df["Stock Status"].fillna("unknown")
df["Discount"] = df["Discount"].fillna(0)
df["Price"] = df["Price"].astype(int)
df = df.rename(columns={"Product Name": "product_name",
"Price": "price",
"Stock Status": "stock_status",
"Discount": "discount"})

print(df)
print(df.info())