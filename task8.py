print("MANUFACTURING COST AND PROFIT")

try:
    quantity = int(input("Enter number of products made: "))
    material_cost = float(input("Enter total material cost: Rs. "))
    labour_cost = float(input("Enter total labour cost: Rs. "))
    wastage_percent = float(input("Enter wastage percentage: "))
    machine_cost = float(input("Enter machine cost: Rs. "))
    selling_price = float(input("Enter selling price per product: Rs. "))
    profit_target = float(input("Enter required profit target: Rs. "))

    if (quantity <= 0 or material_cost < 0 or labour_cost < 0
            or machine_cost < 0 or selling_price < 0
            or profit_target < 0 or wastage_percent < 0):
        print("Error: Quantity must be positive; costs and percentages cannot be negative.")
    else:
        # Wastage cost is calculated as a percentage of material cost.
        wastage_cost = material_cost * wastage_percent / 100
        total_cost = material_cost + labour_cost + wastage_cost + machine_cost
        total_revenue = selling_price * quantity
        profit = total_revenue - total_cost

        print("\n------ PRODUCTION REPORT ------")
        print(f"Material cost:       Rs. {material_cost:.2f}")
        print(f"Labour cost:         Rs. {labour_cost:.2f}")
        print(f"Wastage cost:        Rs. {wastage_cost:.2f}")
        print(f"Machine cost:        Rs. {machine_cost:.2f}")
        print(f"Total production cost: Rs. {total_cost:.2f}")
        print(f"Total selling amount:  Rs. {total_revenue:.2f}")
        print(f"Profit/Loss:           Rs. {profit:.2f}")

        if profit >= profit_target:
            print("Result: Profit target achieved.")
        else:
            print("Result: Profit target not achieved.")

except ValueError:
    print("Error: Please enter valid numbers.")