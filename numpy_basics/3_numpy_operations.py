# Lines: Branch 0, Branch 1, Branch 2
# Column: Q1, Q2, Q3, Q4
import numpy as np
sales = np.array([
    [100, 120, 110, 130],  # Branch 0
    [80,  90,  95,  100],  # Branch 1
    [150, 160, 170, 180]   # Branch 2
])

quarterly_totals = np.sum(sales, axis=0)
branch_totals = np.sum(sales, axis=1)
print(f"Quarterly total revenue:{quarterly_totals}\nBranch total revenue:{branch_totals}")



# Lines: Department 0 (Software), Department 1 (Marketing), Department 2 (Sale)
# Column: Employee 0, Employee 1, Employee 2, Employee 3
bonus_matrix = np.array([
    [15, 22, 18, 30],  # Software
    [10, 12, 25, 14],  # Marketing
    [28, 35, 19, 40]   # Sale
])

dept_means = np.mean(bonus_matrix, axis=1)
max_bonuses_per_col = np.max(bonus_matrix, axis=0)
overall_mean = np.mean(bonus_matrix)
high_bonuses = bonus_matrix[bonus_matrix > overall_mean]

print(f"Department mean:{dept_means}\nMax bonuses per position:{max_bonuses_per_col}\nOverall mean:{overall_mean}\nHigh Bonuses:{high_bonuses}")
