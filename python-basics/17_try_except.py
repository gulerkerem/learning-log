"""""
age_list = ["21", "30", "unknown", "19"]
for age_str in age_list:
    try:
        age_float = int(age_str)
        print(f"Succesfull: {age_float}")
    except ValueError:
        print(f"Not Successfull: {age_str}")
"""

raw_salaries = ["2500.50", "3200.00", "UNKNOWN", "4100.75", "NONE", "2900.00"]

valid_salaries = []
for salary_str in raw_salaries:
    try:
       salary_float = float(salary_str)
       valid_salaries.append(salary_float)
       print(f"Valid Salary: {salary_float:.2f}")
    except ValueError:
        print(f"Invalid Salary Skipped: {salary_str}")
if len(valid_salaries) > 0:
    average_salary = sum(valid_salaries) / len(valid_salaries)
    print(f"Average Salary: {average_salary:.2f}")