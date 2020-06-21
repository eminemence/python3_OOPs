my_artists = {"Sarah Brightman", "Guns N' Roses", "Opeth", "Vixy and Tony"}
auburns_artists = {"Nickelback", "Guns N' Roses", "Savage Garden"}

print("All: {}".format(my_artists.union(auburns_artists)))
print("Both: {}".format(my_artists.intersection(auburns_artists)))
print(
    "Either but not both: {}".format(my_artists.symmetric_difference(auburns_artists))
)
