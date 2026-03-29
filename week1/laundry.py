'''
number_of_folded_shirts = 0

while number_of_folded_shirts < 5:
    print(f"You have folded {number_of_folded_shirts} shirts.")
    number_of_folded_shirts += 1  # Increment the count of folded shirts

print("You have folded all 5 shirts!")
'''

'''
number_of_folded_shirts = 0

while True:
    
    user_input = input("Enter done to stop folding shirts: ")

    if user_input.lower() == "done":
        break

    number_of_folded_shirts += 1  # Increment the count of folded shirts
    print(f"You have folded {number_of_folded_shirts} shirts.")

print("You have folded all the shirts you wanted to fold!")
'''

clothes = {
    "shirts": 0,
    "socks": 0,
    "pants": 0
}

while True:
    item = input("Enter clothing type (shirts, socks, pants) or 'done' to stop: ").lower()

    if item == "done":
        break

    if item in clothes:
        clothes[item] += 1
        print(f"You have folded {clothes[item]} {item}.")
    else:
        print("Invalid clothing type. Try again.")

print("\nFinal count:")
for item, count in clothes.items():
    print(f"{item.capitalize()}: {count}")
