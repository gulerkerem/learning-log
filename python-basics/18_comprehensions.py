prices = [100, 250, 400, 80, 150]
bigger_numbers = [ price * 1.10 for price in prices if price >= 150 ]
print(f"New prices with tax: {bigger_numbers}")


products = ["laptop", "phone", "mouse"]
new_products = {product: len(product) for product in products}
print(f"Product lengths dict: {new_products}")