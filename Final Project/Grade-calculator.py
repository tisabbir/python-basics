def get_marks():
    marks = []
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter the mark for subject {i + 1} (0-100): "))
                if mark < 0 or mark > 100:
                    raise ValueError
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 100.")
    return marks

def calculate_total_and_percentage(marks):
    total = sum(marks)
    percentage = (total / 500) * 100
    return total, percentage

def determine_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def main():
    marks = get_marks()
    total, percentage = calculate_total_and_percentage(marks)
    grade = determine_grade(percentage)

    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
