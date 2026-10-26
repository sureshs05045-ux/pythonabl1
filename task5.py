print("EMPLOYEE PAYROLL")

try:
    basic_pay = float(input("Enter basic pay: Rs. "))
    allowances = float(input("Enter total allowances: Rs. "))
    overtime_hours = float(input("Enter overtime hours: "))
    overtime_rate = float(input("Enter overtime rate per hour: Rs. "))
    incentives = float(input("Enter incentives: Rs. "))

    if (basic_pay < 0 or allowances < 0 or overtime_hours < 0
            or overtime_rate < 0 or incentives < 0):
        print("Error: Values cannot be negative.")
    else:
        overtime_pay = overtime_hours * overtime_rate
        gross_salary = basic_pay + allowances + overtime_pay + incentives

        
        if gross_salary <= 10000:
            tax = 0
        elif gross_salary <= 30000:
            tax = (gross_salary - 10000) * 0.05
        else:
            tax = (20000 * 0.05) + ((gross_salary - 30000) * 0.10)

        net_salary = gross_salary - tax

        print("\n------ SALARY STATEMENT ------")
        print(f"Basic pay:       Rs. {basic_pay:.2f}")
        print(f"Allowances:      Rs. {allowances:.2f}")
        print(f"Overtime pay:    Rs. {overtime_pay:.2f}")
        print(f"Incentives:      Rs. {incentives:.2f}")
        print(f"Gross salary:    Rs. {gross_salary:.2f}")
        print(f"Tax deduction:   Rs. {tax:.2f}")
        print(f"Net salary:      Rs. {net_salary:.2f}")

except ValueError:
    print("Error: Please enter a valid number.")
