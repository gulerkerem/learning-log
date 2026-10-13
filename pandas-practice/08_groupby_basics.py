import pandas as pd
import numpy as np

sales_data = {
    "branch": ["Ankara", "Istanbul", "Ankara", "Izmir", "Istanbul", "Izmir"],
    "department": ["Electronics", "Electronics", "Clothing", "Clothing", "Clothing", "Electronics"],
    "sales_amount": [5000, 12000, 3000, 4000, 7000, 9000]
}
df = pd.DataFrame(sales_data)

sales_amount = df.groupby("branch")["sales_amount"].sum()
branch_summary = df.groupby("department")["sales_amount"].agg(["mean", "max", "count"])
print(branch_summary)
print(sales_amount)