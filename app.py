def get_valid_grade(prompt):
    while True:
        value = input(prompt).strip()
        try:
            grade = float(value)
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")

def main():
    print("=" * 40)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 40)

    while True:
        name = get_non_empty("Enter Student Name: ")
        student_id = get_non_empty("Enter Student ID: ")

        grades = []
        for i in range(1, 5):
            grades.append(get_valid_grade(f"Enter Grade {i}: "))

        average = sum(grades) / len(grades)
        status = "PASSED" if average >= 75 else "FAILED"

        print("=" * 40)
        print("STUDENT RESULT")
        print("=" * 40)
        print(f"Student Name : {name}")
        print(f"Student ID   : {student_id}")
        for i, g in enumerate(grades, 1):
            print(f"Grade {i}      : {g}")
        print(f"Average      : {average:.2f}")
        print(f"Status       : {status}")
        print("=" * 40)

        again = input("Process another student? (Y/N): ").strip().upper()
        if again != "Y":
            print("Exiting application. Goodbye!")
            break

if __name__ == "__main__":
    main()
