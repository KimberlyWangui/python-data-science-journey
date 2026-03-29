star_milestone = [1, 10, 100, 1000, 10000, 100000, 1000000]
congratulatory_messages = [
    "Congratulations! You've collected your first star!",       
    "Great job! You've collected 10 stars!",
    "Awesome! You've collected 100 stars!",
    "Fantastic! You've collected 1,000 stars!",
    "Incredible! You've collected 10,000 stars!",
    "Amazing! You've collected 100,000 stars!",
    "Unbelievable! You've collected 1,000,000 stars!"
]

for milestone in star_milestone:
    message_index = star_milestone.index(milestone)
    current_message = congratulatory_messages[message_index]

    print(current_message)

print(f"\nCongratulations on reaching all the star milestones! You've reached {len(star_milestone)} milestones in total!")