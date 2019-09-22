def song_decoder(song):
    my_string = song.replace("WUB", " ").split()
    new_str = ""
    for i in my_string:
        new_str += i + " "
    return new_str[:-1]
