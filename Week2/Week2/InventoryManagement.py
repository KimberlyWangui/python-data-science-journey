inventory = {
    "laptop": {"quantity": 2, "price": 50.0},
    "phone": {"quantity": 5, "price": 30.0},
    "tablet": {"quantity": 3, "price": 20.0},
    "headphones": {"quantity": 10, "price": 15.0},
    "monitor": {"quantity": 4, "price": 100.0},
    "Bluetooth Speaker": {"quantity": 6, "price": 25.0}
    }

# Function to safely get a number - either an integer or a float - from user input
def get_valid_number(prompt, num_type=float):
    while True:
        try:
            value = num_type(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to add products to the inventory
def add_product(name, quantity, price):
    if name in inventory:
        print(f"Product '{name}' already exists in the inventory.")
    else:
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"Product '{name}' added to the inventory.")

# Function for viewing product information
def view_product(name):
    product = inventory.get(name)
    if product:
        print(f"Product: {name}, Quantity: {product['quantity']}, Price: ${product['price']}")
    else:
        print(f"Product '{name}' not found in the inventory.")

# Function to update product quantity
def update_quantity (name, new_quantity):
    if name in inventory:
        if new_quantity < 0:
            print("Quantity cannot be negative. Please try again.")
        else:
            inventory[name]['quantity'] = new_quantity
            print(f"Quantity for product '{name}' updated to {new_quantity}.")
    else:
        print(f"Product '{name}' not found in the inventory.")

# Function to remove products from the inventory
def remove_product(name):
    removed = inventory.pop(name, None) #pop method removes the specified key and returns the corresponding value. If the key is not found, it returns None.
    if removed:
        print(f"Product '{name}' removed from the inventory.")
    else:
        print(f"Product '{name}' not found in the inventory.")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Product")
        print("3. Update Quantity")
        print("4. Remove Product")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            quantity = get_valid_number("Enter product quantity: ", int)
            price = get_valid_number("Enter product price: ", float)
            add_product(name, quantity, price)
        elif choice == '2':
            name = input("Enter product name: ")
            view_product(name)
        elif choice == '3':
            name = input("Enter product name: ")
            new_quantity = get_valid_number("Enter new quantity: ", int)
            update_quantity(name, new_quantity)
        elif choice == '4':
            name = input("Enter product name: ")
            remove_product(name)
        elif choice == '5':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()