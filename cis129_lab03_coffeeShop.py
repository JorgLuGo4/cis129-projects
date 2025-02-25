# Prices
coffee_price = 5
muffin_price = 4
tax_rate = 0.06

# User Input
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))

# Calculate coffee and muffins
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price

# Calculate before tax
subtotal = subtotal_coffee + subtotal_muffin

# Calculate the tax
tax = subtotal * tax_rate

# Calculate the total with tax
total = subtotal + tax

# Display the formatted receipt
print("\n***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought?\n{num_coffees}")
print(f"Number of muffins bought?\n{num_muffins}")
print("***************************************")
print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee{'s' if num_coffees > 1 else ''} at ${coffee_price} each: ${subtotal_coffee:.2f}")
print(f"{num_muffins} Muffin{'s' if num_muffins > 1 else ''} at ${muffin_price} each: ${subtotal_muffin:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
