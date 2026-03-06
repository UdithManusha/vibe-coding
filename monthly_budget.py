def get_valid_float(prompt):
    """Prompts for a numeric value and handles invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Monthly Budget Calculator")
    print("-" * 30)

    # Get total monthly budget
    total_budget = get_valid_float("Enter your total monthly budget: ")
    
    total_expenses = 0
    print("\nEnter your expenses one by one. Type 'done' to finish.")
    
    # Expense entry loop
    while True:
        user_input = input("Enter expense amount (or 'done'): ").strip().lower()
        
        if user_input == 'done':
            break
            
        try:
            expense = float(user_input)
            total_expenses += expense
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Calculate remaining balance
    remaining_balance = total_budget - total_expenses

    # Display results
    print("-" * 30)
    print(f"Total Budget     : {total_budget:,.2f} LKR")
    print(f"Total Expenses   : {total_expenses:,.2f} LKR")
    print(f"Remaining Balance: {remaining_balance:,.2f} LKR")
    
    # Check for low funds
    if remaining_balance < 500:
        print("Warning: Low Funds")
    
    print("-" * 30)

if __name__ == "__main__":
    main()
