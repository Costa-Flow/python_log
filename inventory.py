# Interactive inventory calculator
product = input("Product name: ")
quantity = int(input("Quantity in stock: "))
unit_price = float(input("Unit price ($): "))

total_value = quantity * unit_price

print("----------------------------------------")
print(f"Total inventory value for {product}: ${total_value:.2f}")
