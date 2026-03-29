goal_steps = 10000

while True:  # Infinite loop (user exits with 'q' or 'quit')
    current_steps = int(input("Enter your current step count (or 'q' to quit): "))

    if current_steps < 0:
        print("Invalid input. Please enter a non-negative step count.")
        continue  # Skip to the next iteration if input is invalid

    if current_steps >= goal_steps:
        print("Congratulations! You reached your daily step goal!")
        break  # Exit the loop if goal is reached

    print("Keep going! You're almost there!")