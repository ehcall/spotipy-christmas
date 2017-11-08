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

    print(client_id + "\n" + client_secret)

# # # Spotify authentication
credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

# # # Get list of artists with the genre 'christmas'
with open("artist-uris.csv",'w') as csvwritefile:
    writer = csv.writer(csvwritefile)
    i = 0
    while i <= 100:
        results = sp.search(q='genre:christmas', offset=i, type='artist', limit=50)
        items = results['artists']['items']
        for item in items:
            writer.writerow([item['uri'],item['name']])
        i += 1

# # # Get list of artists with the genre 'holiday'
with open("artist-uris.csv",'w') as csvwritefile:
    writer = csv.writer(csvwritefile)
    i = 0
    while i <= 100:
        results = sp.search(q='genre:holiday', offset=i, type='artist', limit=50)
        items = results['artists']['items']
        for item in items:
            writer.writerow([item['uri'], item['name']])
        i += 1

# # # Get list of artists with the genre 'chanukah'
with open("artist-uris.csv",'w') as csvwritefile:
    writer = csv.writer(csvwritefile)
    i = 0
    while i <= 100:
        results = sp.search(q='genre:chanukah', offset=i, type='artist', limit=50)
        items = results['artists']['items']
        for item in items:
            writer.writerow([item['uri'], item['name']])
        i += 1

# # # Get list of artists with the genre 'carols'
with open("artist-uris.csv",'w') as csvwritefile:
    writer = csv.writer(csvwritefile)
    i = 0
    while i <= 100:
        results = sp.search(q='genre:carols', offset=i, type='artist', limit=50)
        items = results['artists']['items']
        for item in items:
            writer.writerow(item['uri'], item['name'])
        i += 1