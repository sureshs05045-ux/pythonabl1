
print("CAMPUS FESTIVAL REGISTRATION AND FINANCE AUDIT")

# Registration details
participants = []
student_ids = []
registration_total = 0

participant_count = int(input("Enter number of participants: "))

for i in range(participant_count):
    print("\nRegistration", i + 1)

    student_id = input("Enter Student ID: ")

    if student_id in student_ids:
        print("Duplicate registration. Not counted.")

    else:
        student_ids.append(student_id)

        name = input("Enter Student Name: ")
        fee = int(input("Enter Registration Fee: "))

        participants.append(name)
        registration_total = registration_total + fee


# Sponsorship details
print("\nSPONSORSHIP DETAILS")

sponsorship_count = int(input("Enter number of sponsors: "))
sponsorship_total = 0

for i in range(sponsorship_count):
    sponsor = input("Enter Sponsor Name: ")
    amount = int(input("Enter Sponsorship Amount: "))

    sponsorship_total = sponsorship_total + amount


# Expense details
print("\nEXPENSE DETAILS")

expense_count = int(input("Enter number of expenses: "))
expense_total = 0

for i in range(expense_count):
    expense = input("Enter Expense Name: ")
    cost = int(input("Enter Expense Amount: "))

    expense_total = expense_total + cost


# Financial calculation
total_income = registration_total + sponsorship_total
balance = total_income - expense_total


# Audit summary
print("\n===== AUDIT SUMMARY =====")

print("Total Participants:", len(participants))
print("Registration Fees:", registration_total)
print("Sponsorship Amount:", sponsorship_total)
print("Total Income:", total_income)
print("Total Expenses:", expense_total)
print("Final Balance:", balance)


# IF ELSE CONDITIONS
if balance > 0:
    print("Result: Festival has a Surplus.")

elif balance < 0:
    print("Result: Festival has a Deficit.")

else:
    print("Result: Income and Expenses are Equal.")
