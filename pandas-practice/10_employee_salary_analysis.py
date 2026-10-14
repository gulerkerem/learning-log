import pandas as pd
import numpy as np

employee_data = {
    "Full Name": [" Ali Candan ", "Zeynep Kaya", "Ali Candan", "Ahmet Yılmaz", " Elif Demir ", "Zeynep Kaya", "Burak Çelik"],
    "Department": ["IT", "HR", "IT", "Finance", np.nan, "HR", "IT"],
    "Salary": ["45000", "35000", "45000", "50000", np.nan, "35000", "42000"],
    "Performance Score": [85, 90, 85, np.nan, 75, 90, 80]
}

df = pd.DataFrame(employee_data)
df["Full Name"] = df["Full Name"].str.strip()
df = df.drop_duplicates()
df["Department"] = df["Department"].fillna("Unassigned")
df["Salary"] = pd.to_numeric(df["Salary"])
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Performance Score"] = df["Performance Score"].fillna(70)
df["Salary"] = df["Salary"].astype(int)
df = df.rename(columns=lambda x: x.lower().replace(" ", "_"))
summary = df.groupby("department")[["salary", "performance_score"]].agg({
    "salary": "mean",
    "performance_score": "max"
})
print("---Cleaned Data Set---")
print(df)
print("---Department Summary---")
print(summary)

