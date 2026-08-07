import pandas as pd
import numpy as np 

data = {
    "item" : ["Computer", "Phone", "Car", "Earphones"],
    "price" : [3000, np.nan, 25000, 390],
    "stock" : ["yes", "no", np.nan, "yes"],
    "Tax Ratio" : [3, 5, 4, np.nan]
    }

df = pd.DataFrame(data)
print(df.isna())
print(df.isna().sum())
df_clean = df.dropna()
print(df_clean)
df_filled = df.fillna("Unknown")
print(df_filled)
