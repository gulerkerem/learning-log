import pandas as pd

data = {
    "item": ["Computer", "Car", "Phone"],
    "price": [3000, 25000, 1000],
    "stock": ["yes", "no", "yes"],
    "Tax Ratio": [5, 12, 6]
}

df = pd.DataFrame(data)
print(df["item"])
print(df[["stock", "item"]])
print(df[df["price"] > 2000])
print(df[df["stock"] == "yes"]) 