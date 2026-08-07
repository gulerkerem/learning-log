import pandas as pd
data = {
    "item" : ["Car", "Phone", "Car", "Earphone", "Watch", "Phone", "Computer", "Car"],
    "price" : [25000, 999, 25000, 399, 500, 999, 3000, 25000],
}
df = pd.DataFrame(data)
print(df.duplicated())
print(df.duplicated().sum())
df_unique = df.drop_duplicates()
print(df_unique)
print(len(df)) 
print(len(df_unique))
