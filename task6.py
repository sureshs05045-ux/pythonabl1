print("RAILWAY FARE AND RESERVATION")

reservation_fee = 50
cancellation_rate = 0.25

try:
    distance = float(input("Enter journey distance in km: "))
    passenger_count = int(input("Enter number of passengers: "))

    if distance <= 0 or passenger_count <= 0:
        print("Error: Distance and passenger count must be greater than zero.")
    else:
        total_payable = 0
        total_refund = 0
        total_penalty = 0

        for passenger in range(1, passenger_count + 1):
            print("\nPassenger", passenger)
            age = int(input("Enter age: "))
            travel_class = input(
                "Enter class (sleeper, ac, first): "
            ).lower()

            if age < 0:
                print("Error: Age cannot be negative.")
                continue

            if travel_class == "sleeper":
                class_rate = 1
            elif travel_class == "ac":
                class_rate = 2
            elif travel_class == "first":
                class_rate = 3
            else:
                print("Invalid class. This passenger is skipped.")
                continue

            # Distance slab sets the basic fare per km.
            if distance <= 100:
                fare_per_km = 2
            elif distance <= 500:
                fare_per_km = 1.5
            else:
                fare_per_km = 1

            fare = distance * fare_per_km * class_rate

            # Sample age concessions: children under 12 get 50%;
            # senior citizens aged 60 or more get 40%.
            if age < 12:
                concession_rate = 0.50
            elif age >= 60:
                concession_rate = 0.40
            else:
                concession_rate = 0

            concession = fare * concession_rate
            discounted_fare = fare - concession
            ticket_total = discounted_fare + reservation_fee

            cancel = input("Cancel this ticket? (yes/no): ").lower()

            if cancel == "yes":
                # Reservation fee is non-refundable.
                penalty = discounted_fare * cancellation_rate
                refund = discounted_fare - penalty
                total_penalty += penalty
                total_refund += refund
                print(f"Cancellation penalty: Rs. {penalty:.2f}")
                print(f"Refund (reservation fee not returned): Rs. {refund:.2f}")
            elif cancel == "no":
                total_payable += ticket_total
                print(f"Fare before concession: Rs. {fare:.2f}")
                print(f"Age concession: Rs. {concession:.2f}")
                print(f"Reservation fee: Rs. {reservation_fee:.2f}")
                print(f"Amount payable: Rs. {ticket_total:.2f}")
            else:
                print("Invalid cancellation choice. This passenger is skipped.")

        print("\n------ JOURNEY SUMMARY ------")
        print(f"Total amount to pay: Rs. {total_payable:.2f}")
        print(f"Total cancellation penalties: Rs. {total_penalty:.2f}")
        print(f"Total refunds: Rs. {total_refund:.2f}")

except ValueError:
    print("Error: Please enter valid numbers for distance, passenger count, and age.")
