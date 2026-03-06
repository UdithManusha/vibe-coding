def get_valid_mark(prompt):
    """Prompts for an integer mark and handles invalid input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer for the mark.")

def main():
    while True:
        # Ask for student's name
        name = input("\nEnter student's name (type 'Exit' to quit): ").strip()
        
        # Check for exit condition
        if name.lower() == 'exit':
            break

        # Ask for marks for 3 subjects
        marks = []
        for i in range(1, 4):
            mark = get_valid_mark(f"Enter mark for subject {i}: ")
            marks.append(mark)

        # Calculate average
        average = sum(marks) / len(marks)

        # Assign Grade/Result
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Formatted Output
        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")
        print(f"Grade  : {grade}")
        print("-" * 30)

if __name__ == "__main__":
    main()
