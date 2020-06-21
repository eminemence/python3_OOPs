song_library = [
    ("Phanton of the Opera", "Sarah Brightman"),
    ("Knocking on a heaven's door", "Guns N Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns in the ivy", "Opeth"),
    ("November Rain", "Guns N Roses"),
    ("Beautuful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

artists = set()

for song, artist in song_library:
    artists.add(artist)

print(artists)
