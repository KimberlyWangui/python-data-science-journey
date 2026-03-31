user_data = [
   ("RNB", ["The Weeknd", "Doja Cat", "SZA"]),
   ("RNB", ["Odeal", "Summer Walker", "H.E.R."]),
   ("Pop", ["Adele", "Bruno Mars", "Lady Gaga"]),
   ("Pop", ["Taylor Swift", "Ariana Grande", "Ed Sheeran"]),
   ("Pop", ["Billie Eilish", "Dua Lipa", "Justin Bieber"]),
   ("Hip-Hop", ["Kendrick Lamar", "Drake", "Cardi B"]),
   ("Hip-Hop", ["J. Cole", "Travis Scott", "Megan Thee Stallion"]),
   ("Rock", ["Imagine Dragons", "Linkin Park", "Foo Fighters"]),
   ("Country", ["Luke Combs", "Carrie Underwood", "Chris Stapleton"])
]

genre_counts = {}

# Count the number of genres
for genre, artists in user_data:
    if genre in genre_counts:
        genre_counts[genre] += 1
    else:
        genre_counts[genre] = 1

print("Genre counts:", genre_counts)

# Find the most common genre
most_common_genre = max(genre_counts, key=genre_counts.get)
print("Most popular genre:", most_common_genre)

# Find users who listen to a specific artist
target_artist = "Adele"
user_listening = []

for index, (genre, artists) in enumerate(user_data):
    if target_artist in artists:
        user_listening.append(index)

if user_listening:
  print(f"Users who listened to {target_artist}:", user_listening)
else:
  print(f"No users listened to {target_artist} this week.")