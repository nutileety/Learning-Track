def make_album(artist_name,album_title,no_songs=None):
    music_album={
                'artist':artist_name,
                'album':album_title
                }
    if no_songs:
        music_album['no_of_songs'] = no_songs
    print("\nThe list of the singer and his album: ")
    return music_album

while True:
    print("\n(if yu want to quit enter 'q')")
    singer = input("Name of the artist: ").title()
    if singer.lower() == 'q':
        break

    song = input("The name of the song of that singer: ").title()
    if song.lower() == 'q':
        break

    output = make_album(singer,song)
    print(output)
