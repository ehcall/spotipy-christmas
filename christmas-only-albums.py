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


# # # Get albums uris
with open("christmas-album-uris.txt",'w') as wfile:
    for uri in album_uris:
        #print(uri[:-1])
        to_check = sp.album(uri[:-1])
        print(to_check["genres"],to_check["name"])
        if 'christmas' in to_check["genres"]:
            print(uri)
            wfile.write(uri)
        elif re.search('christmas',to_check["name"].lower()):
            print(to_check["name"])
            wfile.write(uri)
        elif re.search('holiday',to_check["name"].lower()):
            print(to_check["name"])
            wfile.write(uri)
