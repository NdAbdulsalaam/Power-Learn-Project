def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price after applying the discount, or the original price if no discount was applied
if final_price != original_price:
    print(f"Final price after applying {discount_percentage}% discount: ${final_price:.2f}")
else:
    print("No discount applied. Original price: ${:.2f}".format(original_price))
