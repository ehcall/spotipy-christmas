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

with open("christmas.csv",'a+',encoding="utf-8",newline='') as writefile:
    csvwriter = csv.writer(writefile)
    offset_num = 0
    while offset_num <= 100000:
        try:
            results = sp.search(q='genre:christmas', limit=50, type='track', offset=offset_num)
            print(results)
            tracks = results['tracks']['items']
            for track in tracks:
                track_id = track['id']
                track_name = track["name"]
                print(track_name)
                artist_names = []
                artist_ids = []
                for artist in track["artists"]:
                    artist_names.append(artist["name"])
                    artist_ids.append(artist['id'])
                album_name = track['album']['name']
                album_id = track['album']['id']
                csvwriter.writerow([track_name, track_id, artist_names, artist_ids, album_name, album_id])
        except:
            print("something broke")
        offset_num+=50