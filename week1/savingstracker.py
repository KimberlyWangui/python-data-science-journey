savings_goal = int(input("Enter your savings goal: "))
current_savings = 0

while current_savings < savings_goal:
    amount = float(input("Enter the amount you saved (or 'q' to quit): "))

    if amount < 0:
        print("Invalid input. Please enter a non-negative amount.")
        continue  # Skip to the next iteration if input is invalid

    current_savings += amount
    print(f"Current savings: {current_savings}")
    print(f"Keep saving! You're {savings_goal - current_savings:.2f} ksh away from your goal.")

print("Congratulations! You reached your savings goal!")