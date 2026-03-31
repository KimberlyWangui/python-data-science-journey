artist_songs = {
    "The Beatles": ["Hey Jude", "Let It Be", "Yesterday"],
    "Taylor Swift": ["Love Story", "Shake It Off", "Blank Space"],
    "Ed Sheeran": ["Shape of You", "Perfect", "Thinking Out Loud"],
    "Adele": ["Hello", "Someone Like You", "Rolling in the Deep"],
    "Beyoncé": ["Single Ladies", "Halo", "Crazy in Love"],
    "Drake": ["God's Plan", "In My Feelings", "One Dance"],
    "Bruno Mars": ["Uptown Funk", "Just the Way You Are", "Grenade"],
    "Rihanna": ["Umbrella", "Diamonds", "Work"]
}

# Accessing songs by an artist
print(artist_songs["The Beatles"])  # Output: ['Hey Jude', 'Let It Be', 'Yesterday']
print(artist_songs["Taylor Swift"])  # Output: ['Love Story', 'Shake It Off', 'Blank Space']
print(artist_songs["Ed Sheeran"])  # Output: ['Shape of You', 'Perfect', 'Thinking Out Loud']
print(artist_songs["Adele"])  # Output: ['Hello', 'Someone Like You', 'Rolling in the Deep']
print(artist_songs["Beyoncé"])  # Output: ['Single Ladies', 'Halo', 'Crazy in Love']
print(artist_songs["Drake"])  # Output: ['God's Plan', 'In My Feelings', 'One Dance']
print(artist_songs["Bruno Mars"])  # Output: ['Uptown Funk', 'Just the Way You Are', 'Grenade']
print(artist_songs["Rihanna"])  # Output: ['Umbrella', 'Diamonds', 'Work']

# Iterating through the songs
for artist, songs in artist_songs.items():
    print(f"{artist}:")
    for song in songs:
        print(f"  - {song}")

# Checking if users favorite artist is in the dictionary
favorite_artist = input("Enter your favorite artist: ")
if favorite_artist in artist_songs: # Checks if the user's favorite artist is a key in the artist_songs dictionary
    print(f"{favorite_artist} is in the dictionary. Here are some of their songs:")
    for song in artist_songs[favorite_artist]: # Accesses the list of songs for the user's favorite artist and iterates through it, printing each song with a dash in front for formatting.
        print(f"  - {song}")
else:
    print(f"Sorry, {favorite_artist} is not in the dictionary.")