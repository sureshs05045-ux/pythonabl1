# Each inner list represents one classroom.
# "-" = vacant seat, "R" = reserved seat
classrooms = [
    ["-", "R", "-", "-"],
    ["-", "-", "R", "-"]
]

while True:
    student = input("\nEnter student name (or type 'stop' to finish): ").strip()

    if student.lower() == "stop":
        break

    if student == "":
        print("Student name cannot be empty.")
        continue

    # Check whether this student has already been assigned a seat.
    already_assigned = False
    for room in classrooms:
        for seat in room:
            if seat.lower() == student.lower():
                already_assigned = True

    if already_assigned:
        print("This student already has a seat.")
        continue

    try:
        room_number = int(input("Enter classroom number: "))
        seat_number = int(input("Enter seat number: "))
    except ValueError:
        print("Please enter numbers for the classroom and seat.")
        continue

    # Convert from numbers starting at 1 to list positions starting at 0.
    room_index = room_number - 1
    seat_index = seat_number - 1

    if room_index < 0 or room_index >= len(classrooms):
        print("That classroom does not exist.")
    elif seat_index < 0 or seat_index >= len(classrooms[room_index]):
        print("That seat does not exist.")
    elif classrooms[room_index][seat_index] == "R":
        print("That seat is reserved.")
    elif classrooms[room_index][seat_index] != "-":
        print("That seat is already occupied.")
    else:
        classrooms[room_index][seat_index] = student
        print("Student assigned successfully.")

# Display classrooms and count vacant seats.
vacant_seats = 0

print("\n--- CLASSROOM SEATING ---")
for room_index in range(len(classrooms)):
    print("Classroom", room_index + 1, ":", classrooms[room_index])

    for seat in classrooms[room_index]:
        if seat == "-":
            vacant_seats += 1

print("Number of vacant seats:", vacant_seats)