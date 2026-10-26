print("RETAIL BILLING")

# Sample tax rates and discount policy. Change them to match your assignment.
tax_rates = {
    "food": 0.05,
    "clothing": 0.05,
    "electronics": 0.18
}
discount_threshold = 5000
discount_rate = 0.10
maximum_discount = 1000

try:
    product_count = int(input("How many products? "))

    if product_count <= 0:
        print("Enter at least one product.")
    else:
        products = []
        subtotal = 0
        total_tax = 0

        for number in range(1, product_count + 1):
            print("\nProduct", number)
            name = input("Product name: ")
            category = input(
                "Category (food, clothing, electronics): "
            ).lower()
            price = float(input("Price per item: Rs. "))
            quantity = int(input("Quantity: "))

            if category not in tax_rates:
                print("Unknown category. This product was not added.")
                continue

            if price < 0 or quantity <= 0:
                print("Price must not be negative and quantity must be positive.")
                continue

            amount = price * quantity
            tax = amount * tax_rates[category]
            subtotal += amount
            total_tax += tax
            products.append((name, quantity, price, amount, tax))

        if len(products) == 0:
            print("No valid products were entered.")
        else:
            if subtotal >= discount_threshold:
                discount = subtotal * discount_rate
                if discount > maximum_discount:
                    discount = maximum_discount
            else:
                discount = 0

            final_total = subtotal + total_tax - discount

            print("\n-------------- INVOICE --------------")
            print("Product          Qty   Price    Amount     Tax")
            for name, quantity, price, amount, tax in products:
                print(
                    f"{name:<16} {quantity:<5} "
                    f"{price:>7.2f} {amount:>9.2f} {tax:>8.2f}"
                )

            print("-------------------------------------")
            print(f"Subtotal:          Rs. {subtotal:.2f}")
            print(f"Category taxes:    Rs. {total_tax:.2f}")
            print(f"Discount:          Rs. {discount:.2f}")
            print(f"Amount to pay:     Rs. {final_total:.2f}")

except ValueError:
    print("Error: Enter a valid number for product count, price, and quantity.")