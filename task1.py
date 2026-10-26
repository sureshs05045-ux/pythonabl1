print("CAMPUS EVENT BUDGET")

try:
    venue = float(input("Venue cost: Rs. "))
    equipment = float(input("Equipment cost: Rs. "))
    transport = float(input("Transport cost: Rs. "))
    catering = float(input("Catering cost per participant: Rs. "))
    certificate = float(input("Certificate cost per participant: Rs. "))
    registration_fee = float(input("Registration fee per participant: Rs. "))
    participants = int(input("Expected number of participants: "))
    sponsorship = float(input("Sponsorship amount: Rs. "))

    values = [venue, equipment, transport, catering, certificate,
              registration_fee, sponsorship]

    if min(values) < 0 or participants < 0:
        print("Error: Costs and participant count cannot be negative.")
    else:
        fixed_cost = venue + equipment + transport
        cost_per_participant = catering + certificate
        total_cost = fixed_cost + cost_per_participant * participants
        contributions = registration_fee * participants
        total_funds = contributions + sponsorship
        shortfall = total_cost - total_funds

        # Break-even registrations = fixed costs left after sponsorship
        # divided by the amount each participant contributes after costs.
        needed = fixed_cost - sponsorship
        contribution_per_person = registration_fee - cost_per_participant

        if needed <= 0:
            break_even_count = 0
        elif contribution_per_person <= 0:
            break_even_count = None
        else:
            break_even_count = int(needed / contribution_per_person)
            if break_even_count * contribution_per_person < needed:
                break_even_count += 1

        print("\n--- EVENT SUMMARY ---")
        print(f"Total event cost:        Rs. {total_cost:.2f}")
        print(f"Participant contributions: Rs. {contributions:.2f}")
        print(f"Sponsorship:             Rs. {sponsorship:.2f}")

        if shortfall > 0:
            print(f"Funding shortfall:       Rs. {shortfall:.2f}")
        else:
            print(f"Surplus:                 Rs. {-shortfall:.2f}")

        if break_even_count is None:
            print("Break-even is not possible with this registration fee.")
        else:
            print(f"Registrations needed to break even: {break_even_count}")

except ValueError:
    print("Error: Enter valid numbers.")
