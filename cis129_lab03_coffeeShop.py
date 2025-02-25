# Define the prices for the items
coffee_price = 5
muffin_price = 4
croissant_price = 3
tea_price = 2
tax_rate = 0.06

# Ask the user for input (number of items)
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_croissants = int(input("Number of croissants bought? "))
num_teas = int(input("Number of teas bought? "))

# Calculate the subtotal for each item
subtotal_coffee = num_coffees * coffee_price
subtotal_muffin = num_muffins * muffin_price
subtotal_croissant = num_croissants * croissant_price
subtotal_tea = num_teas * tea_price

# Calculate the total before tax
subtotal = subtotal_coffee + subtotal_muffin + subtotal_croissant + subtotal_tea

# Calculate the tax
tax = subtotal * tax_rate

# Calculate the total with tax
total = subtotal + tax

# Display the formatted receipt
print("\n***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought?\n{num_coffees}")
print(f"Number of muffins bought?\n{num_muffins}")
print(f"Number of croissants bought?\n{num_croissants}")
print(f"Number of teas bought?\n{num_teas}")
print("***************************************")
print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
if num_coffees > 0:
    print(f"{num_coffees} Coffee{'s' if num_coffees > 1 else ''} at ${coffee_price} each: ${subtotal_coffee:.2f}")
if num_muffins > 0:
    print(f"{num_muffins} Muffin{'s' if num_muffins > 1 else ''} at ${muffin_price} each: ${subtotal_muffin:.2f}")
if num_croissants > 0:
    print(f"{num_croissants} Croissant{'s' if num_croissants > 1 else ''} at ${croissant_price} each: ${subtotal_croissant:.2f}")
if num_teas > 0:
    print(f"{num_teas} Tea{'s' if num_teas > 1 else ''} at ${tea_price} each: ${subtotal_tea:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")

# Thank the customer
print("\nThank you for visiting My Coffee and Muffin Shop!")
