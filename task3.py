print("HOSPITAL BILLING")

try:
    consultation = float(input("Consultation charge: "))
    diagnostic = float(input("Diagnostic charge: "))
    treatment = float(input("Treatment charge: "))

    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Error: charges cannot be negative.")
    else:
        total = consultation + diagnostic + treatment
        senior = input("Is the patient a senior citizen? (yes/no): ").lower()

        if senior == "yes":
            concession = total * 0.10
        elif senior == "no":
            concession = 0
        else:
            print("Error: enter yes or no.")
            concession = None

        if concession is not None:
            final_bill = total - concession
            print("\n--- BILL ---")
            print(f"Total charges:  Rs. {total:.2f}")
            print(f"Concession:     Rs. {concession:.2f}")
            print(f"Amount payable: Rs. {final_bill:.2f}")

            paid = float(input("Amount paid: Rs. "))

            if paid < 0:
                print("Error: payment cannot be negative.")
            elif paid > final_bill:
                print("Error: payment cannot be more than the amount payable.")
            else:
                balance = final_bill - paid

                if balance == 0:
                    classification = "Fully paid"
                elif paid == 0:
                    classification = "Unpaid"
                else:
                    classification = "Partially paid"

                print(f"Balance due:   Rs. {balance:.2f}")
                print(f"Patient classification: {classification}")
except ValueError:
    print("Error: please enter a valid number for charges and payment.")