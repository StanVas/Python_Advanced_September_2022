# https://judge.softuni.org/Contests/Practice/Index/3534#2
def add_songs(*args):  # args = songs
    songs = {}
    for song in args:
        title = song[0]
        lyrics = song[1]
        if title not in songs:
            songs[title] = []
        songs[title].extend(lyrics)

    output = []
    for key, value in songs.items():
        output.append("- " + key)
        output.extend(value)

    return "\n".join(output)


# input
print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
