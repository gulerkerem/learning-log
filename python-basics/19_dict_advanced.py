transactions = [
    ("Electronics", 1200),
    ("Grocery", 50),
    ("Electronics", 300),
    ("Clothing", 100),
    ("Grocery", 80),
    ("Clothing", 40)
]
category_totals = {}
for category, amount in transactions:
    category_totals[category] = category_totals.get(category, 0) + amount

print("--Category Totals--")
for category, total in category_totals.items():
 print(f"{category}: ${total}")