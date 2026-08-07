import pandas as pd

data = {
    "item": ["Computer", "Car", "Phone"],
    "price": [3000, 25000, 1000],
    "stock": ["yes", "no", "yes"]
}

df = pd.DataFrame(data)
print(df)
print(df.head(2))
print(df.info())