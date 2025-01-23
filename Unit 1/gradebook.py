import statistics

def main():
    # Step 1: Ask for the total number of students
    total_students = int(input("Enter the total number of students: "))

    # Step 2: Ask for the total assignment value
    total_assignment_value = float(input("Enter the total assignment value (e.g., 100): "))

    # Step 3: Collect marks and student names
    student_marks = {}
    for _ in range(total_students):
        name = input("Enter the student's name: ")
        mark = float(input(f"Enter the mark for {name}: "))
        percentage = (mark / total_assignment_value) * 100
        student_marks[name] = percentage

    # Step 6: Display results
    print("\nClass Results:")
    for name, percentage in student_marks.items():
        print(f"{name}: {percentage:.2f}%")

    # Step 7: Calculate mean, median, and mode
    percentages = list(student_marks.values())
    mean = statistics.mean(percentages)
    median = statistics.median(percentages)
    try:
        mode = statistics.mode(percentages)
    except statistics.StatisticsError:
        mode = "No unique mode"

    print("\nClass Statistics:")
    print(f"Mean: {mean:.2f}%")
    print(f"Median: {median:.2f}%")
    print(f"Mode: {mode}")

if __name__ == "__main__":
    main()