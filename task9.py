"""Simple campus festival registration and finance audit."""


def read_amount(message):
    while True:
        try:
            amount = int(input(message))
            if amount >= 0:
                return amount
        except ValueError:
            pass
        print("Please enter a whole number that is zero or more.")


print("CAMPUS FESTIVAL AUDIT")
print("Enter all money amounts in whole rupees.\n")

participants = []
registered_ids = set()
duplicate_ids = []
registration_total = 0

participant_count = read_amount("How many registrations will you enter? ")

for number in range(participant_count):
    print("\nRegistration", number + 1)
    student_id = input("Student ID: ").strip()
    while not student_id:
        print("Student ID cannot be empty.")
        student_id = input("Student ID: ").strip()

    if student_id in registered_ids:
        duplicate_ids.append(student_id)
        print("Duplicate registration found. This entry will not be counted.")
        continue

    name = input("Student name: ").strip()
    fee = read_amount("Registration fee paid (rupees): ")

    registered_ids.add(student_id)
    participants.append((student_id, name, fee))
    registration_total += fee

print("\nSPONSORSHIPS")
sponsorship_total = 0
sponsor_count = read_amount("How many sponsorships were received? ")

for number in range(sponsor_count):
    sponsor = input("Sponsor name: ").strip()
    amount = read_amount("Contribution from " + sponsor + " (rupees): ")
    sponsorship_total += amount

print("\nEXPENSES")
expense_total = 0
expense_count = read_amount("How many expenses were paid? ")

for number in range(expense_count):
    expense = input("Expense description: ").strip()
    amount = read_amount("Cost of " + expense + " (rupees): ")
    expense_total += amount

income_total = registration_total + sponsorship_total
balance = income_total - expense_total

print("\nAUDIT SUMMARY")
print("Unique participants:", len(participants))
for student_id, name, fee in participants:
    print("-", student_id, name, "- fee:", fee, "rupees")

if duplicate_ids:
    print("Duplicate student IDs:", ", ".join(duplicate_ids))
else:
    print("Duplicate registrations: None")

print("Registration fees:", registration_total, "rupees")
print("Sponsorships:", sponsorship_total, "rupees")
print("Total income:", income_total, "rupees")
print("Total expenses:", expense_total, "rupees")
print("Final balance:", balance, "rupees")

if balance > 0:
    print("Result: Festival has a surplus.")
elif balance < 0:
    print("Result: Festival has a deficit.")
else:
    print("Result: Income and expenses are equal.")