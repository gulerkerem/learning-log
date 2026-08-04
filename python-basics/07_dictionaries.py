product = {
"name" : "Economics of Turkey",
"price" : 8.99,
"in_stock" : True
}
for key, value in product.items():
    print(f"{key}: {value}")
product["category"] = "Economics"
product["price"] = 9.99
print(product)