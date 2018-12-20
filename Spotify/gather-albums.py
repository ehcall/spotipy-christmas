import spotipy
import re
import spotipy.oauth2 as oauth2
import csv

# # # Import client id and client secret (and username). I know there's a better way to set ENV variables, but I'm not gonna learn how right now.
with open('../spotify-christmas-keysecret.txt', encoding="ascii") as txtfile:
    lines = txtfile.readlines()
    client_id = re.sub("client_id = ", "", lines[0])
    client_id = re.sub("\n","",client_id)

    client_secret = re.sub("client_secret = ", "", lines[1])
    client_secret = re.sub("\n", "", client_secret)

    #print(client_id + "\n" + client_secret)

# # # Spotify authentication
credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

# # # Import uri list
artist_uris = []
with open("artist-uris.csv",encoding='utf-8') as urifile:
    csvreader = csv.reader(urifile)
    for line in csvreader:
        artist_uris.append(line[1])

# # # Get albums uris
with open("album-uris.csv",'a+',encoding="utf-8") as writefile:
    csvwriter = csv.writer(writefile)
    for uri in artist_uris:
        try:
            results = sp.artist_albums(uri)
            albums = results['items']
            while results['next']:
                results = sp.next(results)
                albums.extend(results['items'])
            for album in albums:
                csvwriter.writerow([album["name"],album['uri'],uri])
        except:
            token = credentials.get_access_token()
            sp = spotipy.Spotify(auth=token)
            results = sp.artist_albums(uri)
            albums = results['items']
            while results['next']:
                results = sp.next(results)
                albums.extend(results['items'])
            for album in albums:
                csvwriter.writerow([album["name"], album['uri'], uri])
