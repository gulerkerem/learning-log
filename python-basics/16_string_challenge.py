orders = [
    "  ORD-901 | alexander SMITH | 120.50 | completed  ",
    "ORD-902 | ELENA rodrigues | 45.00 | cancelled ",
    " ord-903 | MARCUS johnson | 210.00 | COMPLETED",
    "ORD-904 | SARAH lee | 85.25 | pending ",
    "   ORD-905 | hannah WHITE | 310.00 | completed "
]

total_revenue = 0 

print("Completed Orders")
for order in orders:
    code, name, price, situation = [eleman.strip() for eleman in order.split("|")]
    name = name.title() #Hem adını hem de soy adının ilk harifini büyütüyor burası
    code = code.upper()

    if situation.lower() == "completed":
        price_float = float(price)
        total_revenue += price_float
    print(f"{name} {code} - {price_float:.2f}")

print(f"\nTotal Revenues:{total_revenue:.2f} TL")
    
