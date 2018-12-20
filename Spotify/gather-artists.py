import spotipy
import re
import spotipy.oauth2 as oauth2
import csv
import string

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


with open("artist-uris.csv",'a+',encoding='utf-8') as csvwritefile:
    writer = csv.writer(csvwritefile)
    # # # Get list of artists with the genre 'christmas'
    i = 0
    for letter in list(string.ascii_lowercase):
        search_term = letter + "*"
        print(search_term)
        i = 0
        while i <= 5000:
            results = sp.search(q=search_term,limit=50,type='artist',offset=i)
            for artist in results['artists']['items']:
                writer.writerow([artist['name'],artist['uri']])
            if len(results['artists']['items']) == 0:
                break
            i += 50

