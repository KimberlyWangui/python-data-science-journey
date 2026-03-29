coin_milestones = [1, 10, 100, 1000, 10000, 100000, 1000000]
congratulatory_messages = [
    "Congratulations! You've collected your first coin!",           
    "Great job! You've collected 10 coins!",
    "Awesome! You've collected 100 coins!",
    "Fantastic! You've collected 1,000 coins!",
    "Incredible! You've collected 10,000 coins!",
    "Amazing! You've collected 100,000 coins!",
    "Unbelievable! You've collected 1,000,000 coins!"
]

for milestone in coin_milestones:
    current_message = congratulatory_messages[coin_milestones.index(milestone)]
    print(current_message)