# Pizza Order Cost Calculator
# User Input
pizza_size = input("Enter pizza size (small, large): ").lower()
number_of_toppings = int(input("Enter number of toppings: "))
delivery_distance = float(input("Enter delivery distance in miles: "))

# Input Validation
if pizza_size not in ["small", "large"]:
    print("Invalid pizza size. Please enter 'small' or 'large'.")
    exit()

if number_of_toppings < 0 or delivery_distance < 0:
    print("Invalid input. Number of toppings and delivery distance cannot be negative.")
    exit()

# Base Cost Calculation
if pizza_size == "small":
    base_cost = 8
else:
    base_cost = 12

# Topping Cost Calculation
topping_cost = number_of_toppings * 1

# Delivery Cost Calculation
if delivery_distance == 0:
    delivery_cost = 0  # pickup
elif delivery_distance <= 5:
    delivery_cost = 2
else:
    delivery_cost = 2 + (delivery_distance - 5) * 1

# Total Cost Calculation
total_cost = base_cost + topping_cost + delivery_cost

# Output the order summary and total cost
print("\nOrder Summary:")   
print(f"Pizza Size: {pizza_size}")
print(f"Number of Toppings: {number_of_toppings}")
print(f"Delivery Distance: {delivery_distance} miles")
print(f"The total cost of your pizza order is: ${total_cost:.2f}")