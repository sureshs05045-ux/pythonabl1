print("EXAMINATION RESULT")

# Sample policy: each subject is out of 100, pass mark is 40,
# and up to 5 grace marks can be added to a subject.
PASS_MARK = 40
MAX_MARKS = 100
MAX_GRACE = 5

try:
    subject_count = int(input("Enter number of subjects: "))

    if subject_count <= 0:
        print("Error: Enter at least one subject.")
    else:
        marks_list = []

        for number in range(1, subject_count + 1):
            marks = float(input(f"Enter marks for subject {number} (out of 100): "))

            if marks < 0 or marks > MAX_MARKS:
                print("Error: Marks must be between 0 and 100.")
                marks_list = []
                break

            marks_list.append(marks)

        if marks_list:
            grace_used = 0
            final_marks = []
            failed_subjects = 0

            for marks in marks_list:
                # Add grace marks only to a subject that is just below passing.
                needed = PASS_MARK - marks
                if 0 < needed <= MAX_GRACE and grace_used + needed <= MAX_GRACE:
                    marks += needed
                    grace_used += needed

                # Keep the final mark within the subject's maximum.
                marks = min(marks, MAX_MARKS)
                final_marks.append(marks)

                if marks < PASS_MARK:
                    failed_subjects += 1

            total = sum(final_marks)
            percentage = total / subject_count

            print("\n--- RESULT ---")
            for number in range(subject_count):
                print(
                    f"Subject {number + 1}: "
                    f"{marks_list[number]:g} marks, "
                    f"final {final_marks[number]:g}/100"
                )

            print(f"Grace marks used: {grace_used}")
            print(f"Total marks: {total:g}/{subject_count * MAX_MARKS}")
            print(f"Percentage: {percentage:.2f}%")

            if failed_subjects == 0:
                if percentage >= 75:
                    classification = "First Class with Distinction"
                elif percentage >= 60:
                    classification = "First Class"
                elif percentage >= 50:
                    classification = "Second Class"
                else:
                    classification = "Pass"
                print("Result: PASS")
                print("Classification:", classification)
            else:
                print("Result: FAIL")
                print("Failed subjects:", failed_subjects)

except ValueError:
    print("Error: Enter valid numbers for subject count and marks.")