import spotipy
import re
import spotipy.oauth2 as oauth2

# # # Import client id and client secret (and username). I know there's a better way to set ENV variables, but I'm not gonna learn how right now.
with open('../spotify-christmas-keysecret.txt', encoding="ascii") as txtfile:
    lines = txtfile.readlines()
    client_id = re.sub("client_id = ", "", lines[0])
    client_id = re.sub("\n","",client_id)

    client_secret = re.sub("client_secret = ", "", lines[1])
    client_secret = re.sub("\n", "", client_secret)

    print(client_id + "\n" + client_secret)

wiki_christmas = []
with open('wiki-christmas-albums.txt') as readfile:
    for line in readfile:
        wiki_christmas.append(line[:-1].lower())

# # # Spotify authentication
credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

# # # Import uri list
album_uris = []
with open("album-uris.txt") as urifile:
    for line in urifile:
        album_uris.append(line)

# # # Get christmas only album uris
christmas_albums = []
for uri in album_uris:
    album_uri = uri[:-1]
    try:
        to_check = sp.album(album_uri)
    except:
        token = credentials.get_access_token()
        sp = spotipy.Spotify(auth=token)
        to_check = sp.album(album_uri)
    print(to_check["genres"], to_check["name"])
    print(album_uri)
    album_name = to_check["name"].lower()
    if 'christmas' in to_check["genres"]:
        print(uri)
        christmas_albums.append(album_uri)
    elif re.search('christmas', album_name):
        print(album_name, uri)
        christmas_albums.append(album_uri)
    elif re.search('holiday', album_name):
        print(album_name)
        christmas_albums.append(album_uri)
    elif re.search('winter', album_name):
        print(album_name)
        christmas_albums.append(album_uri)
    elif album_name in wiki_christmas:
        print(album_name)
        christmas_albums.append(album_uri)
    print(len(christmas_albums))

with open("christmas-album-uris.txt", "w") as wfile:
    for christmas_album in christmas_albums:
        wfile.write(christmas_album)