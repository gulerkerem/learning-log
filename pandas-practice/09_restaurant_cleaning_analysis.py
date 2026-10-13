import pandas as pd
import numpy as np

restaurant_data = {
    "Customer Name": [" Ahmet Y. ", "Ayşe K.", "Ahmet Y.", "Mehmet D.", "Can S. ", "Ayşe K.", "Zeynep B."],
    "Day": ["Friday", "Saturday", "Friday", "Sunday", "Saturday", "Saturday", np.nan],
    "Bill Amount": ["450.5", "300", "450.5", np.nan, "1250", "300", "750"],
    "Tip": [50, 30, 50, 20, np.nan, 30, 80]
}

df = pd.DataFrame(restaurant_data)

df["Customer Name"] = df["Customer Name"].str.strip()
df = df.drop_duplicates()
df["Day"] = df["Day"].fillna("Unknown")
df["Bill Amount"] = pd.to_numeric(df["Bill Amount"])
df["Bill Amount"] = df["Bill Amount"].fillna(df["Bill Amount"].median())
df["Tip"] = df["Tip"].fillna(0)
df["Bill Amount"] = df["Bill Amount"].astype(float)
df = df.rename(columns= lambda x: x.lower().replace(" ", "_"))
tip = df.groupby("day")[["bill_amount", "tip"]].agg(["mean","sum"])

print("---Cleaned Data Set---")
print(df)
print("\n--- Daily Summary Report---")
print(df)
