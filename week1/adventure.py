location = input("Choose your location (forest, cave, beach): ").lower()

if location != "forest" and location != "cave" and location != "beach":
    print("Invalid location. Please choose 'forest', 'cave', or 'beach'.")
    exit()

if location == "forest":
    print("You are in a dark forest. You see a path leading to a mysterious cave.")
elif location == "cave":
    print("You are in a damp cave. You see a glimmer of light coming from a tunnel.")
else:
    print("You are on a sunny beach. You see a boat anchored offshore.")


